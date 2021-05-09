import bpy
from ..t3dn_bip.ops import InstallPillow


class T3DN_OT_bip_example_install_pillow(bpy.types.Operator, InstallPillow):
    bl_idname = 't3dn.bip_example_install_pillow'
