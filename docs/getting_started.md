Get Library via PyPI:

```
python -m pip install t3dn-bip
```

Get Converter via PyPI:

```
python -m pip install t3dn-bip-converter
```

### Links

-   GitHub: [https://github.com/3dninjas/3dn-bip/](https://github.com/3dninjas/3dn-bip/)
-   Library @ PyPI: [https://pypi.org/project/t3dn-bip/](https://pypi.org/project/t3dn-bip/)
-   Converter @ PyPI: [https://pypi.org/project/t3dn-bip-converter/](https://pypi.org/project/t3dn-bip-converter/)

---

## BIP Converter

-   Convert to `.bip`, this is done by passing the path to the original image as
    a single arguement.
    ```
    python -m t3dn_bip_converter source_file.png
    ```
-   Convert to a [`Pillow` supported format](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html),
    this is done by passing the path to the original image as the first argument
    and the path to the location of the converted image with it's respective
    extension.
    ```
    python -m t3dn_bip_converter source_file.png destination_file.bip
    ```

---

## Example

Download the `.zip` from the link below to get the resources referenced in the
example.

-   [BIP Getting Started](_resources\BIP.zip)

The structure within the unziped folder is as follows.

```
__init__.py
\t3dn_bip
\images
\images\image0.bip
\images\image1.bip
\images\image2.bip
```

If you'd like more examples of the capability of the library, feel free to
[take a look at some examples we have created](examples.md). And if you'd like
to take a look at all the available calls, feel free to
[take a look at the API reference](api_reference.md).

The example draws three images that are of the optimized `.bip` format in a
panel. Notice that the registration is a drop in replacement of the
`bpy.utils.previews` module with an additional argument of `max_size`, one of
the benefits of using the library.

```python
import bpy
from pathlib import Path
from .t3dn_bip import previews

bl_info = {
    "name": "BIP",
    "author": "3D Ninjas",
    "blender": (2, 83, 0),
    "version": (0, 0, 1),
}


class T3DN_PT_bip_panel(bpy.types.Panel):
    bl_label = "BIP Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "3D Ninjas"

    def draw(self, context):
        layout = self.layout
        grid = layout.grid_flow()

        # Loop through the images in the folder and draw them
        images = Path(__file__).resolve().parent.joinpath('images')
        for item in images.glob('*.bip'):
            icon = BIP.load_safe(str(item), str(item), 'IMAGE')
            grid.template_icon(icon_value=icon.icon_id, scale=13.2)


# Empty variable to hold the preview collections
BIP = None


def register():
    # Create a preview collection to store 256 by 256 images
    global BIP
    BIP = previews.new(max_size=(256, 256))

    bpy.utils.register_class(T3DN_PT_bip_panel)


def unregister():
    bpy.utils.unregister_class(T3DN_PT_bip_panel)

    # Close the preview collection
    global BIP
    previews.remove(BIP)
```
