
mappings = [
    {
        'fanduel': 'BAY',
        'cbs': 'BAYLOR'
    },
    {
        'fanduel': 'GONZ',
        'cbs': 'GONZAG'
    },
    {
        'fanduel': 'MEM',
        'cbs': 'MEMP'
    },
    {
        'fanduel': 'MIZZ',
        'cbs': 'MIZZOU'
    },
    {
        'fanduel': 'OSU',
        'cbs': 'OHIOST'
    },
    {
        'fanduel': 'TEX',
        'cbs': 'TEXAS'
    },
    {
        'fanduel': 'TXAM',
        'cbs': 'TEXAM'
    },
    {
        'fanduel': 'UCF',
        'cbs': 'UCF'
    },
    {
        'fanduel': 'UF',
        'cbs': 'FLA'
    },
    {
        'fanduel': 'USF',
        'cbs': 'SFLA'
    },
    {
        'fanduel': 'ARMY',
        'cbs': 'ARMY'
    },
    {
        'fanduel': 'BC',
        'cbs': 'BC'
    },
    {
        'fanduel': 'DUKE',
        'cbs': 'DUKE'
    },
    {
        'fanduel': 'KU',
        'cbs': 'KANSAS'
    },
    {
        'fanduel': 'MASS',
        'cbs': 'UMASS'
    },
    {
        'fanduel': 'UNC',
        'cbs': 'UNC'
    },
    {
        'fanduel': 'VCU',
        'cbs': 'VCU'
    },
    {
        'fanduel': 'WVU',
        'cbs': 'WVU'
    },
    {
        'fanduel': 'ARK',
        'cbs': 'ARK'
    },
    {
        'fanduel': 'AUB',
        'cbs': 'AUBURN'
    },
    {
        'fanduel': 'DAY',
        'cbs': 'DAYTON'
    },
    {
        'fanduel': 'FSU',
        'cbs': 'FSU'
    },
    {
        'fanduel': 'HOU',
        'cbs': 'HOU'
    },
    {
        'fanduel': 'NW',
        'cbs': 'NWEST'
    },
    {
        'fanduel': 'RICE',
        'cbs': 'RICE'
    },

    # {
    #     'fanduel': '',
    #     'cbs': ''
    # },

]


class TeamMappings:

    @staticmethod
    def fanduel_to_cbs(team):

        for mapping in mappings:
            if mapping["fanduel"] == team:
                return mapping["cbs"]

        return None