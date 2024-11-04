from webpages.WebScraper import WebScraper


class CBSSportsTeams:

    def load(self):
        url = 'https://www.cbssports.com/college-basketball/teams/'

        self.webScraper = WebScraper()
        self.webScraper.scrap(url)

        teamsElements = self.webScraper.soup.findAll('span', class_='TeamName')
        teamsElements = list(map(lambda x: x.findChildren("a" , recursive=False)[0].get("href"), teamsElements))
        list(map(lambda x: self.parseTeamHref(x), teamsElements))

    def parseTeamHref(self, href):
        elements = href.split("/")
        teamAbr = elements[3]
        team = elements[4]
        return team

