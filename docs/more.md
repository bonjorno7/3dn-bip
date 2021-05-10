# More

## Features

- Drop-in replacement for `bpy.utils.previews`.
- Provides a highly optimized format for loading previews.
- Loads arbitrarily sized images. You are not locked with Blender's default of `128x128`.
- Support for lazy and eager loading of previews.
    - Lazy loading is the recommended method of loading previews as it allows the user interface to remain responsive.
    - Eager loading is possible but not recommended. Some factors are out of the developer's control, such as slow systems without SSDs, growing dynamic lists of images, etc.
- Supports a fast load of PNG and JPEG previews if the [Pillow](https://pypi.org/project/Pillow/) library is installed.
- A built-in base class for an operator to install [Pillow](https://pypi.org/project/Pillow/) with a single click.
- Convenience function `load_safe()` which can be called repetitively. In case the image is loaded already, it will be returned instead. It allows you to focus on loading your previews and requires less management code on your end.
- Being a drop-in replacement for `bpy.utils.previews`, the library maintains support for the standard Blender loading behavior of other file types that are not supported.

## Warning

Our library is powerful, but we recommend using it wisely. Loading images that are unnecessarily large will slow down the user interface and consume memory. We recommend using the library to load reasonably sized images depending on the context.

## The Idea

We developed this library while developing an asset manager for Blender. While working on this project, we realized that the resolution of the images provided by the default `bpy.utils.previews` was quite limiting in that we had no control as to image quality/resolution. After some sessions and development, this library came to life. We decided that we should not hoard such knowledge but rather share it with the Blender community.
