#!/usr/bin/python

from datetime import datetime
from os.path import isdir
from os import symlink, chdir, listdir, environ

############# YOU HAVE TO CHANGE THESE VARIABLES

MUSIC = [".flac", ".mp3"]               # Put here the extensions you want to find 

dest = "/home/toto/mydestfolder"        # This is the folder in which the symlinks will be created

LOGFILE = "/home/toto/move_music.log"   # The path to your log file (it's a mandatory argument for now, remove all the lines containing "log" in this script if you don't want to use it)

######################################



# Your job is done.


############# Getting environment variables

TR_TORRENT_NAME = environ.get('TR_TORRENT_NAME')
TR_TORRENT_DIR = environ.get('TR_TORRENT_DIR')

######################################

TORRENT_DIR = TR_TORRENT_DIR + "/" 

PATH = TORRENT_DIR

chdir(dest)

####### Log operations

log = open(LOGFILE, 'a')
date = str(datetime.now())
log.write(date + "\n")

#######

def musicin(dir):
    for i in listdir(dir):
        ipath = dir + "/" + i
        if isdir(ipath):
            if musicin(ipath)==True:
                return True
        else:
            for ext in MUSIC:
                if i.endswith(ext)==True:
                    log.write("\tFound a " + ext + " file at " + ipath +"\n")
                    return True
    return False

def main(i):
    ipath = PATH + i
    if isdir(ipath):
        if musicin(ipath)==True:
            log.write("\tCreating symlink from " + ipath + " to " + dest + i)
            symlink(ipath, i)
        else:
            log.write("\tFound no music files in " + ipath + ". Exiting.")
    else:
        log.write("\t" + ipath + " wasn't a directory. Exiting.")
    log.write("\n")


main(TR_TORRENT_NAME)

log.write("\n")
log.close()
