import bpy
from typing import List, Tuple
from .. import previews

# We do this on a global level to bypass the dynamic enum bug.
_icons: List[Tuple[str, str, str, int, int]] = []


def _get_icon_list(self, context: bpy.types.Context):
    _icons.clear()

    paths = previews.folder.joinpath(self.type).glob(f'*.{self.type}')

    for index, path in enumerate(list(paths)):
        icon = previews.collection.load_safe(str(path), str(path), 'IMAGE')
        _icons.append((path.name, path.name, '', icon.icon_id, index))

    return _icons


class T3DN_OT_bip_example_template_icon_view(bpy.types.Operator):
    bl_idname = 't3dn.bip_example_template_icon_view'
    bl_label = 'Template Icon View'
    bl_description = 'Load and use images with the `template_icon_view` construct'
    bl_options = {'REGISTER', 'INTERNAL'}

    type: bpy.props.StringProperty()
    icons: bpy.props.EnumProperty(items=_get_icon_list)

    def invoke(self, context: bpy.types.Context, event: bpy.types.Event) -> set:
        if event.shift:
            previews.collection.clear()

        return context.window_manager.invoke_popup(self, width=120)

    def execute(self, context: bpy.types.Context) -> set:
        return {'FINISHED'}

    def draw(self, context: bpy.types.Context):
        col = self.layout.column(align=True)
        col.label(text='Click to Expand')
        col.template_icon_view(self, 'icons')
