import bpy


class T3DN_OT_bip_showcase_dummy(bpy.types.Operator):
    bl_idname = 't3dn.bip_showcase_dummy'
    bl_label = 'Dummy Operator'
    bl_description = 'Does nothing'
    bl_options = {'REGISTER', 'INTERNAL'}

    def execute(self, context: bpy.types.Context) -> set:
        return {'FINISHED'}
