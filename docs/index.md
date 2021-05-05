## Introduction

BIP is a [Blender](https://blender.org) library by 3D Ninjas that allows addon
developers to have extra functionality that comes built into Blender but takes
quite some time to set up.
The library allows for the developer to easily and quickly load images that they
have control over into Blender, this is with the use of the `.bip` format, the
developer can easily converter their images to this format using our
[BIP Converter - TODO: fix this](https://3dninjas.io) (Information on how this can be achieved is
available [here - TODO: fix this](https://3dninjas.io)).

Have a look at the **[Getting Started](getting_started.md)** guide, and follow the
steps to test BIP.

## Features

-   Quickly load previews
-   Load arbitrarily sized images, bypass Blender's standard 256px by 256px

-   If BIP is available, this is the best case and is recommended
-   If unavailable, prompt the user to install [`Pillow`](https://pypi.org/project/Pillow/)
-   Load large high quality previews
