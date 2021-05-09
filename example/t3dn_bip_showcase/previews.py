from pathlib import Path
from .t3dn_bip import previews

folder = None
collection = None
collection_hero = None


def register():
    global folder, collection, collection_hero

    folder = Path(__file__).resolve().parent.joinpath('images')
    collection = previews.new()
    collection_hero = previews.new(max_size=(512, 512))


def unregister():
    global folder, collection, collection_hero

    previews.remove(collection_hero)
    previews.remove(collection)
    folder = None
