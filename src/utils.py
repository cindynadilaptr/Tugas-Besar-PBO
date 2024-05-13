#!/usr/bin/env python3

"""utils.py: Utility functions."""

import time
import moderngl
import pygame
from typing import List, Tuple
from PIL import Image, ImageDraw

from src.constants import SCALE_FACTOR

def scale_to_resolution(size: int | float) -> int:
    """Skalakan ukuran ke resolusi saat ini."""
    return round(size * SCALE_FACTOR)

def get_height(image: str) -> int:
    """Mendapatkan ketinggian gambar."""
    img: Image.Image = Image.open(image)
    return img.height

def surface_to_texture(ctx: moderngl.Context, surface: pygame.Surface) -> moderngl.Texture:
    """Mengonversi pygame.Surface menjadi moderngl.Texture."""
    texture: moderngl.Texture = ctx.texture(surface.get_size(), 4)
    texture.filter = moderngl.NEAREST, moderngl.NEAREST
    texture.swizzle = 'BGRA'
    texture.write(surface.get_view('1'))
    return texture

DEFAULT_PALETTE = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
DEFAULT_WEIGHTS = [1, 1, 1]

def extract_color_palette(image: str) -> Tuple[List[Tuple[int, int, int]], List[int]]:
    """Mengekstrak palet warna dari gambar."""
    img: Image.Image = Image.open(image)
    colors: List[Tuple[int, int, int]] = img.getcolors(maxcolors=256)
    if colors is None:
        return DEFAULT_PALETTE, DEFAULT_WEIGHTS
    else:
        palette: List[Tuple[int, int, int]] = [color for (_, color) in colors]
        weights: List[int] = [count for (count, _) in colors]
        return palette, weights