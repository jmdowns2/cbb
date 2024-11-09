import json
import os
from datetime import datetime
from os import listdir

import numpy as np

from models.Game import Game


class GameRepo:

    def saveGame(self, game, date, team):
        path = self.getGamePath(date, team, True)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(game, f, ensure_ascii=False, indent=2)

    def loadGame(self, date, team):
        path = self.getGamePath(date, team, False)
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return Game.fromNpArray(np.array(data))

    def getGamePath(self, date, team, ensurePath):

        if ensurePath == True:
            self.ensureGamePath(self._gamePath(team))

        return self._gameFile(date, team)

    def _gamePath(self, team):
        return f"./data/games/{team}/"

    def _gameFile(self, date, team):
        dateEncoded = date.strftime("%Y-%m-%d")
        return f"./data/games/{team}/{dateEncoded}.json"

    def ensureGamePath(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def getLastGame(self, team):
        files = listdir(self._gamePath(team))
        files = list(map(lambda x: datetime.strptime(x.replace(".json", ""), "%Y-%m-%d"), files))

        return self.loadGame(files[-1], team)

    def getLastGames(self, team, numGames):
        files = listdir(self._gamePath(team))
        files = list(map(lambda x: datetime.strptime(x.replace(".json", ""), "%Y-%m-%d"), files))

        files.sort()

        games = files[-numGames:]
        return list(map(lambda g: self.loadGame(g, team), games))

    def exists(self, date, team):
        return os.path.exists(self._gameFile(date, team))
