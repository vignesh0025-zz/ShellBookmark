#!/usr/bin/env bash

wget -O /usr/local/cdb.py https://raw.githubusercontent.com/vignesh0025/ShellBookmark/master/Scripts/cdb.py
wget -O /usr/local/cdb.sh https://raw.githubusercontent.com/vignesh0025/ShellBookmark/master/Scripts/cdb.sh

chmod +x /usr/local/cdb.py
chmod +x /usr/local/cdb.sh

echo "Add the following line to the end of .bashrc / .zshrc "
echo "source /usr/local/cdb.sh"



