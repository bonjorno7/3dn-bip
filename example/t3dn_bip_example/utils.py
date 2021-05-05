import bpy


def get_scale_from_res(resolution: int) -> int:
    '''
    Get a Blender scale value from a given resolution. This only works for a
    `ui_scale` of 1 and greater.

    Args:
        resolution: The resolution to be converted.
    Returns:
        The Blender scale value of the resolution.
    '''

    width = (resolution + 8) / bpy.context.preferences.view.ui_scale
    return width / 20
