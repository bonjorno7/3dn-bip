import bpy
from .t3dn_bip.ops import InstallPillow
from . import previews


class T3DN_OT_bip_example_install_pillow(bpy.types.Operator, InstallPillow):
    bl_idname = 't3dn.bip_example_install_pillow'


class T3DN_OT_bip_example_load_previews(bpy.types.Operator):
    bl_idname = 't3dn.bip_example_load_previews'
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
        self.paths = [str(path) for path in paths][:96]

        return context.window_manager.invoke_popup(self, width=1700)

    def draw(self, context: bpy.types.Context):
        layout = self.layout
        grid = layout.grid_flow(row_major=True, columns=12)

        for path in self.paths:
            preview = previews.collection.load_safe(path, path, 'IMAGE')
            grid.template_icon(preview.icon_id, scale=6.8)

    def execute(self, context: bpy.types.Context) -> set:
        return {'FINISHED'}


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

        self.bip = previews.collection.load_safe(bip, bip, 'IMAGE')
        self.png = previews.collection.load_safe(png, png, 'IMAGE')

        return context.window_manager.invoke_popup(self, width=300)

    def draw(self, context: bpy.types.Context):
        layout = self.layout

        row = layout.row()
        row.template_icon(self.bip.icon_id, scale=6.8)
        row.template_icon(self.png.icon_id, scale=6.8)

        row = layout.row()
        row.operator('t3dn.bip_example_dummy', icon_value=self.bip.icon_id)
        row.operator('t3dn.bip_example_dummy', icon_value=self.png.icon_id)

    def execute(self, context: bpy.types.Context) -> set:
        return {'FINISHED'}


class T3DN_OT_bip_example_load_misc(bpy.types.Operator):
    bl_idname = 't3dn.bip_example_load_misc'
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

        self.movie = previews.collection.load_safe(movie, movie, 'MOVIE')
        self.blend = previews.collection.load_safe(blend, blend, 'BLEND')
        self.font = previews.collection.load_safe(font, font, 'FONT')

        return context.window_manager.invoke_popup(self, width=800)

    def draw(self, context: bpy.types.Context):
        layout = self.layout
        row = layout.row()

        row.template_icon(self.movie.icon_id, scale=13.2)
        row.template_icon(self.blend.icon_id, scale=13.2)
        row.template_icon(self.font.icon_id, scale=13.2)

    def execute(self, context: bpy.types.Context) -> set:
        return {'FINISHED'}


class T3DN_OT_bip_example_dummy(bpy.types.Operator):
    bl_idname = 't3dn.bip_example_dummy'
    bl_label = 'Dummy Operator'
    bl_description = 'Does nothing'
    bl_options = {'REGISTER', 'INTERNAL'}


classes = (
    T3DN_OT_bip_example_install_pillow,
    T3DN_OT_bip_example_load_previews,
    T3DN_OT_bip_example_load_alpha,
    T3DN_OT_bip_example_load_misc,
    T3DN_OT_bip_example_dummy,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
