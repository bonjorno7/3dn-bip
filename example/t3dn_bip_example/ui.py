import bpy


class T3DN_PT_bip_example_panel(bpy.types.Panel):
    bl_idname = 'T3DN_PT_bip_example_panel'
    bl_label = 'BIP Example'
    bl_category = '3D Ninjas'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context: bpy.types.Context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'

        layout.operator(
            't3dn.bip_example_load_previews',
            text='Load BIP Previews',
        ).type = 'bip'

        layout.operator(
            't3dn.bip_example_load_previews',
            text='Load JPG Previews',
        ).type = 'jpg'


classes = (T3DN_PT_bip_example_panel,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
