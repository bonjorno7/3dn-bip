from typing import Union
from pathlib import Path
from PIL import Image
from zlib import compress, decompress


def convert_file(src: Union[str, Path], dst: Union[str, Path] = None):
    '''Convert between BIP and various image formats.'''
    src = Path(src).resolve()
    src_bip = src.suffix.lower() == '.bip'

    if dst is not None:
        dst = Path(dst).resolve()
        dst_bip = dst.suffix.lower() == '.bip'
    else:
        dst = src.with_suffix('.png' if src_bip else '.bip')
        dst_bip = not src_bip

    if not src_bip and dst_bip:
        _image_to_bip(src, dst)
    elif src_bip and not dst_bip:
        _bip_to_image(src, dst)
    else:
        raise ValueError('exactly one file must be in BIP format')


def _image_to_bip(src: Path, dst: Path):
    '''Convert various image formats to BIP.'''
    with Image.open(src) as image:
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        image = image.convert('RGBA')

        width, height = image.size
        data = image.tobytes()

        with open(dst, 'wb') as output:
            output.write(b'BIP1')

            output.write(width.to_bytes(2, 'big'))
            output.write(height.to_bytes(2, 'big'))

            output.write(compress(data))


def _bip_to_image(src: Path, dst: Path):
    '''Convert BIP to various image formats.'''
    with open(src, 'rb') as bip:
        magic = bip.read(4)

        if magic != b'BIP1':
            raise ValueError('input is not a supported file format')

        width = int.from_bytes(bip.read(2), 'big')
        height = int.from_bytes(bip.read(2), 'big')

        data = decompress(bip.read())

        image = Image.frombytes('RGBA', (width, height), data)
        image = image.transpose(Image.FLIP_TOP_BOTTOM)

        try:
            image.save(dst)
        except OSError:
            image.convert('RGB').save(dst)
