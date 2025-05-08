# 3D Model Generator from Image 

This project allows you to generate a simple 3D object from:
- an image of a single item (like a toy, chair, etc.)

## How to Run
1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```
2. Install:
```bash
pip install -r requirements.txt
```
3. Run with image:
```bash
python main.py --image test.jpg --output output/model.ply
```
