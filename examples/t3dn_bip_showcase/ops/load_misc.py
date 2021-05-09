import bpy
from .. import previews


class T3DN_OT_bip_showcase_load_misc(bpy.types.Operator):
    bl_idname = 't3dn.bip_showcase_load_misc'
    bl_label = 'Load Misc Previews'
    bl_description = '.\n'.join((
        'Load movie, blend, and font previews',
        'Shift click to reload previews',
    ))
    bl_options = {'REGISTER', 'INTERNAL'}

    def invoke(self, context: bpy.types.Context, event: bpy.types.Event) -> set:
        if event.shift:
            previews.collection.clear()

        movie = str(previews.folder.joinpath('misc', 'cube.mp4'))
        blend = str(previews.folder.joinpath('misc', 'monkey.blend'))
        font = str(previews.folder.joinpath('misc', 'courier.ttf'))

        self._movie = previews.collection.load_safe(movie, movie, 'MOVIE')
        self._blend = previews.collection.load_safe(blend, blend, 'BLEND')
        self._font = previews.collection.load_safe(font, font, 'FONT')

        return context.window_manager.invoke_popup(self, width=800)

    def draw(self, context: bpy.types.Context):
        row = self.layout.row()

        row.template_icon(self._movie.icon_id, scale=13.2)
        row.template_icon(self._blend.icon_id, scale=13.2)
        row.template_icon(self._font.icon_id, scale=13.2)

    def execute(self, context: bpy.types.Context) -> set:
        return {'FINISHED'}
