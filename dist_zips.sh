#!/bin/bash

# strict mode
set -euo pipefail
IFS=$'\n\t'
cd "$( dirname "${BASH_SOURCE[0]}" )"

# create zips
DIST_PATH="$(realpath dist_zips)"

generate_zip () {
    pushd "$(dirname "$1")"
    7z a -l "$DIST_PATH/$(basename "$1").zip" "$(basename "$1")"
    popd
}

generate_zip "bip/t3dn_bip"

for example in $(find examples -mindepth 1 -maxdepth 1 -type d);
do
    generate_zip "$example"
done
