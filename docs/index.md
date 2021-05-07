## About

**Blender Image Preview**, or BIP for short is a **[Blender](https://blender.org)**
library by 3D Ninjas that allows addon developers to have extra functionality
that comes built into Blender but takes quite some time to set up.

So what exactly is the `.bip` format? The accronym is exactly the same as the
name of the library **Blender Image Preview**. Its a format designed to be 100%
compatible with the Blender in-memory format of these objects. It primarily
guarantees, that we can just read the data from the file and copy it without any
modifications in the right buffer.

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
to look into the other features that come with the library as they are what make
it stand out.

---

## Use Cases

### Controlled Environment

Quickly load optimized images images that they have control over into Blender
using a custom format named `.bip`. How to convert your images to `.bip` is
covered in the **[Getting Started](getting_started.md)** section.

### Arbitrarily Sized Images

Loading arbitrarily sized images. By default Blender's standard previews
come at a resolution of `32px by 32px` for icons and `256px by 256px` for
images. With BIP, you have control of the image sizes per collection. For
example, you can choose to have a hero image previewed at a specific place
within your addon of `1024px by 1024px`, you can then choose to have a more
optimized collection of images `128px by 128px` to use for displaying items in
a library.

### Uncontrolled Environment

Use of Python's [`Pillow`](https://pypi.org/project/Pillow/) library to
quickly process images that you do not have control over. A use case for this
would be if your addon allows for users to load their own images, you would
not have control as to how big they. In such a case, you should prompt the user
to download [`Pillow`](https://pypi.org/project/Pillow/), if this is not done,
then the library will default to Blender's standard preview service.

---

## Features

-   Drop-In replacement for the standard Blender preview library
    `(bpy.utils.previews)`.
-   Use of an optimized format for loading previews.
-   Load arbitrarily sized images, you are not locked with Blender's default
    maximum of 256px by 256px.
-   Support for lazy and eager of previews.

    -   Lazy loading allows the interface remains responsive, however if you
        have few images that you'd like to have loaded on demand, then eager
        loading would be a better choice.
    -   Eager loading is a feature that comes built into the BIP library, it
        will freeze up the interface for a certain amount of time and load all
        the images on demand, if your images are optimized and a decent size,
        then this will take an extremely short time and may not even be noticed,
        on the other hand, if the images are large, there will be considerable
        wait time and lazy loading is recommended.

-   Support for loading previews that are out of your control with the use of
    the [`Pillow`](https://pypi.org/project/Pillow/) library.

-   Pre-set safety when loading previews, instead of using the `load()` method,
    you can opt to use the `load_safe()` method. The same is the case for the
    `new()` method. This allows you to focus on loading your previews and less
    on whether you need to provide a safety check.

## Drawbacks

-   When in need of loading multiple large images, this is prone to being slow,
    the best case use of this library is multiple reasonably sized images or
    single large sized images.

---

## Conclusion

Now that we have the formalities covered, feel free to take a look at the
fastest way to **[Getting Started](getting_started.md)** using BIP, see you on
the other side!
