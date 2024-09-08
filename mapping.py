def mapping(point: complex) -> float:
    """
    A mapping from a complex point to a real number using a method of interlacing digits.
    To make it simple, it takes the absolute value of all negative parts.
    """
    point = abs(point.real) + abs(point.imag) * 1j

    assert(point.real >= 0)
    assert(point.imag >= 0)

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


if __name__ == "__main__":
    print(mapping(-0.5 + 0.5j))