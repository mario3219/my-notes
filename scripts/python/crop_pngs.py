import os
import sys
from PIL import Image

def crop_image(input_path, output_path, box):
    img = Image.open(input_path)
    cropped = img.crop(box)
    cropped.save(output_path)
    print(f"Cropped → {output_path}")

def process_path(path, out_dir, box):
    if os.path.isfile(path):
        filename = os.path.basename(path)
        out_path = os.path.join(out_dir, filename)
        crop_image(path, out_path, box)

    elif os.path.isdir(path):
        for file in os.listdir(path):
            if file.lower().endswith(".png"):
                in_path = os.path.join(path, file)
                out_path = os.path.join(out_dir, file)
                crop_image(in_path, out_path, box)
    else:
        print("Input path not found!")

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage:")
        print("python crop_pngs.py <input_path> <output_folder> left top right bottom")
        print("Example:")
        print("python crop_pngs.py images cropped 0 0 500 500")
        sys.exit(1)

    input_path = sys.argv[1]
    output_dir = sys.argv[2]
    left, top, right, bottom = map(int, sys.argv[3:7])

    os.makedirs(output_dir, exist_ok=True)

    crop_box = (left, top, right, bottom)
    process_path(input_path, output_dir, crop_box)

