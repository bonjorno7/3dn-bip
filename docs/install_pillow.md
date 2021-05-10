# Install Pillow

Our library provides an operator base class offering a fully integrated installation process for [Pillow](https://pypi.org/project/Pillow/).

Inherit `t3dn_bip.ops.InstallPillow` next to `bpy.types.Operator` and set a unique `bl_idname`. Here is an example:

```py
import bpy
from .t3dn_bip.ops import InstallPillow

class MyInstallPillowOperator(bpy.types.Operator, InstallPillow):
    bl_idname = 'my.install_pillow_unique'
```
