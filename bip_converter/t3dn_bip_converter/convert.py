from typing import Union
from pathlib import Path
from PIL import Image
from zlib import compressobj, decompressobj


def _image_to_bip(src: Path, dst: Path):
    '''Convert various image formats to BIP.'''
    with Image.open(src) as image:
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        image = image.convert('RGBA')

        width, height = image.size
        data = image.tobytes()
        compressor = compressobj()

        with open(dst, 'wb') as output:
            output.write(b'BIP1')

            output.write(width.to_bytes(2, 'big'))
            output.write(height.to_bytes(2, 'big'))

            output.write(compressor.compress(data))
            output.write(compressor.flush())


def _bip_to_image(src: Path, dst: Path):
    '''Convert BIP to various image formats.'''
    with open(src, 'rb') as bip:
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
            image.save(dst)
        except OSError:
            image.convert('RGB').save(dst)
