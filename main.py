from fanduel import FanDuel
from webpages.CBSSportsTeams import CBSSportsTeams
from webpages.NcaaStats import NcaaStats
import datetime


if __name__ == '__main__':
    fanduel = FanDuel()
    player_data = fanduel.load('./data/players.csv')
    teams = fanduel.getTeams()

    #NcaaStats().load(datetime.datetime(2024, 11, 4))
    CBSSportsTeams().load();



