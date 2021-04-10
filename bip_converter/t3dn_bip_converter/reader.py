from typing import Union
from pathlib import Path
from PIL import Image
from zlib import decompressobj


def convert(input_path: Union[str, Path], output_path: Union[str, Path]):
    '''Convert BIP to various image formats.'''
    input_path = Path(input_path).resolve()
    output_path = Path(output_path).resolve()

    with open(input_path, 'rb') as bip:
        magic = bip.read(4)

        if magic != b'BIP1':
            raise ValueError('input is not a supported file format')

        width = int.from_bytes(bip.read(2), 'big')
        height = int.from_bytes(bip.read(2), 'big')

        decompressor = decompressobj()
        data = decompressor.decompress(bip.read())
        data += decompressor.flush()

        image = Image.frombytes('RGBA', (width, height), data)
        image = image.transpose(Image.FLIP_TOP_BOTTOM)

        try:
            image.save(output_path)
        except OSError:
            image.convert('RGB').save(output_path)
