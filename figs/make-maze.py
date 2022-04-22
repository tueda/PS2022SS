"""Encode the maze."""
import base64
import textwrap
import zlib
from typing import Sequence

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

BitMatrix = Sequence[Sequence[int]]


def show_bitmatrix(a: BitMatrix) -> None:
    """Show a bit matrix."""
    fig, ax = plt.subplots()
    ax.matshow(a, vmin=0, vmax=1)
    ax.axis("off")
    plt.show()


def bitmatrix_to_bytes(a: BitMatrix) -> bytes:
    """Convert a bit matrix to bytes."""
    n = 0
    for i, x in enumerate(sum(a, [])):
        n += x << i
    return n.to_bytes((n.bit_length() + 7) // 8, "big")


def bytes_to_bitmatrix(data: bytes, m: int, n: int) -> BitMatrix:
    """Convert bytes to a bit matrix."""
    a = [[0] * n for _ in range(m)]
    b = int.from_bytes(data, "big")
    for i in range(m * n):
        a[i // n][i % n] = (b >> i) & 1
    return a


def bytes_to_compressedstr(data: bytes) -> str:
    """Convert bytes to a compressed string."""
    return base64.b64encode(zlib.compress(data)).decode()


def compressedstr_to_bytes(s: str) -> bytes:
    """Convert a compressed string to bytes."""
    return zlib.decompress(base64.b64decode(s.replace(" ", "").encode()))


def main() -> None:
    """Entry point."""
    im = Image.open("maze.png")
    a = np.array(im)
    # print(im.size)
    # print(a.shape)
    m = [[0] * a.shape[1] for _ in range(a.shape[0])]
    # print(len(m))
    for i in range(a.shape[1]):
        for j in range(a.shape[0]):
            if tuple(a[j, i]) != (255, 255, 255, 255):
                m[j][i] = 1
    print(f"# {a.shape[0], a.shape[1]}")
    for s in textwrap.wrap(bytes_to_compressedstr(bitmatrix_to_bytes(m))):
        print(s)


if __name__ == "__main__":
    main()
