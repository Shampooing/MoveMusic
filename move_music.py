#!/usr/bin/python

from path import path
import logging
import os

# ---- Please configure the following for your system
extensions = [".flac", ".mp3"]           # Put here all the extensions you want to match 
dest_dir = "/home/toto/destination_folder"         # This is the folder in which the symlinks will be created
log_file = "/home/toto/logs/move_music.log"   # The path to your log file (empty string for no file)
# ---- You're good to go !


# ---- Getting environment variables
TR_TORRENT_NAME = os.environ.get('TR_TORRENT_NAME')
TR_TORRENT_DIR = os.environ.get('TR_TORRENT_DIR')


source_dir = path(TR_TORRENT_DIR)
dezst_dir = path(dest_dir)

# ---- Log operations
logging.basicConfig(level=logging.INFO,
                    filename=log_file,
                    format='%(asctime)s :: %(levelname)s :: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def music_in_dir(dir):
    # We will search recursively for music files in the given directory.
    for content in dir.listdir():
        # If the content is a directory, we call 'music_in_dir' on it.
        if content.isdir():
            if music_in_dir(content):
                return True
            continue
        # At this point, 'content' is a file, so we check wether it has a wanted extension.
        extension = content.split('.')[-1]
        if extension in extensions:
            logging.info("Found file '{}' with wanted extension '{}' in directory '{}'."
                         .format(content.name, "." + extension, dir))
            return True
    # If we get to this point, then we didn't find any music file :(
    return False


def main(torrent_name):
    torrent_full_path = source_dir / torrent_name
    logging.info("Starting...")
    logging.info("Called for torrent name '{}'.".format(torrent_full_path))
    try:
        # We ignore all torrents that are not directories (who DOES that anyway ?)
        if not torrent_full_path.isdir():
            logging.warning("Torrent '{}' wasn't a directory."
                            .format(torrent_full_path))
            raise SystemExit
        # Now we check for music files in the directory.
        if musicin(ipath):
            logging.info("Creating symlink from '{}' to '{}'.".format(torrent_full_path, dest_dir))
            torrent_full_path.symlink(dest_dir / torrent_name)  
        else:
            logging.info("Found no music files in torrent '{}'.".format(torrent_full_path))
    except SystemExit:
        pass
    except Exception as e:
        logging.exception(e)
    finally:
        logging.info("Exiting.\n")


if __name__ == '__main__':
    main(TR_TORRENT_NAME)

