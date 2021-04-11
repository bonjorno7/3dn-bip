import bpy
import bpy.utils.previews
from bpy.types import ImagePreview
from multiprocessing.dummy import Pool
from multiprocessing import cpu_count
from queue import Queue
from traceback import print_exc
from .load import load_file


class ImagePreviewCollection:
    '''Dictionary-like class of previews.'''

    def __init__(self):
        self._collection = bpy.utils.previews.new()

        self._pool = Pool(processes=cpu_count())
        self._queue = Queue()

        if not bpy.app.timers.is_registered(self._timer):
            bpy.app.timers.register(self._timer)

    def __contains__(self, key):
        return key in self._collection

    def __getitem__(self, key):
        return self._collection[key]

    def new(self, name: str) -> ImagePreview:
        '''Generate a new empty preview.'''
        if name in self:
            return self[name]

        preview = self._collection.new(name)
        preview.image_size = (1, 1)
        preview.image_pixels_float = (0, 0, 0, 1)

        return preview

    def load(self, name: str, filepath: str, filetype: str) -> ImagePreview:
        '''Generate a new preview from given file path.'''
        if name in self:
            return self[name]

        if filetype != 'IMAGE':
            return self._collection.load(name, filepath, filetype)

        preview = self.new(name)

        self._pool.apply_async(
            func=self._load_file,
            args=(name, filepath),
            error_callback=print,
        )

        return preview

    def _load_file(self, name: str, filepath: str):
        size, pixels = load_file(filepath)
        self._queue.put((name, size, pixels))

    def _timer(self):
        try:
            args = self._queue.get(block=False)
        except:
            return 0.1

        try:
            self._load_preview(*args)
        except:
            print_exc()

        return 0.0

    def _load_preview(self, name: str, size: tuple, pixels: list):
        preview = self._collection[name]
        preview.image_size = size
        preview.image_pixels = pixels

    def clear(self):
        '''Clear all previews.'''
        self._collection.clear()

    def close(self):
        '''Close the collection and clear all previews.'''
        self._collection.close()

        if bpy.app.timers.is_registered(self._timer):
            bpy.app.timers.unregister(self._timer)


def new():
    '''Return a new preview collection.'''
    return ImagePreviewCollection()


def remove(collection: ImagePreviewCollection):
    '''Remove the specified preview collection.'''
    collection.close()
