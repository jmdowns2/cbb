import numpy as np


class Game:

    headers: None
    stats: None

    @staticmethod
    def fromNpArray(x):
        game = Game()
        game.headers = x[0]
        game.stats = np.delete(x, 0, 0)
        return game


    def getHeaderNdx(self, str):
        return np.where(self.headers == str)[0][0]
