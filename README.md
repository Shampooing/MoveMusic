MoveMusic
=========

Suppose your Transmission client just downloaded a music torrent TORRENT in your DOWNLOADS folder, and your DOWNLOADS folder is very messy (because you are messy like me). You want to be able to access this music without having to find it among all your other downloads. say through a symbolic link, in a folder SYMLINKS, pointing to this file/folder TORRENT.

Requirements :
  Python (not sure about which version ; for python >= 2.6 this shouldn't be a concern)
  Transmission (not sure either but any decently recent version should be fine)

The script won't work immediatly, you'll have to edit the file and provide convenient values for the first 3 variables :
  - MUSIC (the extensions you want to find, eg .flac, .mp3, .ogg, etc.)
  - dest (the folder in which you want your symbolic links)
  - LOGFILE (a log file to keep track of what happened while using the script)
