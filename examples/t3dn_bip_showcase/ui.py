import bpy
from .t3dn_bip.utils import support_pillow


class T3DN_PT_bip_showcase_panel(bpy.types.Panel):
    bl_idname = 'T3DN_PT_bip_showcase_panel'
    bl_label = 'BIP Example'
    bl_category = '3D Ninjas'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context: bpy.types.Context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'
        col = layout.column(align=True)
        col.scale_y = 1.2

        text = 'Update Pillow' if support_pillow() else 'Install Pillow'
        col.operator('t3dn.bip_showcase_install_pillow', text=text)

        col = layout.column(align=True)
        col.scale_y = 1.2

        col.operator(
            't3dn.bip_showcase_load_previews',
            text='Load BIP Previews',
        ).type = 'bip'

        col.operator(
            't3dn.bip_showcase_load_previews',
            text='Load JPG Previews',
        ).type = 'jpg'

        col.operator(
            't3dn.bip_showcase_template_icon_view',
            text='Load BIP Enum Icons',
        ).type = 'bip'

        col.operator(
            't3dn.bip_showcase_template_icon_view',
            text='Load JPG Enum Icons',
        ).type = 'jpg'

        col.operator(
            't3dn.bip_showcase_hero_image',
            text='BIP Hero Image Preview',
        ).type = 'bip'

        col.operator(
            't3dn.bip_showcase_hero_image',
            text='JPG Hero Image Preview',
        ).type = 'jpg'

        col.operator('t3dn.bip_showcase_load_alpha')
        col.operator('t3dn.bip_showcase_load_misc')


classes = (T3DN_PT_bip_showcase_panel,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
