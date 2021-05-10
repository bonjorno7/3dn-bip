# Install Pillow

The `BIP` library comes with a base class for an operator for installing
[`Pillow`](https://pypi.org/project/Pillow/).

Import `ops` from the `t3dn_bip` package and ensure your operator inherits from
both `bpy.types.Operator` and `InstallPillow`. You will also need to provide
a unique `bl_idname` for the class. An example of how this can be achieved is as
follows.

```
import bpy
from .t3dn_bip.ops import InstallPillow

class T3DN_OT_bip_install_pillow(bpy.types.Operator, InstallPillow):
    bl_idname = 't3dn.bip_install_pillow'
```
