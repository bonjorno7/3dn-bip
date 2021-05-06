import bpy
import io
import sys
import site
import subprocess
import importlib.util
from pathlib import Path
from zlib import decompress
from array import array

USER_SITE = site.getusersitepackages()

if USER_SITE not in sys.path:
    sys.path.append(USER_SITE)

try:
    from PIL import Image
except ImportError:
    Image = None


def support_pillow() -> bool:
    '''Check whether Pillow is installed.'''
    return bool(Image)


def install_pillow():
    '''Install Pillow and import the Image module.'''
    command = [sys.executable, '-m', 'ensurepip']
    options = ['--user', '--upgrade', '--default-pip']
    if subprocess.call(args=command + options, timeout=60):
        return

    command = [sys.executable, '-m', 'pip']
    options = ['install', '--user', '--upgrade', 'Pillow']
    if subprocess.call(args=command + options, timeout=60):
        return

    name = 'PIL'
    path = Path(USER_SITE).joinpath(name, '__init__.py')

    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)

    sys.modules[module.__name__] = module
    spec.loader.exec_module(module)

    global Image
    from PIL import Image


def can_load(filepath: str) -> bool:
    '''Return whether an image can be loaded.'''
    with open(filepath, 'rb') as bip:
        if bip.read(4) == b'BIP2':
            return True

    return support_pillow()


def load_file(filepath: str, max_size: tuple) -> dict:
    '''Load image preview data from file.

    Args:
        filepath: The input file path.
        max_size: Scale images above this size down.

    Returns:
        A dictionary with icon_size, icon_pixels, image_size, image_pixels.

    Raises:
        AssertionError: If pixel data type is not 32 bit.
        AssertionError: If pixel count does not match size.
        ValueError: If file is not BIP and Pillow is not installed.
    '''
    with open(filepath, 'rb') as bip:
        if bip.read(4) == b'BIP2':
            count = int.from_bytes(bip.read(1), 'big')
            assert count > 0, 'the file contains no images'

            icon_size = [int.from_bytes(bip.read(2), 'big') for _ in range(2)]
            icon_length = int.from_bytes(bip.read(4), 'big')
            bip.seek(8 * (count - 2), io.SEEK_CUR)
            image_size = [int.from_bytes(bip.read(2), 'big') for _ in range(2)]
            image_length = int.from_bytes(bip.read(4), 'big')

            icon_content = decompress(bip.read(icon_length))
            bip.seek(-image_length, io.SEEK_END)
            image_content = decompress(bip.read(image_length))

            if support_pillow() and _should_resize(image_size, max_size):
                image = Image.frombytes('RGBa', image_size, image_content)
                image = _resize_image(image, max_size)
                image_size = image.size
                image_content = image.tobytes()

            icon_pixels = array('i', icon_content)
            assert icon_pixels.itemsize == 4, 'unexpected bytes per pixel'
            length = icon_size[0] * icon_size[1]
            assert len(icon_pixels) == length, 'unexpected amount of pixels'

            image_pixels = array('i', image_content)
            assert image_pixels.itemsize == 4, 'unexpected bytes per pixel'
            length = image_size[0] * image_size[1]
            assert len(image_pixels) == length, 'unexpected amount of pixels'

            return {
                'icon_size': icon_size,
                'icon_pixels': icon_pixels,
                'image_size': image_size,
                'image_pixels': image_pixels,
            }

    if support_pillow():
        with Image.open(filepath) as image:
            image = image.transpose(Image.FLIP_TOP_BOTTOM)
            image = image.convert('RGBA').convert('RGBa')

            if _should_resize(image.size, max_size):
                image = _resize_image(image, max_size)

            image_pixels = array('i', image.tobytes())
            assert image_pixels.itemsize == 4, 'unexpected bytes per pixel'
            length = image.size[0] * image.size[1]
            assert len(image_pixels) == length, 'unexpected amount of pixels'

            data = {
                'icon_size': image.size,
                'icon_pixels': image_pixels,
                'image_size': image.size,
                'image_pixels': image_pixels,
            }

            if _should_resize(image.size, (32, 32)):
                icon = image.resize(size=(32, 32))

                icon_pixels = array('i', icon.tobytes())
                assert icon_pixels.itemsize == 4, 'unexpected bytes per pixel'
                length = icon.size[0] * icon.size[1]
                assert len(icon_pixels) == length, 'unexpected amount of pixels'

                data['icon_size'] = icon.size
                data['icon_pixels'] = icon_pixels

            return data

    raise ValueError('input is not a supported file format')


def _should_resize(size: tuple, max_size: tuple) -> bool:
    '''Check whether width or height is greater than maximum.'''
    if max_size[0] and size[0] > max_size[0]:
        return True

    if max_size[1] and size[1] > max_size[1]:
        return True

    return False


def _resize_image(image: 'Image.Image', max_size: tuple) -> 'Image.Image':
    '''Resize image to fit inside maximum.'''
    scale = min(
        max_size[0] / image.size[0] if max_size[0] else 1,
        max_size[1] / image.size[1] if max_size[1] else 1,
    )

    size = [int(n * scale) for n in image.size]
    return image.resize(size=size)


def tag_redraw():
    '''Redraw every region in Blender.'''
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            for region in area.regions:
                region.tag_redraw()
