import bpy
from .. import previews


class T3DN_OT_bip_example_load_alpha(bpy.types.Operator):
    bl_idname = 't3dn.bip_example_load_alpha'
    bl_label = 'Load Alpha Previews'
    bl_description = '.\n'.join((
        'Load BIP and PNG with transparency',
        'Shift click to reload previews',
    ))
    bl_options = {'REGISTER', 'INTERNAL'}

    def invoke(self, context: bpy.types.Context, event: bpy.types.Event) -> set:
        if event.shift:
            previews.collection.clear()

        bip = str(previews.folder.joinpath('alpha', 'rainbow.bip'))
        png = str(previews.folder.joinpath('alpha', 'rainbow.png'))

        self._bip = previews.collection.load_safe(bip, bip, 'IMAGE')
        self._png = previews.collection.load_safe(png, png, 'IMAGE')

        return context.window_manager.invoke_popup(self, width=300)

    def draw(self, context: bpy.types.Context):
        row = self.layout.row()
        row.template_icon(self._bip.icon_id, scale=6.8)
        row.template_icon(self._png.icon_id, scale=6.8)

        row = self.layout.row()
        row.operator('t3dn.bip_example_dummy', icon_value=self._bip.icon_id)
        row.operator('t3dn.bip_example_dummy', icon_value=self._png.icon_id)

    def execute(self, context: bpy.types.Context) -> set:
        return {'FINISHED'}
