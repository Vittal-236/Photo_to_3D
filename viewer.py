import open3d as o3d

def display_3d_model(file_path):
    print(f"Loading model from {file_path}")
    pcd = o3d.io.read_point_cloud(file_path)
    o3d.visualization.draw_geometries([pcd])
