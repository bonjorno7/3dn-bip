#!/bin/bash

# strict mode
set -euo pipefail
IFS=$'\n\t'
cd "$( dirname "${BASH_SOURCE[0]}" )"

# install requirements
if [ "${1-}" == "--install-requirements" ];
then
    pip install mkdocs mkdocs-material
fi

# build docs
mkdocs build -c -d build_docs/
