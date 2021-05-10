# To speed up loading, bl_info should always be at the top of the file.
bl_info = {
    'name': '3DN BIP Getting Started',
    'description': 'Getting started with 3D Ninjas BIP library',
    'author': '3D Ninjas',
    'version': (0, 0, 2),
    'blender': (2, 80, 0),
    'location': '3D View > Sidebar',
    'category': 'Development',
}

import bpy
from pathlib import Path
from .t3dn_bip import previews

# Preview collection created in the register function.
collection = None


class T3DN_PT_bip_panel(bpy.types.Panel):
    bl_label = '3DN BIP Getting Started'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = '3D Ninjas'

    def draw(self, context):
        # The layout is part of the panel class.
        layout = self.layout
        # We'll be drawing things on a dynamic grid.
        grid = layout.grid_flow()

        # Get the path to this python file.
        file = Path(__file__).resolve()
        # Get the path to the images folder.
        folder = file.parent / 'images'

        # Loop through the BIP files in the folder.
        for path in folder.glob('*.bip'):
            # Cast the path to string so the preview collection can use it.
            path = str(path)
            # Load a preview for this path, or use a cached one.
            preview = collection.load_safe(path, path, 'IMAGE')

            # When drawing a preview, you'll need its icon_id.
            icon_id = preview.icon_id
            # Scale 13.2 comes out at 256x256 pixels if your UI scale is 1.
            grid.template_icon(icon_value=icon_id, scale=13.2)


def register():
    # Create a preview collection to load 256x256 images.
    global collection
    collection = previews.new(max_size=(256, 256))

    # Register the panel so it shows up in the sidebar.
    bpy.utils.register_class(T3DN_PT_bip_panel)


def unregister():
    # Unregister the panel to free resources and avoid errors.
    bpy.utils.unregister_class(T3DN_PT_bip_panel)

    # Discard all loaded previews and remove the collection.
    previews.remove(collection)
