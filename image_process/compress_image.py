import sys
from PIL import Image

def compress_image(filepath):
    img = Image.open(filepath)
    ext = img.format.lower()
    out_path = filepath
    params = {}

    if ext == "jpeg" or ext == "jpg":
        params = {"quality": 60, "optimize": True}
    elif ext == "png":
        params = {"optimize": True}
    elif ext == "gif":
        params = {"optimize": True}
    elif ext == "bmp":
        params = {}
    else:
        # Unsupported format
        return

    img.save(out_path, **params)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Передайте путь к файлу")
        sys.exit(1)
    compress_image(sys.argv[1])