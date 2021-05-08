## Install Pillow

The `BIP` library comes with a base class for an operator for installing
[`Pillow`](https://pypi.org/project/Pillow/).

Import `ops` from the `t3dn_bip` package and ensure your operator inherits from
both `bpy.types.Operator` and `ops.InstallPillow`. You will also need to provide
a unique `bl_idname` for the class. An example of how this can be achieved is as
follows.

```
class T3DN_OT_bip_install_pillow(bpy.types.Operator, InstallPillow):
    bl_idname = 't3dn.bip_install_pillow'
```

## BIP Reference

```
new():
    Description:
        Return a new preview collection.
        An example of this would be to group the collections according to
        function, you can choose to have a gallery with images that have a
        maximum resolution of 128px by 128px and lazy loading enabled would be
        used in a browser with a large volume of images. On the other hand, you
        may have need for a hero image of 1024px by 1024px, and you'd create a
        separate collection for this.

    Arguments:
        max_size (tuple): The maximum size of previews to be held by the class
            instance, any images that are greater than this size will be resized
            if Pillow is present. The default value is (128, 128).
        lazy_load (bool): Set whether to use lazy or eager loading. The default
            value is True.

    Returns:
        An object of type ImagePreviewCollection.
```

```
remove():
    Description:
        Remove the specified preview collection.

    Arguments:
        collection (ImagePreviewCollection): Preview collection to close.
```

```
class ImagePreviewCollection:

    new():
        Description:
            Generate a new empty preview.

        Arguments:
            name (str): The name (unique id) identifying the preview.

        Returns:
            An object of type ImagePreview.

    new_safe():
        Description:
            Attempt to create a new empty preview, otherwise return the
            specified preview if it already exists in the collection.

        Arguments:
            name (str): The name (unique id) identifying the preview.

        Returns:
            An object of type ImagePreview.

    load():
        Description:
            Generate a new preview from the given filepath.

        Arguments:
            name (str): The name (unique id) identifying the preview.
            filepath (str): The file path to generate the preview from.
            filetype (str): The type of file, needed to generate the preview in
            [‘IMAGE’, ‘MOVIE’, ‘BLEND’, ‘FONT’].

        Returns:
            An object of type ImagePreview.

    load_safe():
        Description:
            Return the specified preview if it already exists in the collection,
            otherwise attempt to load a preview from the given filepath.

        Arguments:
            name (str): The name (unique id) identifying the preview.
            filepath (str): The file path to generate the preview from.
            filetype (str): The type of file, needed to generate the preview in
            [‘IMAGE’, ‘MOVIE’, ‘BLEND’, ‘FONT’].

        Returns:
            An object of type ImagePreview.

    clear():
        Description:
            Clear all previews.

    close():
        Description:
            Close the collection and clear all previews.

    pop():
        Description:
            Remove preview with the given name and return it.

        Arguments:
            key (str): The name of the preview to be fetched, removed, and
                access returned.
            default

        Returns:
            An object of type ImagePreview.

    get():
        Description:
            Return preview with the given name, or default.

        Arguments:
            key (str): The name of the preview to be returned.
            default: A value to return if the specified key does not exist. The
            default value is None.

        Returns:
            An object of type ImagePreview.

    keys():
        Description:
            Return preview names.

        Returns:
            An object of type KeysView[str].

    values():
        Description:
            Return previews.

        Returns:
            An object of type ValuesView[ImagePreview].

    items():
        Description:
            Return pairs of name and preview.

        Returns:
            An object of one of these two types ItemsView[str, ImagePreview].
```
