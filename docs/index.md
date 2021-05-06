## Introduction

**Blender Image Preview**, or BIP for short is a [Blender](https://blender.org)
library by 3D Ninjas that allows addon developers to have extra functionality
that comes built into Blender but takes quite some time to set up.

BIP came about as a solution to image previews on an asset manager that we are
currently developing at [3D Ninjas](https://3dninjas.io). While working on this
project, we realized that the resolution of the images provided by the default
`bpy.utils.previews` was quite limiting in that we had no control as to image
quality/resolution. After some sessions and development, BIP came to life. We
decided that such knowledge should not be hoarded but rather shared with the
Blender community.

The library can be used as a direct drag and drop replacement for the inbuilt
`bpy.utils.previews` module, however, it pays off to take a bit of time to look
into the other features that come with the library as they are what make it
stand out.

## Use Cases

-   Quickly load optimized images images that they have control over into
    Blender using a custom format named `.bip`. You can look into how to get
    your images in this format using our standalone `bip converter` detailed in
    this **[Guide](converter.md)**.
-   Loading arbitrarily sized images. By default Blender's standard previews
    come at a resolution of 32px by 32px for icons and 256px by 256px for
    images. With BIP, you have control of the image sizes per collection. For
    example, you can choose to have a hero image previewed at a specific place
    within your addon of 1024px by 1024px, you can then choose to have a more
    optimized collection of images 128px by 128px to use for displaying items in
    a library.
-   Use of Python's [Pillow](https://pypi.org/project/Pillow/) library to
    quickly process images that are out of your control. A use case for this
    would be if your addon allows for users to load their own images, you would
    not have control as to how big they.

## Features

-   Drag and drop replacement for the standard Blender preview library.
-   Use of an optimized format for loading previews
-   Load arbitrarily sized images, bypass Blender's standard 256px by 256px
-   Support for lazy and eager of previews

    -   Lazy loading allows the interface remains responsive, however if you
        have few images that you'd like to have loaded on demand, then eager
        loading would be a better choice.
    -   Eager loading is a feature that comes built into the BIP library, it
        will freeze up the interface for a certain amount of time and load all
        the images on demand, if your images are optimized and a decent size,
        then this will take an extremely short time and may not even be noticed,
        on the other hand, if the images are large, there will be considerable
        wait time and lazy loading is recommended.

-   If BIP is available, this is the best case and is recommended
-   If unavailable, prompt the user to install [`Pillow`](https://pypi.org/project/Pillow/)
-   Load large high quality previews

## Conclusion

Now that we have the formalities covered, feel free to take a look at the
fastest way to **[Getting Started](getting_started.md)** using BIP, see you on
the other side!
