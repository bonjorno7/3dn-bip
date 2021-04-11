import bpy
from . import previews

enum_items = []


def get_enum_items(self, context: bpy.types.Context):
    return enum_items


class T3DN_OT_bip_example_load_previews(bpy.types.Operator):
    bl_idname = 't3dn.bip_example_load_previews'
    bl_label = 'Load Previews'
    bl_description = 'Load BIP or JPG image previews'
    bl_options = {'REGISTER', 'INTERNAL'}

    type: bpy.props.StringProperty()
    enum: bpy.props.EnumProperty(items=get_enum_items)

    def invoke(self, context: bpy.types.Context, event: bpy.types.Event) -> set:
        paths = previews.folder.joinpath(self.type).glob(f'*.{self.type}')
        previews.collection.clear()
        enum_items.clear()

        for index, path in enumerate(paths):
            preview = previews.collection.load(path.name, str(path), 'IMAGE')
            item = (path.name, path.name, path.name, preview.icon_id, index)
            enum_items.append(item)

        return context.window_manager.invoke_popup(self, width=120)

    def draw(self, context: bpy.types.Context):
        layout = self.layout
        layout.template_icon_view(self, 'enum')

    def execute(self, context: bpy.types.Context) -> set:
        return {'FINISHED'}


classes = (T3DN_OT_bip_example_load_previews,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
