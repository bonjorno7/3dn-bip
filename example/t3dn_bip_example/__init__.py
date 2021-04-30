bl_info = {
    'name': 'BIP Example',
    'description': 'Showcase the 3D Ninjas Blender Image Preview library.',
    'author': 'Jorijn de Graaf',
    'version': (1, 2),
    'blender': (2, 80, 0),
    'location': '3D View > Sidebar',
    'category': 'Development',
}

from . import previews, ops, ui

modules = (
    previews,
    ops,
    ui,
)


def register():
    for module in modules:
        module.register()


def unregister():
    for module in reversed(modules):
        module.unregister()
