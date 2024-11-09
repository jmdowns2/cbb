import random

from GameRepo import GameRepo
from mappings.PlayerMappings import PlayerMappings
from mappings.TeamMappings import TeamMappings
import numpy as np

from webpages.CBSSportsOdds import CBSSportsOdds


def getHeaderNdx(headers, str):
    return np.where(headers == str)[0][0]


class Predict:

    def __init__(self, fanduel):
        self.fanduel = fanduel
        self.gameRepo = GameRepo()
        self.gameCache = {}
        self.teamScoreCache = {}
        self.LAST_NUM_GAMES = 4
        self.odds = CBSSportsOdds()
        self.odds.load()

        self.requireOdds = True

    def setRequireOdds(self, val):
        self.requireOdds = val

    def predict(self):
        predictions = []

        for row in self.fanduel.data:
            predictions.append(self.predictPlayer(row))

        return predictions

    def predictPlayer(self, row):

        fanduelTeam = row[self.fanduel.getHeaderNdx("Team")]
        stats, headers = self.getStatsForPlayer(fanduelTeam, row[self.fanduel.getHeaderNdx("Id")])
        if len(stats) == 0:
            return 0

        percentPtsNdx = getHeaderNdx(headers, "PercentPts")
        ptsNdx = getHeaderNdx(headers, "PTS")
        stealsNdx = getHeaderNdx(headers, "STL")
        oReboundNdx = getHeaderNdx(headers, "OREB")
        dReboundNdx = getHeaderNdx(headers, "DREB")
        blockNdx = getHeaderNdx(headers, "BLK")
        assistsNdx = getHeaderNdx(headers, "AST")
        turnOverNdx = getHeaderNdx(headers, "TO")

        percentPts = self.getAvgStats(stats, percentPtsNdx)
        expectedTeamScore = self.odds.predictTeamScore(TeamMappings.fanduel_to_cbs(fanduelTeam))

        if expectedTeamScore is None:

            if self.requireOdds:
                raise Exception(f"Unable to find odds for {fanduelTeam}")

            print(f"Unable to find odds for {fanduelTeam}")

            expectedPoints = self.getAvgStats(stats, ptsNdx)
        else:
            expectedPoints = percentPts * expectedTeamScore

        return expectedPoints + 1.2*self.getAvgStats(stats, oReboundNdx) + 1.2*self.getAvgStats(stats, dReboundNdx) + 2*self.getAvgStats(stats, blockNdx) + 2*self.getAvgStats(stats, stealsNdx) + 1.5*self.getAvgStats(stats, assistsNdx) - self.getAvgStats(stats, turnOverNdx)

    def getAvgStats(self, stats, ndx):
        vals = []
        for s in stats:
            vals.append(float(s[ndx]))

        return sum(vals) / len(vals)



    def getStatsForPlayer(self, fanduelTeam, fanduelPlayerId):
        cbsId = PlayerMappings.fanduel_to_cbs(fanduelPlayerId)
        cbsTeam = TeamMappings.fanduel_to_cbs(fanduelTeam)


        games = self.getTeamStats(cbsTeam)
        ret = []
        headers = None
        for game in games:
            for stat in game.stats:
                if stat[game.getHeaderNdx("PlayerID")] == cbsId:
                    ret.append(stat)
                    headers = game.headers

        return ret, headers


    def getTeamStats(self, cbsTeam):
        if cbsTeam in self.gameCache.keys():
            return self.gameCache[cbsTeam]

        ret = self.gameRepo.getLastGames(cbsTeam, self.LAST_NUM_GAMES)

        self.gameCache[cbsTeam] = ret
        return ret
