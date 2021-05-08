## About

**Blender Image Preview**, or **BIP** for short is a **[Blender](https://blender.org)**
library by 3D Ninjas that allows addon developers to have extra functionality
that would take quite some time for them to set up on their own. `.bip` is a
format designed to be 100% compatible with the Blender in-memory format of these
objects. It primarily guarantees, that we can just read the data from the file
and copy it without any modifications in the right buffer.

### Origin

BIP came about as a solution to image previews on an asset manager that we are
currently developing at **[3D Ninjas](https://3dninjas.io)**. While working on
this project, we realized that the resolution of the images provided by the
default `bpy.utils.previews` was quite limiting in that we had no control as to
image quality/resolution. After some sessions and development, BIP came to life.
We decided that such knowledge should not be hoarded but rather shared with the
Blender community.

### Ease-Of-Use

The library can be used as a direct drop-in replacement for the Blender's
default `bpy.utils.previews` module, however, it pays off to take a bit of time
to look into the other features that come with the library.

---

## Use Cases

### Controlled Environment

If you create all the images yourself, you can use the highly optimized `.bip`
format to load the images. Converting images to the `.bip` format is covered in
the **[Getting Started](getting_started.md)** guide.

### Images In Any Size

Loading arbitrarily sized images. By default Blender's standard previews
come at a resolution of `32px by 32px` for icons and `128px by 128px` for
images. With BIP, you have control of the image sizes per collection. For
example, you can choose to have a hero image previewed at a specific place
within your addon of `1024px by 1024px`, you can then choose to have a more
optimized collection of images `128px by 128px` to use for displaying items in
a library.

### Fast Image Load and Resize with Pillow

Use of Python's [`Pillow`](https://pypi.org/project/Pillow/) library to
quickly process images that you do not have control over. A use case for this
would be if your addon allows for users to load their own images or from an
external software, you would not have control as to how big they. In such a
case, you should prompt the user to use the built-in operator to install
[`Pillow`](https://pypi.org/project/Pillow/). If it's not installed then the
library will default to Blender's standard preview service.

<!-- TODO: Document the API reference with the call for the install Pillow operator -->

---

## Features

-   Drop-In replacement for the standard Blender preview library
    `(bpy.utils.previews)`.
-   Use of an optimized format for loading previews.
-   Load arbitrarily sized images, you are not locked with Blender's default
    maximum of 256px by 256px.
-   Support for lazy and eager loading of previews.

    -   Lazy loading is the recommended method of loading previews as it allows
        the interface to remain responsive.
    -   Eager loading also comes built into the library but is not recommended,
        this is due to the fact that there are factors that are out of the
        developer's control such as slow systems without SSDs, growing dynamic
        lists of images, etc.

-   Support for loading previews that are out of your control with the use of
    the [`Pillow`](https://pypi.org/project/Pillow/) library. The library comes
    with a built in operator that handles this for the developer.
    <!-- TODO: Document the API reference with the call for the install Pillow operator -->

-   Pre-set safety when loading previews, instead of using the `load()` method,
    you can opt to use the `load_safe()` method. The same is the case for the
    `new()` method. This allows you to focus on loading your previews and less
    on whether you need to provide a safety check.

## Warnings

-   BIP is powerful but it's also wise to practice discretion, loading images
    that are unnecessarily large is not recommended, we recommend using the
    library to load reasonably sized images or single large images depending on
    context.
