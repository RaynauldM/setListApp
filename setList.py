import csv_functions as SETLIST
import argparse
import shutil


helpText = "[get] random song and artistname"

SCREENSIZE = shutil.get_terminal_size()
SCREENWIDTH = SCREENSIZE.columns
SCREENHEIGHT = SCREENSIZE.lines
EMPTYSPACE = "\n" * round((SCREENHEIGHT / 2))


# returns string of [songname] by [artist]
def getSong():
    return SETLIST.nameAndArtistString(SETLIST.getRandomSongDict())


parser = argparse.ArgumentParser(
    prog="setList",
    description="Provides random songs from the setlist currently working on.",
    epilog="Awesome!",
)
parser.add_argument("choice", help=helpText, type=str)
args = parser.parse_args()

if args.choice == "get":
    print(EMPTYSPACE, getSong().center(round(SCREENWIDTH)), EMPTYSPACE)
    input("")
