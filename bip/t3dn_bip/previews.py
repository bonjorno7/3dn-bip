from __future__ import annotations

import bpy
import bpy.utils.previews
from bpy.types import ImagePreview
from multiprocessing.dummy import Pool
from multiprocessing import cpu_count
from threading import Event
from queue import Queue
from traceback import print_exc
from time import time
from typing import ItemsView, Iterator, KeysView, ValuesView
from .utils import support_pillow, can_load, load_file, tag_redraw


class ImagePreviewCollection:
    '''Dictionary-like class of previews.'''

    def __init__(self, max_size: tuple = (128, 128), lazy_load: bool = True):
        '''Create collection and start internal timer.'''
        if not support_pillow():
            print('Pillow is not installed, therefore:')
            print('-   BIP images load without scaling.')

            if lazy_load:
                print('-   Other images load slowly (Blender standard).')
            if lazy_load and max_size != (128, 128):
                print('-   Other images load in 128x128 (Blender standard).')
            elif not lazy_load and max_size != (256, 256):
                print('-   Other images load in 256x256 (Blender standard).')

        self._collection = bpy.utils.previews.new()
        self._max_size = max_size
        self._lazy_load = lazy_load

        self._pool = Pool(processes=cpu_count())
        self._event = None
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
        return self._collection.new(name)

    def new_safe(self, name: str) -> ImagePreview:
        '''Generate a new empty preview or return existing.'''
        if name in self:
            return self[name]

        return self.new(name)

    def load(self, name: str, filepath: str, filetype: str) -> ImagePreview:
        '''Generate a new preview from the given filepath.'''
        if filetype != 'IMAGE':
            return self._collection.load(name, filepath, filetype)

        if not can_load(filepath):
            return self._load_fallback(name, filepath)

        event = self._get_event()
        preview = self._collection.new(name)

        if self._lazy_load:
            self._pool.apply_async(
                func=self._load_file,
                args=(name, filepath, event),
                error_callback=print,
            )
        else:
            self._load_file(name, filepath, event)

        return preview

    def load_safe(
        self,
        name: str,
        filepath: str,
        filetype: str,
    ) -> ImagePreview:
        '''Generate a new preview from the given filepath or return existing.'''
        if name in self:
            return self[name]

        return self.load(name, filepath, filetype)

    def _load_fallback(self, name: str, filepath: str) -> ImagePreview:
        '''Load preview using Blender's standard method.'''
        preview = self._collection.load(name, filepath, 'IMAGE')
        if not self._lazy_load:
            preview.image_size[:]  # Force Blender to load this preview now.
        return preview

    def _load_file(self, name: str, filepath: str, event: Event):
        '''Load image contents from file and queue preview load.'''
        if not self._lazy_load or not event.is_set():
            size, pixels = load_file(filepath, self._max_size)

        if not self._lazy_load:
            self._load_preview(name, size, pixels, event)
        elif not event.is_set():
            self._queue.put((name, size, pixels, event))

    def _timer(self):
        '''Load queued image contents into previews.'''
        now = time()
        redraw = False
        delay = 0.1

        while time() - now < 0.1:
            try:
                args = self._queue.get(block=False)
            except:
                break

            try:
                self._load_preview(*args)
            except:
                print_exc()
            else:
                redraw = True

        else:
            delay = 0.0

        if redraw:
            tag_redraw()

        return delay

    def _load_preview(self, name: str, size: tuple, pixels: list, event: Event):
        '''Load image contents into preview.'''
        if not self._lazy_load or not event.is_set():
            if name in self._collection:
                preview = self._collection[name]
                preview.image_size = size
                preview.image_pixels = pixels

    def clear(self):
        '''Clear all previews.'''
        self._set_event()
        self._collection.clear()

    def close(self):
        '''Close the collection and clear all previews.'''
        self._set_event()
        self._collection.close()

        if bpy.app.timers.is_registered(self._timer):
            bpy.app.timers.unregister(self._timer)

    def _get_event(self) -> Event:
        '''Get the clear event, make one if necesssary.'''
        if self._event is None:
            self._event = Event()

        return self._event

    def _set_event(self):
        '''Set the clear event, then remove the reference.'''
        if self._event is not None:
            self._event.set()
            self._event = None

    def __del__(self):
        '''Called when collection is garbage collected.'''
        self.close()


def new(
    max_size: tuple = (128, 128),
    lazy_load: bool = True,
) -> ImagePreviewCollection:
    '''Return a new preview collection.'''
    return ImagePreviewCollection(max_size, lazy_load)


def remove(collection: ImagePreviewCollection):
    '''Remove the specified preview collection.'''
    collection.close()
