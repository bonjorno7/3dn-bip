import bpy
from .install_pillow import T3DN_OT_bip_example_install_pillow
from .load_previews import T3DN_OT_bip_example_load_previews
from .load_alpha import T3DN_OT_bip_example_load_alpha
from .load_misc import T3DN_OT_bip_example_load_misc
from .template_icon_view import T3DN_OT_bip_example_template_icon_view
from .hero_image import T3DN_OT_bip_example_hero_image
from .dummy import T3DN_OT_bip_example_dummy

classes = (
    T3DN_OT_bip_example_install_pillow,
    T3DN_OT_bip_example_load_previews,
    T3DN_OT_bip_example_load_alpha,
    T3DN_OT_bip_example_load_misc,
    T3DN_OT_bip_example_template_icon_view,
    T3DN_OT_bip_example_hero_image,
    T3DN_OT_bip_example_dummy,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
