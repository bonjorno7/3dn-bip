import bpy
from .. import previews


class T3DN_OT_bip_showcase_load_previews(bpy.types.Operator):
    bl_idname = 't3dn.bip_showcase_load_previews'
    bl_label = 'Load Previews'
    bl_description = '.\n'.join((
        'Load BIP or JPG image previews',
        'Shift click to reload previews',
    ))
    bl_options = {'REGISTER', 'INTERNAL'}

    type: bpy.props.StringProperty()

    def invoke(self, context: bpy.types.Context, event: bpy.types.Event) -> set:
        if event.shift:
            previews.collection.clear()

        paths = previews.folder.joinpath(self.type).glob(f'*.{self.type}')
        self._paths = [str(path) for path in paths]

        dlg_width = (context.window.width -
                     100) / context.preferences.view.ui_scale

        return context.window_manager.invoke_popup(self, width=dlg_width)

    def draw(self, context: bpy.types.Context):
        grid = self.layout.grid_flow(row_major=True, columns=12)

        for path in self._paths:
            preview = previews.collection.load_safe(path, path, 'IMAGE')
            grid.template_icon(preview.icon_id, scale=6.8)

    def execute(self, context: bpy.types.Context) -> set:
        return {'FINISHED'}
