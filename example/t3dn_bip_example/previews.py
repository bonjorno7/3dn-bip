from pathlib import Path
from .t3dn_bip import previews

folder = None
collection = None


def register():
    global folder, collection

    folder = Path(__file__).resolve().parent.joinpath('images')
    collection = previews.new()


def unregister():
    global folder, collection

    folder = None
    previews.remove(collection)
