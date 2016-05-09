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
A neat way to do that would be to have all your music torrents regrouped in a
dedicated folder ; the only thing being that in the case of torrents, you often
don't want to move them accross folders (you might still want to share them with
friends or family, and in that case you often need them to remain in the same place).
This script does just that : if there are audio files in the folder *torrent*
(ie .flac, .mp3, etc. ; you can change these, see the "What you need to do
section"), _no matter the recursion level_, it will create a symbolink link in a
specified folder *dest*, pointing to *torrent*. Your torrent never left its place
in your folder *downloads*, but now you can access it directly from *dest*.

What it requires to work:
-------------------------

Update:
------
I probably broke the python2-compliance in the latest commit, and now,
unfortunately, the script relies on _path.py_, which you'll have to install
separately (**pip install path.py** does the trick).
However, I didn't bring any new feature (except a proper logging system),
so if you just want the script to work quickly, I suggest you grab the version
of the previous commit. Now the code is more readable (and a bit less childish).


- Python 3 is recommended and probably required, I didn't check for python2 ;
- the module path.py, that you can install by running **pip install path.py** ;
- Transmission (not sure about which version either but anything decently recent
should be fine).

What you need to do:
--------------------

The script is too simple to work out of the box, you'll have to edit a few lines.

First, change the first line so that it contains the path to your desired python
installation. The default value (/usr/bin/python) might work for you, but if you
installed python in a different place (if you have a custom installation for example),
you will have to change it. A good way to know where is your 'default' python
interpreter is to run **which python** in a terminal, and paste what you get after
the "#!".

Second, provide convenient values for the first 3 variables :
  - 'extensions' : the extensions you want to find, eg .flac, .mp3, .ogg, etc. ;
  - 'dest_dir' : the folder in which you want to place the symbolic links ;
  - 'log_file' : a log file to keep track of what happened while using the script. If you don't want it, you can set it to an empty string.

Third, configure your transmission client to launch the script on completion of
a torrent. Edit your transmission-daemon's settings.json file, and

- set "script-torrent-done-enabled" to true;
- set "script-torrent-done-filename" to the path to the move_music.py script;

See the Transmission documentation for more details.

