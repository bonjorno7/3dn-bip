We have provided an example to help you get acquainted with BIP.

1. You will first have to download the library from pip:
   [https://pypi.org/project/t3dn-bip/](https://pypi.org/project/t3dn-bip/)
1. TODO: Continue writing the steps.

The folder structure of the assumed example is as follows:

```
__init__.py
\t3dn_bip
\images
\images\image0.bip
\images\image1.bip
\images\image2.bip
```

```python
from pathlib import Path
from .t3dn_bip import previews

import bpy

bl_info = {
    "name": "BIP",
    "author": "3D Ninjas",
    "description": "",
    "blender": (2, 83, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "Generic"
}

# This will be used to access the package directory, initialized on registration
folder = None

# An empty dictionary to hold the preview collections
PREVIEW_COLL = {}


class T3DN_PT_bip_panel(bpy.types.Panel):
    bl_label = "BIP Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "3D Ninjas"

    def draw(self, context):

        # NOTE: Step 1 - Add this folder to the project and add a few images.
        images = folder.joinpath('images')

        # NOTE: Step 2 - Replace the image names with the images you added
        # to the folder in the stop above.
        image_names = ('image0.bip', 'image1.bip', 'image2.bip')

        coll = PREVIEW_COLL['images']

        layout = self.layout
        grid = layout.grid_flow()
        row = grid.row(align=True)

        # Load each of the images
        for item in image_names:
            image = str(images.joinpath(item))
            try:
                icon = coll[image]
            except KeyError:
                icon = coll.load(image, image, 'IMAGE')

            row.template_icon(
                icon_value=icon.icon_id,
                scale=13.2,
            )


def register():
    global folder, PREVIEW_COLL

    # Access the package directory
    folder = Path(__file__).resolve().parent

    # Preview collection to store 128 by 128 images
    # NOTE: Step 3 - Try changing the  parameter to both larger and smaller
    # sizes
    size = 256
    PREVIEW_COLL['images'] = previews.new(max_size=(size, size), lazy_load=True)

    bpy.utils.register_class(T3DN_PT_bip_panel)


def unregister():
    global folder, collection, PREVIEW_COLL

    bpy.utils.unregister_class(T3DN_PT_bip_panel)

    # Remove the collections from the `PREVIEW_COLL` dictionary
    for item in PREVIEW_COLL.values():
        previews.remove(item)
    PREVIEW_COLL.clear()
```
