from PIL import Image
from pathlib import Path
from mapping import mapping

def get_colour(mode: str, val: float) -> float | tuple[int, ...]:
    if mode == "HSV":
        return (int(val * 255), 255, 255)
    
    if mode == "L":  # greyscale
        return int(val * 255)

def plot(
    mode: str = "HSV",
    img_size: tuple[int, int] = (500, 500),
    x_range: tuple[int, int] = (0, 1),
    y_range: tuple[int, int] = (0, 1),
) -> Image:
    image = Image.new(mode=mode, size=img_size)

    x_pixel_height = (x_range[1] - x_range[0]) / img_size[0]
    y_pixel_height = (y_range[1] - y_range[0]) / img_size[1]

    for x in range(img_size[0]):
        real = x * x_pixel_height
        for y in range(img_size[1]):
            imag = y * y_pixel_height

            val = mapping(real + imag * 1j)
            image.putpixel((x, y), get_colour(mode, val))
    
    return image

def save_img(img: Image, name: str) -> None:
    fp = Path("images/pillow") / f"{name}.png"
    
    converted = img.convert("RGB")
    converted.save(fp)

if __name__ == "__main__":
    save_img(plot(), "0to1")
