import bpy
from .t3dn_bip.ops import InstallPillow
from . import previews


class T3DN_OT_bip_example_install_pillow(bpy.types.Operator, InstallPillow):
    bl_idname = 't3dn.bip_example_install_pillow'


class T3DN_OT_bip_example_load_previews(bpy.types.Operator):
    bl_idname = 't3dn.bip_example_load_previews'
    bl_label = 'Load Previews'
    bl_description = 'Load BIP or JPG image previews'
    bl_options = {'REGISTER', 'INTERNAL'}

    type: bpy.props.StringProperty()

    def invoke(self, context: bpy.types.Context, event: bpy.types.Event) -> set:
        paths = previews.folder.joinpath(self.type).glob(f'*.{self.type}')
        previews.collection.clear()

        for path in list(paths)[:96]:
            previews.collection.load(path.name, str(path), 'IMAGE')

        return context.window_manager.invoke_popup(self, width=1700)

    def draw(self, context: bpy.types.Context):
        layout = self.layout
        grid = layout.grid_flow(row_major=True, columns=12)

        for preview in previews.collection.values():
            grid.template_icon(preview.icon_id, scale=6.8)

    def execute(self, context: bpy.types.Context) -> set:
        return {'FINISHED'}


class T3DN_OT_bip_example_load_alpha(bpy.types.Operator):
    bl_idname = 't3dn.bip_example_load_alpha'
    bl_label = 'Load Alpha Previews'
    bl_description = 'Load BIP and PNG with transparency'
    bl_options = {'REGISTER', 'INTERNAL'}

    def invoke(self, context: bpy.types.Context, event: bpy.types.Event) -> set:
        previews.collection.clear()

        bip = str(previews.folder.joinpath('alpha', 'rainbow.bip'))
        png = str(previews.folder.joinpath('alpha', 'rainbow.png'))

        self.bip = previews.collection.load('bip', bip, 'IMAGE')
        self.png = previews.collection.load('png', png, 'IMAGE')

        return context.window_manager.invoke_popup(self, width=300)

    def draw(self, context: bpy.types.Context):
        layout = self.layout
        row = layout.row()

        row.template_icon(self.bip.icon_id, scale=6.8)
        row.template_icon(self.png.icon_id, scale=6.8)

    def execute(self, context: bpy.types.Context) -> set:
        return {'FINISHED'}


class T3DN_OT_bip_example_load_misc(bpy.types.Operator):
    bl_idname = 't3dn.bip_example_load_misc'
    bl_label = 'Load Misc Previews'
    bl_description = 'Load movie, blend, and font previews'
    bl_options = {'REGISTER', 'INTERNAL'}

    def invoke(self, context: bpy.types.Context, event: bpy.types.Event) -> set:
        previews.collection.clear()

        movie = str(previews.folder.joinpath('misc', 'cube.mp4'))
        blend = str(previews.folder.joinpath('misc', 'monkey.blend'))
        font = str(previews.folder.joinpath('misc', 'courier.ttf'))

        self.movie = previews.collection.load('movie', movie, 'MOVIE')
        self.blend = previews.collection.load('blend', blend, 'BLEND')
        self.font = previews.collection.load('font', font, 'FONT')

        return context.window_manager.invoke_popup(self, width=800)

    def draw(self, context: bpy.types.Context):
        layout = self.layout
        row = layout.row()

        row.template_icon(self.movie.icon_id, scale=13.2)
        row.template_icon(self.blend.icon_id, scale=13.2)
        row.template_icon(self.font.icon_id, scale=13.2)

    def execute(self, context: bpy.types.Context) -> set:
        return {'FINISHED'}


classes = (
    T3DN_OT_bip_example_install_pillow,
    T3DN_OT_bip_example_load_previews,
    T3DN_OT_bip_example_load_alpha,
    T3DN_OT_bip_example_load_misc,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
