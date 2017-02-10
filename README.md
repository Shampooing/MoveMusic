MoveMusic
=========

This script recursively scans a directory for files matching any extension among a given list. If any such files are found, a symbolic link to the directory is created in a _destination directory_.

The default use case consists in calling it on completion of a torrent, with a [Transmission](https://transmissionbt.com/) client. Then, if the folder you just downloaded contains **.flac** files, **.mp3** files, etc. (you can configure these extensions in the script file), a symbolic link will be created to this folder in a given _destination directory_.
As soon as you download a music torrent, you'll be able to access the directory directly from _destination directory_, without the hassle of browsing all your downloaded torrents and manually search for music files.

Requirements
------------

- Python 3+ ;
- the module path.py, that you can install by running **pip install path.py** ;
- Transmission (not sure about which version but anything decently recent
  should be fine).
  
Installation
------------

Just grab the file **move_music.py** and put it somewhere convenient. Configure it (see below), make it executable, configure your transmission client, and enjoy!

Usage
-----

Once you've downloaded the file, change its very first line (**#!/usr/bin/python**)so that it contains the path to your desired python installation. If you don't know it, a good way to find out is to run in a terminal

  $ which python

Then, provide convenient values for the first 3 variables :
- `extensions` : the extensions you want to find. By default these will be .flac, .mp3, .ogg, etc., but you can put whatever you like ;
- `dest_dir` : the _destination folder_, in which the symbolic links should be placed ;
- (_optional_) `log_file` : a log file to keep track of what happened while using the script. Leave it to an empty  string if you don't want it.

Finally, you need to configure your transmission client to launch the script on completion of
a torrent. To do this, edit your transmission-daemon's `settings.json` file, and

- set "script-torrent-done-enabled" to `true`;
- set "script-torrent-done-filename" to the path to the `move_music.py` script;

See the [Transmission documentation](https://github.com/transmission/transmission/wiki/Configuration-Files) for more details.

