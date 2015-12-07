#!/usr/bin/env bash


wget -O /usr/local/cdb.py https://raw.githubusercontent.com/vignesh0025/ShellBookmark/master/Scripts/cdb.py
wget -O /usr/local/cdb.sh https://raw.githubusercontent.com/vignesh0025/ShellBookmark/master/Scripts/cdb.sh

python -c "print '\033[92m Please read the README.md at \033[4mhttps://github.com/vignesh0025/ShellBookmark\033[0m'"
python -c "print '\033[91m Important: add the following line to ~/.zshrc or  ~/.bashrc or your preferred configuration file '"
python -c "print '\033[95m \033[1m source /usr/local/cdb.sh'"



