from PIL import Image

class ImageProcess:
    def __init__(self):
        self.default_path = 'C:\Users\offic\OneDrive\Документы\Скриншот'

    def compress(self, fpath, in_place: bool=True) -> None:
        img = Image.open(fpath)
        # need to get extension
        ext = img.format.lower()  # lower just for robustness
        out_path = fpath if in_place else self.default_path
        params = {'optimize': True}

        simple_exts = ['png', 'gif', 'avif', 'bmp']
        match ext:
            case ext if ext in simple_exts:
                ...
            case _:
                ...

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
    