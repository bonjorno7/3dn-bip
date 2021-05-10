# Getting Started

## What is 3DN BIP?
*3DN BIP* or *3D Ninjas Blender Image Preview* is a library, which allows blazingly fast image loads in Blender. It operates as an `bpy.utils.previews` drop-in replacement and does all the heavy lifting for you.

The following major use cases are supported by our library:

1. Load images shipped as BIP images. We recommend this approach in case you can generate the images beforehand. In this case, your users don't need to take any action to enjoy the speed boost.
2. Load regular JPEG or PNG images. We recommend this approach in case you need to load images provided by the user or by external software tools. In this case, you should use our prepared `InstallPillow` operator, so that your users can enjoy the speed boost with a simple click.

Notes:

1. Our library will always fallback to `bpy.utils.previews` in case unsupported formats are loaded. For this reason, there is no disadvantage in using this library. In the worst case, the standard mechanism of Blender will then be applied.
2. `.bip` is a highly optimized image format, which can be transferred to Blenders internal data structures immediately. It is always blazingly fast, wheter Pillow is installed or not.

## Examples

Download the following sample addons. You can easily install the ZIP files in Blender via the addon preferences tab.

- Getting Started: https://github.com/3dninjas/3dn-bip/releases/latest/download/t3dn_bip_getting_started.zip
- Showcase: https://github.com/3dninjas/3dn-bip/releases/latest/download/t3dn_bip_showcase.zip

## Library

The latest release of the library can be downloaded here: https://github.com/3dninjas/3dn-bip/releases/latest/download/t3dn_bip.zip

Just extract the zip file and copy the folder into your addon. Take a closer look at the examples given above to learn how to use the library.

In case you want to install the library via [PyPI](https://pypi.org/project/t3dn-bip/), you can use the following command:

```sh
python -m pip install t3dn-bip
```

## Converter

The converter is provided via [PyPI](https://pypi.org/project/t3dn-bip-converter/). Use the following command:

```sh
python -m pip install t3dn-bip-converter
```

So you can convert images of [various formats](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html) into the BIP format. Use the following command:

```sh
python -m t3dn_bip_converter source_file.png destination_file.bip
```

## Showcases

### Show `.bip` and `.jpg` Images in a Panel

<iframe width="560" height="315" src="https://www.youtube.com/embed/WUcGWo9gad4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Show `.bip` and `.jpg` Images in an Enum

<iframe width="560" height="315" src="https://www.youtube.com/embed/H9-hCtpOLoo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Show large `.bip` and `.jpg` Hero Images in a Panel

<iframe width="560" height="315" src="https://www.youtube.com/embed/W_xV93_M1Ak" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Show `.bip` and `.png` Images with an Alpha Channel

<iframe width="560" height="315" src="https://www.youtube.com/embed/60D5l18AYy0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
