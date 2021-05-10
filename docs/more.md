# More

## Features

- Drop-in replacement for `bpy.utils.previews`.
- Provides an highly optimized format for loading previews.
- Load arbitrarily sized images, you are not locked with Blender's default of `128x128`.
- Support for lazy and eager loading of previews.
    - Lazy loading is the recommended method of loading previews as it allows the user interface to remain responsive.
    - Eager loading is possible, but not recommended. This is due to the fact that there are factors that are out of the developer's control such as slow systems without SSDs, growing dynamic lists of images, etc.
- Support for fast load of PNG and JPEG previews in case the [Pillow](https://pypi.org/project/Pillow/) library is installed.
- A built-in base class for an operator to install [Pillow](https://pypi.org/project/Pillow/) with a single click.
- Convenience function `load_safe()` which can be called repetively. In case the image is loaded already, it will be retuned instead. This allows you to focus on loading your previews and requires less management code on your end.
- Being a drop-in replacement for `bpy.utils.previews` the library maintains support for the standard Blender loading behaviour of other file types that are not supported.

## Warning

 Our library is powerful but we recommend to use it wisely. Loading images that are unnecessarily large will slow down the user interface and might consume a lot of memory. We recommend using the library to load reasonably sized images depending on the context.

## The Idea

We developed this library while working on an asset manager for Blender. While working on this project, we realized that the resolution of the images provided by the default `bpy.utils.previews` was quite limiting in that we had no control as to image quality/resolution. After some sessions and development, this library came to life. We decided that such knowledge should not be hoarded but rather shared with the Blender community.
