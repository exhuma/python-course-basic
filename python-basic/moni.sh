#!/bin/bash

# -----------------------------------------------------------------------------
#
# Sets up a monitor on folder "slides" and waits for changes in "index.rst".
# If changed, regenerate the slides.
#
# -----------------------------------------------------------------------------

FOLDER=slides
FILENAME=index.rst

which inotifywait > /dev/null || {
    echo "inotifywait not available"; exit 1;
}

while true; do
    echo "Waiting for changes..."
    # read output into an array
    read -a change <<< $(inotifywait -e close_write,moved_to,create ${FOLDER})
    if [ "${change[2]}" = "${FILENAME}" ]; then
        clear && fab build_slides;
    fi
done
