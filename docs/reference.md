# Reference

```
new():
    Description:
        Create a new preview collection.

    Arguments:
        max_size (tuple): The maximum preview dimensions to be held by the
            collection. Any images that are greater than this size will be
            resized. The parameter is considered if Pillow is installed. The
            default value is (128, 128).
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
        collection (ImagePreviewCollection): Preview collection to be removed.
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
            Return the specified preview if it already exists in the collection.
            Create it otherwise.

        Arguments:
            name (str): The name (unique id) identifying the preview.

        Returns:
            An object of type ImagePreview.

    load():
        Description:
            Load a new preview from the given filepath.

        Arguments:
            name (str): The name (unique id) identifying the preview.
            filepath (str): The file path to load the preview from.
            filetype ('IMAGE', 'MOVIE', 'BLEND', 'FONT'): The type of the file.

        Returns:
            An object of type ImagePreview.

    load_safe():
        Description:
            Return the specified preview if it already exists in the collection.
            Load the preview from the given file path otherwise.

        Arguments:
            name (str): The name (unique id) identifying the preview.
            filepath (str): The file path to load the preview from.
            filetype ('IMAGE', 'MOVIE', 'BLEND', 'FONT'): The type of the file.

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
            key (str): The name of the preview to be removed and returned.

        Returns:
            An object of type ImagePreview or None.

    get():
        Description:
            Return preview with the given name, or default.

        Arguments:
            key (str): The name of the preview to be returned.
            default (any): A value to be returned if the specified key does not
                exist. The default value is None.

        Returns:
            An object of type ImagePreview or None.

    keys():
        Description:
            Return preview names.

        Returns:
            An iterable of type str.

    values():
        Description:
            Return previews.

        Returns:
            An iterable of type ImagePreview.

    items():
        Description:
            Return pairs of name and preview.

        Returns:
            An iterable of type (str, ImagePreview).
```
