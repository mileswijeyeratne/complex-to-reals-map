# complex-to-reals-map

## Overview

This project is following on from a discussion about whether the size of ℂ is the same as the size of ℝ. The way to show that this is true is to create a mapping from 1 set to the other that maps each element in 1 set uniquely to each element in the other leaving none left over.
 
A way we can achieve this is by interlacing the digits of the real and imaginary parts of a compex number to create a unique real. 

The problem is, this is quite hard to visualise so I decided to write some scrips to help with that.

## Implementation

The impelementation for this interlacing mapping function can be found in the [`mapping.py`](/mapping.py) file. Here is the core logic:

```python
def mapping(point: complex) -> float:
    digits_before_decimal: int = len(str(int(max(point.real, point.imag))))
    num_chars: int = digits_before_decimal + 4 # 4 = 3 for 3dp + 1 for the '.' character
    a: str = f"{float(point.real):0{num_chars}.3f}"
    b: str = f"{float(point.imag):0{num_chars}.3f}"

    res: str = ""
    for i in range(num_chars):
        if i == digits_before_decimal:
            res += "."
            continue

        res += a[i]
        res += b[i]

    return float(res)
```

The visulisation is done in 2 different ways. Originally I used the [`Pillow`](https://python-pillow.org/) module but this didn't show all the information I wanted so I switched to using [`matplotlib`](https://matplotlib.org/).

## Visualizations

The [`images`](/images/) folder contains two sub-folders: [`pillow`](/images/pillow/) and [`matplotlib`](/images/matplotlib/). These contain the images made with each tool respectively.

## Creating new Visualizations

Append to the [`main_matplotlib.py1`](/main_matplotlib.py) or [`main_pillow.py`](/main_pillow.py) scripts and run them. This will add new images to the folders mentioned previously.

## Interesting findings

The mapping creates a grid pattern which repeats a factor of 10 larger as each new decimal place adds precision. This can be shown through mapping the [0-1](/images/matplotlib/0to1_clamped.png) range vs the [0-10](/images/matplotlib/0to10_clamp100.png) range. The result is the same image just on a larger scale. Note: We do need to clamp the values to 1 and 100 repectivley as otherwise the largest value will dominate the scale and leave an uninteresting result (as shown in [this photo](/images/matplotlib/0to1.png))