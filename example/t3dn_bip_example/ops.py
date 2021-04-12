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


classes = (
    T3DN_OT_bip_example_install_pillow,
    T3DN_OT_bip_example_load_previews,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
