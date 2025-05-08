import torch
import cv2
import numpy as np
import open3d as o3d

def image_to_3d_model(image_path, output_path):
    model_type = "DPT_Large"
    midas = torch.hub.load("intel-isl/MiDaS", model_type)
    midas.to("cpu").eval()

    
    midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
    transform = midas_transforms.dpt_transform

    
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

   
    input_tensor = transform(img_rgb) 
    if isinstance(input_tensor, tuple):
        input_tensor = input_tensor[0]

    input_tensor = input_tensor

   
    with torch.no_grad():
        prediction = midas(input_tensor)
        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size=img_rgb.shape[:2],
            mode="bicubic",
            align_corners=False,
        ).squeeze()

    depth_map = prediction.cpu().numpy()

    
    height, width = depth_map.shape
    fx = fy = 1.0
    cx, cy = width / 2, height / 2

    points = []
    colors = []

    for v in range(height):
        for u in range(width):
            z = depth_map[v, u]
            x = (u - cx) * z / fx
            y = (v - cy) * z / fy
            points.append((x, y, z))
            colors.append(img_rgb[v, u] / 255.0)

    points = np.array(points)
    colors = np.array(colors)

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    pcd.colors = o3d.utility.Vector3dVector(colors)

    o3d.io.write_point_cloud(output_path, pcd)
    print(f"✅ Saved 3D point cloud to: {output_path}")
