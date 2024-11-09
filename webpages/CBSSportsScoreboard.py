from webpages.WebScraper import WebScraper


class CBSSportsScoreboard:

    def __init__(self, date):

        dateEncoded = date.strftime("%Y%m%d")
        url = f"https://www.cbssports.com/college-basketball/scoreboard/ALL/{dateEncoded}/"

        self.web = WebScraper()
        self.web.scrape(url)

    def getScoreCards(self):

        cards = self.web.soup.findAll(class_="single-score-card")

        ret = []

        for c in cards:
            href = self.parseScoreCard(c)
            ret.append(href)

        return ret

    def parseScoreCard(self, card):

        boxScore = card.find("a", text="Box Score")
        if boxScore == None:
            return None
        return boxScore.get("href")
