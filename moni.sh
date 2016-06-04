#!/bin/bash

# -----------------------------------------------------------------------------
#
# Sets up a monitor on folder "slides" and waits for changes in "index.rst".
# If changed, regenerate the slides.
#
# -----------------------------------------------------------------------------

FOLDER=${1}/slides

which inotifywait > /dev/null || {
    echo "inotifywait not available"; exit 1;
}

echo "Waiting for changes in ${1}"
while true; do
    # read output into an array
    read -a change <<< $(inotifywait -e close_write,moved_to,create ${FOLDER})
    if [[ "${change[2]}" = *".rst"* ]]; then
        (cd ${FOLDER} && clear && fab build_slides)
    fi
done
