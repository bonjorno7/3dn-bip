from typing import Union
from pathlib import Path
from PIL import Image
from zlib import compressobj, decompressobj


def image_to_bip(input_path: Union[str, Path], output_path: Union[str, Path]):
    '''Convert various image formats to BIP.'''
    input_path = Path(input_path).resolve()
    output_path = Path(output_path).resolve()

    with Image.open(input_path) as image:
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        image = image.convert('RGBA')

        width, height = image.size
        data = image.tobytes()
        compressor = compressobj()

        with open(output_path, 'wb') as output:
            output.write(b'BIP1')

            output.write(width.to_bytes(2, 'big'))
            output.write(height.to_bytes(2, 'big'))

            output.write(compressor.compress(data))
            output.write(compressor.flush())


def bip_to_image(input_path: Union[str, Path], output_path: Union[str, Path]):
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
