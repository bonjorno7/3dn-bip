from typing import Union, Tuple, List
from pathlib import Path
from zlib import decompress
from array import array

try:
    from PIL import Image
except:
    _SUPPORT_PIL = False
else:
    _SUPPORT_PIL = True


def load_file(filepath: Union[str, Path]) -> Tuple[int, int, List[int]]:
    '''Load image preview data from file.

    Args:
        filepath: The input file path.

    Returns:
        The width, height, and pixels.

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

            pixels = array('i', data)
            assert pixels.itemsize == 4, '32 bit type required for pixels'

            return width, height, pixels

    if _SUPPORT_PIL:
        with Image.open(filepath) as image:
            image = image.transpose(Image.FLIP_TOP_BOTTOM)
            image = image.convert('RGBA')

            width, height = image.size
            data = image.tobytes()

            pixels = array('i', data)
            assert pixels.itemsize == 4, '32 bit type required for pixels'

            return width, height, pixels

    raise ValueError('input is not a supported file format')
