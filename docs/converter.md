## Requirements

To use the image converter, you will need to get the latest version of pip using
the link below.
[https://pypi.org/project/t3dn-bip-converter]()

## Usage

Once you have the converter, get the absolute path to the image you would like
to convert an image, you have two options for the operation to be tackled:

-   Convert to `.bip`, this is done by passing the path to the original image as
    a single arguement
    ```
    `bash python -m t3dn_bip_converter source_file.png `
    ```
-   Convert to a [`Pillow`](https://pypi.org/project/Pillow/) supported format,
    this is done by passing the path to the original image as the first argument
    and the path to the location of the converted image with it's respective
    extension.
    ```
    python -m t3dn_bip_converter source_file.png destination_file.bip
    ```
