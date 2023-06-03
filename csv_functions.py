import csv
import random


dictList = []
dataFile = "D:\zelfcode\python\setListApp\coverList.csv"


with open(dataFile) as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        dictList.append(row)


def getRandomSongDict():
    return random.choice(dictList)


def nameAndArtistString(dict):
    return f"{dict['song']} : {dict['artist']}"


def setString(dict):
    return f"in set {dict['set']}\n"


def gradeString(dict):
    return f"grade: {dict['grade']}\n"


def linksString(dict):
    return f"tab: {dict['tab']}\nbassless: {dict['bassless']}\n"


def wholeString(dict):
    return f"{nameAndArtistString(dict)}{setString(dict)}{gradeString(dict)}{linksString(dict)}"
