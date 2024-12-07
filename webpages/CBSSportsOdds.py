from webpages.WebScraper import WebScraper


class CBSSportsOdds:

    def __init__(self):
        self.gameOdds = None
        url = "https://www.cbssports.com/college-basketball/expert-picks/"
        self.web = WebScraper()
        self.web.scrape(url)

    def load(self):

        rows = self.web.soup.findAll(class_="picks-tr")

        odds = []

        for row in rows:
            try:
                odds.append(self.parseRow(row))
            except:
                print("unable to parse odds")


        self.gameOdds = list(filter(lambda x: x is not None, odds))

    def parseRow(self, row):
        tds = row.findAll(class_="picks-td")
        if len(tds) == 0:
            return None

        teams = tds[0].findAll("span", class_="team")

        if len(teams) != 2:
            raise Exception("Invalid value")

        awayTeam = teams[0].find("a").get("href")
        homeTeam = teams[1].find("a").get("href")

        over = tds[1].find(class_="over").getText()
        over = over.strip()
        if over[0] != "o":
            raise Exception("Bad odds")
        over = float(over[1:])

        odds = tds[1].findAll(class_="game-odds")[1].getText()

        if (odds.strip() == "PK"):
            odds = 0
        else:
            odds = float(odds.strip())

        return {
            "homeTeam": self.parseHref(homeTeam),
            "awayTeam": self.parseHref(awayTeam),
            "over": over,
            "odds": odds
        }

    def parseHref(self, url):
        return url.split("/")[5]

    def predictTeamScore(self, team):

        game = list(filter(lambda x: x['homeTeam'] == team or x['awayTeam'] == team, self.gameOdds))
        if len(game) != 1:
            # raise Exception(f"Could not find oods for team {team}")
            print(f"** UNable to predict team score for {team} **")
            return None

        game = game[0]

        homeTeamScore = (game["over"]/2) - (game["odds"]/2)
        if game["awayTeam"] == team:
            return game["over"] - homeTeamScore
        else:
            return homeTeamScore