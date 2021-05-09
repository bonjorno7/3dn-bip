import bpy
from pathlib import Path
from .t3dn_bip import previews

bl_info = {
    'name': '3DN BIP Getting Started',
    'description': 'Getting started with 3D Ninjas BIP library.',
    'author': '3D Ninjas',
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    'location': '3D View > Sidebar',
    'category': 'Development',
}

# Preview collection created in the register function.
collection = None


class T3DN_PT_bip_panel(bpy.types.Panel):
    bl_label = "3DN BIP Getting Started"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "3D Ninjas"

    def draw(self, context):
        grid = self.layout.grid_flow()

        # Loop through the images in the folder and draw them
        images = Path(__file__).resolve().parent.joinpath('images')
        for item in images.glob('*.bip'):
            icon = collection.load_safe(str(item), str(item), 'IMAGE')
            grid.template_icon(icon_value=icon.icon_id, scale=13.2)


def register():
    # Create a preview collection to load 256x256 images
    global collection
    collection = previews.new(max_size=(256, 256))

    bpy.utils.register_class(T3DN_PT_bip_panel)


def unregister():
    bpy.utils.unregister_class(T3DN_PT_bip_panel)

    # Discard all loaded previews and the collection
    previews.remove(collection)
