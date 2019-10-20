import csv

def filterCSV(filename,startYear,filterPositions):
    players = []

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.next()
        for row in csvreader:
            if int(row[fields.index("End Year")]) >= startYear and row[fields.index("Start Year")] != 2019:
                playerPositions = row[fields.index("Position")].split("-")
                for position in playerPositions:
                    if position in filterPositions:
                        players += [{"Name":row[fields.index("Name")],
                                     "Position":position,
                                     "Start Year":max(startYear,int(row[fields.index("Start Year")])),
                                     "End Year":min(2018,int(row[fields.index("End Year")])),
                                     "Link":row[fields.index("Link")]}]


    return players


def writeCSV(filename,data):
    fields = ["Name","Position","Start Year","End Year","Link"]

    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(data)

print writeCSV("test.csv",filterCSV("data/Player List/archive/allHistoricalPlayers.csv",2003,["QB","RB","TE","WR"]))
