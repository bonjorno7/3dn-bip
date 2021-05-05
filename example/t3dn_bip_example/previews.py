from pathlib import Path
from .t3dn_bip import previews

folder = None
collection = None
PREVIEW_COLL = {}


def register():
    global folder, collection, PREVIEW_COLL

    folder = Path(__file__).resolve().parent.joinpath('images')
    collection = previews.new()

    PREVIEW_COLL['images'] = previews.new(max_size=(128, 128), lazy_load=True)
    PREVIEW_COLL['hero'] = previews.new(max_size=(512, 512), lazy_load=True)


def unregister():
    global folder, collection, PREVIEW_COLL

    for item in PREVIEW_COLL.values():
        previews.remove(item)

    PREVIEW_COLL.clear()

    folder = None
    previews.remove(collection)
