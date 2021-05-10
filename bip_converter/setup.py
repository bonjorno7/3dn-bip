from setuptools import setup, find_packages

with open("../README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='t3dn-bip-converter',
    author="3D Ninjas GmbH",
    author_email="niklas@3dninjas.io",
    description="3DN BIP allows blazingly fast image loads in Blender.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/3dninjas/3dn-bip",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    license="GPLv3",
    packages=find_packages(),
    install_requires=['Pillow'],
)
