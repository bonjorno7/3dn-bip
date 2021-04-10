from typing import Union
from pathlib import Path
from PIL import Image
from zlib import compressobj


def convert(input_path: Union[str, Path], output_path: Union[str, Path]):
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
