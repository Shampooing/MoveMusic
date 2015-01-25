MoveMusic
=========

What it does (short):
---------------------

This script is to be launched by your Transmission client, on completion of a
torrent. If the torrent contains music, a symbolic link pointing to the torrent
will be created in a specified folder.

What it does (detailed):
------------------------

Suppose your Transmission client just downloaded a torrent *torrent* in a folder
*downloads*. If there is music in the torrent you downloaded, you want to be
able to access it without having to find it among all your other downloads.
This script does just that : if there are audio files in the folder *torrent*
(ie .flac, .mp3, etc. ; you can change these, see the "What you need to do
section"), _no matter the recursion level_, it will create a symbolink link in a
specified folder *dest*, pointing to *torrent*.

What it requires to work:
-------------------------

- Python (not sure about which version; for python >= 2.6 this shouldn't be a
  concern. Python3 is probably fine too.)
- Transmission (not sure either but any decently recent version should be fine)

What you need to do:
--------------------

The script won't work immediatly, you'll have to edit the file.

First, change the first line so that it contains the path to your python
installation. The default value (/usr/bin/python) might work for you, but to be
sure run **which python** in a terminal, and paste what you get after the "#!".

Second, provide convenient values for the first 3 variables :
  - MUSIC (the extensions you want to find, eg .flac, .mp3, .ogg, etc.)
  - dest (the folder in which you want your symbolic links)
  - LOGFILE (a log file to keep track of what happened while using the script)

Third, configure your transmission client to launch the script on completion of
a torrent. See the Transmission documentation for that.
