from webpages.WebScraper import WebScraper
import numpy as np

class CBSSportsBoxScore:

    @staticmethod
    def parseTeams(url):
        game = url.split("/")[6]
        game = game.split("_")[2]
        homeTeamId = game.split("@")[1]
        awayTeamId = game.split("@")[0]

        return homeTeamId, awayTeamId


    def __init__(self, url):
        self.web = WebScraper()
        self.web.scrape(url)

        self.homeTeamId, self.awayTeamId = CBSSportsBoxScore.parseTeams(url)

    def getHomeTeamStats(self):
        home = self.web.soup.find(id="player-stats-home")
        return self.parseStats(home)

    def getAwayTeamStats(self):
        away = self.web.soup.find(id="player-stats-away")
        return self.parseStats(away)

    def parseStats(self, element):
        starterTable = self.parseStatTable(element.find(class_="starters-stats"))
        benchTable = self.parseStatTable(element.find(class_="bench-stats"))

        benchTable = np.delete(benchTable, 0, axis=0)
        combined = np.append(starterTable, benchTable, axis=0)

        totalPts = 0
        ptsNdx = 1
        percentPtsNdx = 15
        for row in combined[1:,:]:
            totalPts = totalPts + int(row[ptsNdx])

        for row in combined[1:,:]:
            row[percentPtsNdx] = int(row[ptsNdx]) / totalPts

        combined[0][0] = "PLAYER"
        return combined


    def parseStatTable(self, element):
        viewableArea = element.find(class_="stats-viewable-area")
        statsTable = viewableArea.find(class_="stats-table")

        headerRow = statsTable.find(class_="header-row")
        dataRows = statsTable.findAll(class_="data-row")

        headers = self.parseTableRow(headerRow, True)
        headers = np.append(headers, "PercentPts")
        matrix = np.array([headers])

        for r in dataRows:
            newRow = self.parseTableRow(r, False)
            newRow = np.append(newRow, "")
            matrix = np.append(matrix, [newRow], axis=0)

        return matrix


    def parseTableRow(self, row, isHeader):

        if isHeader == True:
            playerId = "PlayerID"
        else:
            playerHref = row.find("a", class_="name-truncate").get("href")
            playerId = playerHref.split("/")[5]

        ret = list(map(lambda x:x.getText().replace("-", "0").strip(), row.findAll("td")))
        ret.append(playerId)
        return ret
