## Pre-Requisites

To get started, you will either have to:

-   Download the repository and copy the `t3dn_bip` folder within the package
    to a folder within your addon.
-   Download the library from pip, find it's location and copy the `t3dn_bip`
    folder to a folder within your addon.

### Links

-   Github Repository: [https://github.com/3dninjas/3dn-bip]()
-   PIP/PyPI Project: [https://pypi.org/project/t3dn-bip/]()

---

## Example

We have provided an example to help you get acquainted with BIP. In order
for this example to work on your machine, you will need to match the folder
structure below or adjust the code to work for your own example.

<!-- TODO: Find a way to make the three images below accessible to the user -->

```
__init__.py
\t3dn_bip
\images
\images\image0.bip
\images\image1.bip
\images\image2.bip
```

Once you have the structure described above, feel free to copy the code below
into the `__init__.py` file. You can then test this within Blender via one of
the two methods below.

-   Zip the folder and install it as you would any other addon within Blender.
    [We reccomend the use of 7-Zip](https://www.7-zip.org/download.html).
-   Use a symbolic link or junction point from this folder into the addon folder
    within Blender.

Once that is done, you can install and look at the code in action within
Blender, notice the detail available within the provided images in comparison to
what you would have by default with Blender.
If you'd like more examples of the capability of the library, feel free to take
a [look at some examples we have created](examples.md).
And if you'd like to take a look at all the available calls, feel free to take a
[look at the API reference](api_reference.md).

```python
from pathlib import Path
import bpy
import bpy.utils.previews
from .t3dn_bip import previews

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


class T3DN_PT_bip_panel(bpy.types.Panel):
    bl_label = "BIP Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "3D Ninjas"

    def draw(self, context):

        bip = PREVIEW_COLL['images']

        # NOTE: Ensure the .bip images are in the `images' folder.
        images = Path(__file__).resolve().parent.joinpath('images')
        images = images.glob('*.bip')

        layout = self.layout
        grid = layout.grid_flow()

        # Loop through the images in the folder and draw them
        for item in images:
            image = str(item)
            try:
                icon = bip[image]
            except KeyError:
                icon = bip.load(image, image, 'IMAGE')

            grid.template_icon(icon_value=icon.icon_id, scale=13.2)


# Empty dictionary to hold the preview collections
PREVIEW_COLL = {}


def register():
    global FOLDER, PREVIEW_COLL

    # Preview collection to store 256 by 256 images
    PREVIEW_COLL['images'] = previews.new(max_size=(256, 256), lazy_load=True)

    bpy.utils.register_class(T3DN_PT_bip_panel)


def unregister():
    global FOLDER, PREVIEW_COLL

    bpy.utils.unregister_class(T3DN_PT_bip_panel)

    # Remove the collections from the `PREVIEW_COLL` dictionary
    for item in PREVIEW_COLL.values():
        previews.remove(item)
    PREVIEW_COLL.clear()
```
