from __future__ import annotations

import bpy
import sys
from subprocess import call
from typing import Tuple
from zlib import decompress
from array import array

try:
    from PIL import Image
except ImportError:
    Image = None


def support_pillow() -> bool:
    '''Check whether Pillow is installed.'''
    return bool(Image)


def install_pillow():
    '''Install Pillow and import the Image module.'''
    args = [sys.executable, '-m', 'pip', 'install', 'Pillow']

    if not call(args=args, timeout=60):
        global Image
        from PIL import Image


def can_load(filepath: str) -> bool:
    '''Return whether an image can be loaded.'''
    with open(filepath, 'rb') as bip:
        magic = bip.read(4)

        if magic == b'BIP1':
            return True

    return support_pillow()


def load_file(filepath: str, max_size: tuple) -> Tuple[tuple, list]:
    '''Load image preview data from file.

    Args:
        filepath: The input file path.
        max_size: Scale images above this size down.

    Returns:
        The size and pixels of the image.

    Raises:
        AssertionError: If pixel data type is not 32 bit.
        ValueError: If file is not BIP and PIL is not found.
    '''
    with open(filepath, 'rb') as bip:
        magic = bip.read(4)

        if magic == b'BIP1':
            width = int.from_bytes(bip.read(2), 'big')
            height = int.from_bytes(bip.read(2), 'big')
            data = decompress(bip.read())

            if support_pillow() and _should_resize((width, height), max_size):
                image = Image.frombytes('RGBA', (width, height), data)
                image = _resize_image(image, max_size)

                width, height = image.size
                data = image.tobytes()

            pixels = array('i', data)
            assert pixels.itemsize == 4, '32 bit type required for pixels'

            return ((width, height), pixels)

    if support_pillow():
        with Image.open(filepath) as image:
            if _should_resize(image.size, max_size):
                image = _resize_image(image, max_size)

            image = image.transpose(Image.FLIP_TOP_BOTTOM)
            image = image.convert('RGBA')

            pixels = array('i', image.tobytes())
            assert pixels.itemsize == 4, '32 bit type required for pixels'

            return (image.size, pixels)

    raise ValueError('input is not a supported file format')


def _should_resize(size: tuple, max_size: tuple) -> bool:
    '''Check whether width or height is greater than maximum.'''
    if max_size[0] and size[0] > max_size[0]:
        return True

    if max_size[1] and size[1] > max_size[1]:
        return True

    return False


def _resize_image(image: Image.Image, max_size: tuple) -> Image.Image:
    '''Resize image to fit inside maximum.'''
    scale = min(
        max_size[0] / image.size[0] if max_size[0] else 1,
        max_size[1] / image.size[1] if max_size[1] else 1,
    )

    width = int(image.size[0] * scale)
    height = int(image.size[1] * scale)
    return image.resize(size=(width, height))


def tag_redraw():
    '''Redraw every region in Blender.'''
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            for region in area.regions:
                region.tag_redraw()
