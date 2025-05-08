import os
os.makedirs("output", exist_ok=True)
import argparse
from image_to_3d import image_to_3d_model
from text_to_3d import text_to_3d_model
from viewer import display_3d_model

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', required=True, help='Input image path')
    parser.add_argument('--output', required=True, help='Output folder path')
    args = parser.parse_args()

    if args.image:
        image_to_3d_model(args.image, args.output)
    elif args.text:
        text_to_3d_model(args.text, args.output)
    else:
        print("Please provide either an image or a text description as input.")
        return

    display_3d_model(args.output)

if __name__ == "__main__":
    main()