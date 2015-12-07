#READ ME
    
This script adds directory bookmarking abilities to shell.  Simple run the following command to install setup the scripts.

    sh -c "$(wget https://raw.githubusercontent.com/vignesh0025/ShellBookmark/master/Tools/install.sh -O -)"
     
Once done, add the following line to you ~/.bashrc or ~/.zshrc
    
    source /usr/local/cdb.sh

#Syntax

    cdb -a Name_of_bookmark
    
Adds the current location as bookmark with name _Name_of_bookmark_ 

    cdb -g Name_of_bookmark
   
Change the directory to bookmark with name _Name_of_bookmark_

    cdb -m Name_of_bookmark
    
Modify the existing bookmark with name _Name_of_bookmark_ to the current location

    cdb -c 
    
Delete all bookmarks present

    cdb -r Name_of_bookmark
   
Delete the bookmark with name Name_of_bookmark

    cdb -h 
    
Display all options for the function

Feel free to post issues and request features. Pull requests are welcome :)  