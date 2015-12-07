#!/usr/bin/env bash
#    ShellBookmark
#    Copyright (C) 2015  Vignesh D (vignesh0025@gmail.com)
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

wget -O /usr/local/cdb.py https://raw.githubusercontent.com/vignesh0025/ShellBookmark/master/Scripts/cdb.py
wget -O /usr/local/cdb.sh https://raw.githubusercontent.com/vignesh0025/ShellBookmark/master/Scripts/cdb.sh

python -c "print '\033[92m Please read the README.md at \033[4mhttps://github.com/vignesh0025/ShellBookmark\033[0m'"
python -c "print '\033[91m Important: add the following line to ~/.zshrc or  ~/.bashrc or your preferred configuration file '"
python -c "print '\033[95m \033[1m source /usr/local/cdb.sh'"



