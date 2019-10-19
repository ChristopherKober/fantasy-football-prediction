import requests
from urllib2 import urlopen
import time
from bs4 import BeautifulSoup
import csv
from string import ascii_uppercase


def urlToSoup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text,"html.parser")


def parsePage(letter):
    url = "https://www.pro-football-reference.com/players/" + letter + "/"
    soup = urlToSoup(url)
    playersDiv = soup.find(id = "div_players")
    playerPList = playersDiv.find_all("p")

    parsedInfo = []

    for i in range(len(playerPList)):
        playerP = playerPList[i]

        textParts = playerP.text.split(' ')
        yearParts = textParts[-1].split('-')

        name = " ".join(textParts[0:-2])
        position = textParts[-2].strip("(").strip(")")
        startYear = yearParts[0]
        endYear = yearParts[1]

        relativeLink = playerP.a["href"]

        parsedInfo += [{"Name":name,"Position":position,"Start Year":startYear,"End Year":endYear,"Link":relativeLink}]


    return parsedInfo


def getPlayerInfo(file):
    fields = ["Name","Position","Start Year","End Year","Link"]

    with open(file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()

        for letter in ascii_uppercase:
            partialPlayerData = parsePage(letter)
            writer.writerows(partialPlayerData)
            print letter
            time.sleep(5)
