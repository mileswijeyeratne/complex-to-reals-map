from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import numpy as np
from pathlib import Path
from mapping import mapping

def plot(
    img_size: tuple[int, int] = (500, 500),
    x_range: tuple[int, int] = (0, 1),
    y_range: tuple[int, int] = (0, 1),
    clamp: float = float("inf"),
) -> Figure:
    x = np.linspace(*x_range, img_size[0])
    y = np.linspace(*y_range, img_size[1])

    X, Y = np.meshgrid(x, y)
    
    Z = X + Y * 1j
    vectorized_mapping = np.vectorize(lambda x: min(mapping(x), clamp))
    Z = vectorized_mapping(Z)

    fig = plt.figure(figsize=(8,6))
    plt.pcolormesh(X, Y, Z, shading="auto", cmap="plasma")
    
    plt.colorbar(label="Real number mapping")
    plt.xlabel("Real part")
    plt.ylabel("Imaginary part")
    plt.title("Unique mapping of complex numbers onto reals")
    
    return fig   
    

def save_img(img: Figure, name: str) -> None:
    fp = Path("images/matplotlib") / f"{name}.png"
    img.savefig(fp)

if __name__ == "__main__":
    # save_img(plot(), "0to1")
    # save_img(plot(clamp=1), "0to1_clamped")
    # save_img(plot(x_range=(0, 1), y_range=(0, 2), clamp=3), "0to1and0to2")
    # save_img(plot(x_range=(0, 2), y_range=(0, 2)), "0to2")
    # save_img(plot(x_range=(0, 2), y_range=(0, 2), clamp=3), "0to2_clamped_3")
    save_img(plot(x_range=(0, 10), y_range=(0, 10), clamp=100), "0to10_clamp100")