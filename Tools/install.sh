#!/usr/bin/env bash

source $(wget -O - https://gist.githubusercontent.com/vignesh0025/7fda7c4a3416a78d62d1/raw/89a6f9d6378458ec52e24d4a9bc39cf92e6552b5/shell_colors.sh)

wget -O /usr/local/cdb.py https://raw.githubusercontent.com/vignesh0025/ShellBookmark/master/Scripts/cdb.py
wget -O /usr/local/cdb.sh https://raw.githubusercontent.com/vignesh0025/ShellBookmark/master/Scripts/cdb.sh

echo "Add the following line to the end of .bashrc / .zshrc "
echo "$UBLu source /usr/local/cdb.sh"



