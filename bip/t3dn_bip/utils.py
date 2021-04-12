import bpy
from typing import Tuple
from zlib import decompress
from array import array

try:
    from PIL import Image
except:
    _SUPPORT_PIL = False
else:
    _SUPPORT_PIL = True


def can_load(filepath: str) -> bool:
    '''Return whether an image can be loaded.'''
    with open(filepath, 'rb') as bip:
        magic = bip.read(4)

        if magic == b'BIP1':
            return True

    return _SUPPORT_PIL


def load_file(filepath: str) -> Tuple[tuple, list]:
    '''Load image preview data from file.

    Args:
        filepath: The input file path.

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

            pixels = array('i', decompress(bip.read()))
            assert pixels.itemsize == 4, '32 bit type required for pixels'

            return ((width, height), pixels)

    if _SUPPORT_PIL:
        with Image.open(filepath) as image:
            image = image.transpose(Image.FLIP_TOP_BOTTOM)
            image = image.convert('RGBA')

            pixels = array('i', image.tobytes())
            assert pixels.itemsize == 4, '32 bit type required for pixels'

            return (image.size, pixels)

    raise ValueError('input is not a supported file format')


def tag_redraw():
    '''Redraw every region in Blender.'''
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            for region in area.regions:
                region.tag_redraw()
