#!python
import sqlite3, sys, os, datetime


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def MAIN():
    now = datetime.datetime.now()
    conn = sqlite3.connect(os.path.expanduser('~') + r'/Bookmarks.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS BOOKMARKS
       (ID INTEGER PRIMARY KEY,
        DATE TEXT NOT NULL,
        LOCATION TEXT UNIQUE UNIQUE NOT NULL,
        NAME CHAR(50) UNIQUE
       );
        ''')
    help_file = {
        '-h': 'Display this help',
        '-g': 'Go to the Specified Bookmark \n Syntax: cdb -g [Name of Bookmark]',
        '-a': 'Add the current Location to bookmark \n syntax: cdb -a [Name of Bookmark]',
        '-c': 'Delete all bookmarks',
        '-l': 'List all Bookmarks',
        '-m': 'Modify a Bookmark to current location \n Syntax: cdb -m [Name of Bookmark]'
    }

    option = sys.argv[1]
    if len(sys.argv) > 2:
        data = sys.argv[2]

    if option == '-a':
        if len(sys.argv) < 3: print bcolors.FAIL + "Argument missing type: -h for help" + bcolors.ENDC
        AddBookmark(data, conn, now)
    elif option == '-g':
        if len(sys.argv) < 3: print bcolors.FAIL + "Argument missing type: -h for help" + bcolors.ENDC
        GoToBookmark(data, conn)
    elif option == '-l':
        ListBookmarks(conn)
    elif option == '-c':
        DeleteBookmarks(conn)
    elif option == '-r':
        if len(sys.argv) < 3: print bcolors.FAIL + "Argument missing type: -h for help" + bcolors.ENDC
        RemoveBookmark(conn, data)
    elif option == '-m':
        if len(sys.argv) < 3: print bcolors.FAIL + "Argument missing type: -h for help" + bcolors.ENDC
        ModifyBookmark(conn, data)
    elif option == '-h':
        DisplayHelp(help_file)


def DisplayHelp(help_file):
    print bcolors.HEADER + bcolors.BOLD + " Shell Bookmarker \n Copyright (c) Vignesh@vignesh0025@gmail.com\n December 7th 2015 Version 1.0 \n"
    for Op, Val in help_file.iteritems():
        print "{0} {1}:{2} {3} {4}".format(bcolors.OKBLUE + bcolors.BOLD, Op, bcolors.ENDC + bcolors.OKGREEN, Val,
                                           bcolors.ENDC)


def ModifyBookmark(conn, data):
    if len(GetBookmarkRow(data, conn)) > 0:
        conn.execute('''UPDATE BOOKMARKS SET LOCATION = ? WHERE NAME = ?''', [os.getcwd(), data])
        conn.commit()
        print bcolors.OKGREEN + "{0} points to {1}".format(data, os.getcwd())
    else:
        print bcolors.WARNING + "Bookmark {0} doesn't exist".format(data)


def RemoveBookmark(conn, data):
    if len(GetBookmarkRow(data, conn)) > 0:
        conn.execute('''DELETE FROM BOOKMARKS WHERE NAME = ?''', [data])
        conn.commit()
        print bcolors.OKGREEN + "Bookmark" + bcolors.BOLD + "{0}" + bcolors.ENDC + bcolors.OKGREEN + " is removed".format(
            data)
    else:
        print bcolors.WARNING + "Bookmark {0} doesn't exist".format(data)


def DeleteBookmarks(conn):
    val = str(raw_input(bcolors.WARNING + 'Are you sure want to remove all Bookmarks ? (y/n)' + bcolors.ENDC))
    if val == 'y':
        conn.execute('DROP TABLE BOOKMARKS')
        conn.commit()


def ListBookmarks(conn):
    val = conn.execute('''SELECT * FROM BOOKMARKS''').fetchall()
    if len(val) == 0: print bcolors.WARNING + "No bookmarks exist" + bcolors.ENDC
    for Row in val:
        print bcolors.OKBLUE + Row[3] + bcolors.OKGREEN + ': ' + Row[2] + bcolors.ENDC


def GoToBookmark(Data, conn):
    val = GetBookmarkRow(Data, conn)
    # print "cd "+str(val[0][0])
    if len(val) != 0:
        print "cd " + str(val[0][0])
    else:
        print bcolors.WARNING + "No such Bookmarks present" + bcolors.ENDC


def GetBookmarkRow(Data, conn):
    val = conn.execute('''SELECT LOCATION FROM BOOKMARKS WHERE NAME = ?''', [Data]).fetchall()
    return val


def AddBookmark(Data, conn, now):
    val = GetBookmarkRow(Data, conn)
    if len(val) == 0:
        conn.execute('''INSERT INTO BOOKMARKS(DATE,LOCATION,NAME) VALUES (?,?,?)''',
                     (now.strftime("%Y-%m-%d %H:%M"), os.getcwd(), Data))
    else:
        print bcolors.WARNING + "Bookmark with name {0} already exists.".format(Data) + bcolors.ENDC
    conn.commit()


# try:
MAIN()
# except:
#    print 'Error occured'
