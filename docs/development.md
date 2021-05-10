# Development

Use Visual Studio Code together with EditorConfig, Python, YAPF, and Pylint.

## VSC Extensions

Install the following Visual Studio Code extensions:

- editorconfig.editorconfig
- ms-python.python

## Python Packages

Install the following Python packages:

- yapf
- pylint


## Setup Symbolic Links on Windows

This repository uses symbolic links. Please enable support for it on your Windows setup, before cloning this repository.

1. Enable symlinks in Git: `git config --global core.symlinks true`
2. Enable symlink policy:
    1. Run `gpedit.msc`
    2. Computer configuration → Windows Settings → Security Settings → Local Policies → User Rights Assignment
    3. Edit `Create symbolic links` policy and add your Windows user to it
    4. Save and reboot
