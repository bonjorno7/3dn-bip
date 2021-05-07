```
new():
    Description:
        Return a new preview collection. Collections can be grouped according to
        function, you can choose tohave a gallery with images that have a
        maximum resolution of 128px by 128px and lazy loading enabled would be
        used in a browser with a large volume of images. On the other hand, you
        may have need for a hero image of 1024px by 1024px, and you'd create a
        separate collection for this.

    Arguments:
        max_size (tuple): The maximum size of previews to be held by the class
            instance. This is only available if Pillow is installed. The default
            value is (128, 128).
        lazy_load (bool): Set whether to use lazy or eager loading. The default
            value is True.

    Returns:
        ImagePreviewCollection
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

    pop():
        Description:
            Remove preview with the given name and return it.

        Arguments:
            key (str): The name of the preview to be fetched, removed, and
                access returned.

        Returns:
            An object of type ImagePreview.

    get():
        Description:
            Return preview with the given name, or default.

        Arguments:
            key (str): The name of the preview to be returned. The default value
            is None.

        Returns:
            An object of type ImagePreview.

    keys():
        Description:
            Return preview names.

        Returns:
            An object of typeKeysView[str].

    values():
        Description:
            Return previews.

        Returns:
            An object of typeValuesView[ImagePreview].

    items():
        Description:
            Return pairs of name and preview.

        Returns:
            An object of one of these two types ItemsView[str, ImagePreview].

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
            Attempt to load a preview from the given filepath, otherwise return
            the specified preview if it already exists in the collection.

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
```
