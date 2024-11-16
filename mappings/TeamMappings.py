
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
    {
        'fanduel': 'FAU',
        'cbs': 'FAU'
    },
    {
        'fanduel': 'JOES',
        'cbs': 'STJOES'
    },
    {
        'fanduel': 'MSU',
        'cbs': 'MICHST'
    },
    {
        'fanduel': 'NOVA',
        'cbs': 'NOVA'
    },
    {
        'fanduel': 'UK',
        'cbs': 'UK'
    },
    {
        'fanduel': 'ALA',
        'cbs': 'BAMA'
    },
    {
        'fanduel': 'ARIZ',
        'cbs': 'ARIZ'
    },
    {
        'fanduel': 'BUT',
        'cbs': 'BUTLER'
    },
    {
        'fanduel': 'MARQ',
        'cbs': 'MARQET'
    },
    {
        'fanduel': 'MD',
        'cbs': 'MD'
    },
    {
        'fanduel': 'MICH',
        'cbs': 'MICH'
    },
    {
        'fanduel': 'PSU',
        'cbs': 'PSU'
    },
    {
        'fanduel': 'PURD',
        'cbs': 'PURDUE'
    },
    {
        'fanduel': 'SMU',
        'cbs': 'SMU'
    },
    {
        'fanduel': 'TCU',
        'cbs': 'TCU'
    },
    {
        'fanduel': 'VT',
        'cbs': 'VATECH'
    },
    {
        'fanduel': 'WIS',
        'cbs': 'WISC'
    },
    {
        'fanduel': 'CSU',
        'cbs': 'COLOST'
    },
    {
        'fanduel': 'GTWN',
        'cbs': 'GTOWN'
    },
    {
        'fanduel': 'IND',
        'cbs': 'IND'
    },
    {
        'fanduel': 'MISS',
        'cbs': 'MISS'
    },
    {
        'fanduel': 'ND',
        'cbs': 'ND'
    },
    {
        'fanduel': 'SCAR',
        'cbs': 'SC'
    },
    {
        'fanduel': 'WAKE',
        'cbs': 'WAKE'
    },
    {
        'fanduel': 'WOFF',
        'cbs': 'WOFF'
    },
    {
        'fanduel': 'XAV',
        'cbs': 'XAVIER'
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