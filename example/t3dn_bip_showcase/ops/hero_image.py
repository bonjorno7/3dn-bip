import bpy
from .. import previews

_HERO_WIDTH = 512


class T3DN_OT_bip_example_hero_image(bpy.types.Operator):
    bl_idname = 't3dn.bip_example_hero_image'
    bl_label = 'Hero Image Preview'
    bl_description = 'Draw a high quality hero image'
    bl_options = {'REGISTER', 'INTERNAL'}

    type: bpy.props.StringProperty()

    def invoke(self, context: bpy.types.Context, event: bpy.types.Event) -> set:
        collection = previews.collection_hero

        if event.shift:
            collection.clear()

        path = previews.folder.joinpath('hero', f'sunset.{self.type}')
        self._icon = collection.load_safe(str(path), str(path), 'IMAGE')

        dlg_width = min(
            context.window.width - 100,
            context.window.height - 200,
            _HERO_WIDTH + 8,
        ) / context.preferences.view.ui_scale

        mouse_x = event.mouse_x
        mouse_y = event.mouse_y
        tmp_x = mouse_x - (_HERO_WIDTH / 2)
        tmp_y = mouse_y + 10

        context.window.cursor_warp(tmp_x, tmp_y)
        try:
            return context.window_manager.invoke_popup(self, width=dlg_width)
        finally:
            context.window.cursor_warp(mouse_x, mouse_y)

    def execute(self, context: bpy.types.Context) -> set:
        return {'FINISHED'}

    def draw(self, context: bpy.types.Context):
        column = self.layout.column()
        icon_width = (_HERO_WIDTH + 8) / context.preferences.view.ui_scale
        column.template_icon(
            icon_value=self._icon.icon_id,
            scale=icon_width / 20,
        )
