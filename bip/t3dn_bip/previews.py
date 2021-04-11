import bpy
import bpy.utils.previews
from bpy.types import ImagePreview
from multiprocessing.dummy import Pool
from multiprocessing import cpu_count
from queue import Queue
from traceback import print_exc
from typing import ItemsView, Iterator, KeysView, ValuesView
from .load import can_load, load_file


class ImagePreviewCollection:
    '''Dictionary-like class of previews.'''

    def __init__(self):
        '''Create collection and start internal timer.'''
        self._collection = bpy.utils.previews.new()

        self._pool = Pool(processes=cpu_count())
        self._queue = Queue()

        if not bpy.app.timers.is_registered(self._timer):
            bpy.app.timers.register(self._timer)

    def __len__(self) -> int:
        '''Return the amount of previews in the collection.'''
        return len(self._collection)

    def __iter__(self) -> Iterator[str]:
        '''Return an iterator for the names in the collection.'''
        return iter(self._collection)

    def __contains__(self, key) -> bool:
        '''Return whether preview name is in collection.'''
        return key in self._collection

    def __getitem__(self, key) -> ImagePreview:
        '''Return preview with the given name.'''
        return self._collection[key]

    def pop(self, key: str) -> ImagePreview:
        '''Remove preview with the given name and return it.'''
        return self._collection.pop(key)

    def get(self, key: str, default=None) -> ImagePreview:
        '''Return preview with the given name, or default.'''
        return self._collection.get(key, default)

    def keys(self) -> KeysView[str]:
        '''Return preview names.'''
        return self._collection.keys()

    def values(self) -> ValuesView[ImagePreview]:
        '''Return previews.'''
        return self._collection.values()

    def items(self) -> ItemsView[str, ImagePreview]:
        '''Return pairs of name and preview.'''
        return self._collection.items()

    def new(self, name: str) -> ImagePreview:
        '''Generate a new empty preview.'''
        if name in self:
            return self[name]

        return self._collection.new(name)

    def load(self, name: str, filepath: str, filetype: str) -> ImagePreview:
        '''Generate a new preview from the given filepath.'''
        if name in self:
            return self[name]

        if filetype != 'IMAGE' or not can_load(filepath):
            return self._collection.load(name, filepath, filetype)

        preview = self._collection.new(name)

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


def new() -> ImagePreviewCollection:
    '''Return a new preview collection.'''
    return ImagePreviewCollection()


def remove(collection: ImagePreviewCollection):
    '''Remove the specified preview collection.'''
    collection.close()
