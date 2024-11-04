from webpages.WebScraper import WebScraper


class NcaaStats:

    def load(self, date):

        dateEncoded = date.strftime("%m/%d/%y")
        url = f'https://stats.ncaa.org/season_divisions/18403/livestream_scoreboards?utf8=%E2%9C%93&season_division_id=D-1&game_date={dateEncoded}'
        url = 'https://www.cbssports.com/college-basketball/players/26778914/ansley-almonor/'
        url = 'https://stats.ncaa.org/season_divisions/18403/livestream_scoreboards'
        self.webScraper = WebScraper()
        self.webScraper.scrap(url)



