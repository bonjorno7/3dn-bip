import bpy
import bpy.utils.previews
from queue import Queue, Empty
from threading import Event, Thread
from time import time
from traceback import print_exc
from multiprocessing import cpu_count
from .utils import load_file, tag_redraw
from . import settings

_pending = 0
_queue_read = Queue()
_queue_emplace = Queue()
_thread_stopsig = None


def _read_thread(thread_index: int, stopsig: Event):
    '''Read image data in the background.'''

    # Run read loop until we are stopped.
    while not stopsig.is_set():
        # Try to get the next item from the read queue. Wait 1s for it.
        try:
            (collection, name, filepath, maxsize,
             abortsig) = _queue_read.get(True, 1)
        except Empty:
            continue

        # Try to load image.
        data = None
        try:
            if not abortsig.is_set():
                data = load_file(filepath, maxsize)
        except:
            print_exc()

        # Queue for emplacement.
        _queue_emplace.put((collection, name, data, abortsig))


def _emplace_timer():
    '''Emplaces pixels into the preview object. Runs on the main thread.'''

    global _pending
    global _thread_stopsig

    # Variables for timer batch management.
    now = time()
    delay = 0.1
    redraw = False

    # Take about 100ms for this batch.
    while time() - now < 0.1:
        # Get next item from emplace queue.
        try:
            (collection, name, data, abortsig) = _queue_emplace.get(block=False)
        except Empty:
            break

        # Bookkeeping.
        _pending -= 1

        # Move data to preview object.
        try:
            if not abortsig.is_set() and name in collection:
                preview = collection[name]
                preview.icon_size = data['icon_size']
                preview.icon_pixels = data['icon_pixels']
                preview.image_size = data['image_size']
                preview.image_pixels = data['image_pixels']
        except:
            print_exc()
        else:
            redraw = True

    # There might be more in the queue. Lets get scheduled soon.
    else:
        delay = 0.01

    # Redraw UI in case we updated preview objects.
    if redraw:
        tag_redraw()

    # If no items are pending, shutdown read thread and emplace timer.
    if not _pending:
        # Stop read thread.
        if _thread_stopsig:
            _thread_stopsig.set()
            _thread_stopsig = None

        # Unregister emplace timer.
        if bpy.app.timers.is_registered(_emplace_timer):
            bpy.app.timers.unregister(_emplace_timer)
        delay = None

    # Schedule next timer call.
    return delay


def load_async(
    collection: bpy.utils.previews.ImagePreviewCollection,
    name: str,
    filepath: str,
    maxsize: int,
    abortsig: Event,
):
    '''Load image asynchronously. Needs to be called on the main thread.'''

    global _pending
    global _thread_stopsig

    # Bookkeeping.
    _pending += 1

    # Queue for reading.
    _queue_read.put((collection, name, filepath, maxsize, abortsig))

    # Start read thread if not running.
    if not _thread_stopsig:
        _thread_stopsig = Event()
        for i in range(max(min(cpu_count(), settings.MAX_THREADS), 1)):
            thread = Thread(target=_read_thread, args=(i, _thread_stopsig))
            thread.start()

    # Register emplace timer if not installed.
    if not bpy.app.timers.is_registered(_emplace_timer):
        bpy.app.timers.register(_emplace_timer, persistent=True)
