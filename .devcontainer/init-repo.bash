#!/bin/bash
set -e
source /usr/local/share/nvm/nvm.sh
cd slides
nvm install v14.20.0
nvm use v14.20.0
npm clean-install
