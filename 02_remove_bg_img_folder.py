import cv2
import rembg
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

in_dir = Path("Y")
out_dir = Path("Y_trf")

def is_image(absolute_path: Path):
    return absolute_path.is_file and str(absolute_path).endswith('.png')


input_filenames = [p for p in filter(is_image, Path(in_dir).iterdir())]


def process_image(in_dir):
    try:
        image = cv2.imread(str(in_dir))
        if image is None or not image.data:
            raise cv2.error("read failed")
        output = rembg.remove(image)
        in_dir = out_dir / in_dir.with_suffix(".png").name
        cv2.imwrite(str(in_dir), output)
    except Exception as e:
        print(f"{in_dir}: {e}", file=sys.stderr)


executor = ThreadPoolExecutor(max_workers=4)

i = 0
for result in executor.map(process_image, input_filenames):
    i+=1
    print(f"{i} Remove bg image {in_dir}: {result}")

print("FINISH")