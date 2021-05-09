Get Library via PyPI:

```
python -m pip install t3dn-bip
```

Get Converter via PyPI:

```
python -m pip install t3dn-bip-converter
```

### Links

-   GitHub: [https://github.com/3dninjas/3dn-bip/](https://github.com/3dninjas/3dn-bip/)
-   Library @ PyPI: [https://pypi.org/project/t3dn-bip/](https://pypi.org/project/t3dn-bip/)
-   Converter @ PyPI: [https://pypi.org/project/t3dn-bip-converter/](https://pypi.org/project/t3dn-bip-converter/)

---

## BIP Converter

-   Convert to `.bip`, this is done by passing the path to the original image as
    a single arguement.
    ```
    python -m t3dn_bip_converter source_file.png
    ```
-   Convert to a [`Pillow` supported format](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html),
    this is done by passing the path to the original image as the first argument
    and the path to the location of the converted image with it's respective
    extension.
    ```
    python -m t3dn_bip_converter source_file.png destination_file.bip
    ```

---

## Example

Download the `.zip` from the link below to get the resources referenced in the
example.

- [Getting Started](https://github.com/3dninjas/3dn-bip/releases/latest/download/t3dn_bip_getting_started.zip)
- [Showcase](https://github.com/3dninjas/3dn-bip/releases/latest/download/t3dn_bip_showcase.zip)

If you'd like more examples of the capability of the library, feel free to
[take a look at some examples we have created](examples.md). And if you'd like
to take a look at all the available calls, feel free to
[take a look at the API reference](api_reference.md).

The example draws three images that are of the optimized `.bip` format in a
panel. Notice that the registration is a drop in replacement of the
`bpy.utils.previews` module with an additional argument of `max_size`, one of
the benefits of using the library.
