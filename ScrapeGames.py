import argparse
import datetime

from GameRepo import GameRepo
from webpages.CBSSportsBoxScore import CBSSportsBoxScore
from webpages.CBSSportsScoreboard import CBSSportsScoreboard


def parseDate(date):
    scoreBoard = CBSSportsScoreboard(date)
    games = scoreBoard.getScoreCards()
    gameRepo = GameRepo()

    count = 0
    for g in games:
        count = count + 1

        if g == None:
            continue

        url = f"https://www.cbssports.com{g}"

        homeTeamId, awayTeamId = CBSSportsBoxScore.parseTeams(url)
        if gameRepo.exists(date, homeTeamId) and gameRepo.exists(date, awayTeamId):
            print(f"Data already fetched for {homeTeamId} and {awayTeamId} on {date}")
            continue


        print(f"Fetching {g} {count} of {len(games)}")

        boxScore = CBSSportsBoxScore(url)
        homeStats = boxScore.getHomeTeamStats()
        awayStats = boxScore.getAwayTeamStats()

        gameRepo.saveGame(homeStats.tolist(), date, boxScore.homeTeamId)
        gameRepo.saveGame(awayStats.tolist(), date, boxScore.awayTeamId)




if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("--start", help="Start Date (ex 2024-11-4)", type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'))
    parser.add_argument("--end", help="End Date (ex 2024-11-4)", type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'))
    args = parser.parse_args()

    current = args.start

    while current <= args.end:
        parseDate(current)
        current = current + datetime.timedelta(days=1)

