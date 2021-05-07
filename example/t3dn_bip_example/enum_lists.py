import bpy
from typing import List, Tuple
from . import previews

# We do this on a global level to bypass the dynamic enum bug
icon_items: List[Tuple[str, str, str]] = []


def temp_icon_example(self, context: bpy.types.Context):
    paths = previews.folder.joinpath(self.type).glob(f'*.{self.type}')
    coll = previews.collection

    icon_items.clear()

    for index, path in enumerate(list(paths)):
        icon = coll.load_safe(str(path), str(path), 'IMAGE')
        icon_items.append((path.name, path.name, '', icon.icon_id, index))

    return icon_items
