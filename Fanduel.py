from numpy import genfromtxt
import numpy as np
from io import StringIO

from GameRepo import GameRepo
from mappings.PlayerMappings import PlayerMappings
from mappings.TeamMappings import TeamMappings


class FanDuel:

    def __init__(self):
        self.data = None
        self.headers = None

        self.excludedTeams = []

    def setExcludedTeams(self, teams):
        self.excludedTeams = teams

    def load(self, filename):
        self.data = genfromtxt(filename, delimiter=',', dtype='str')
        self.headers = self.data[0]

        self.data = np.delete(self.data, 0, axis=0)

        for excludedTeam in self.excludedTeams:
            self.removeTeam(excludedTeam)

        self.validateTeamMappings()
        self.validatePlayers()
        return self.data

    def removeTeam(self, team):
        teamNdx = self.getHeaderNdx("Team")
        for i in reversed(range(len(self.data))):
            if self.data[i][teamNdx] == team:
                self.data = np.delete(self.data, i, axis=0)


    def getTeams(self):
        col = self.getHeaderNdx("Team")
        return np.unique(self.data[:, [col]])

    def getHeaderNdx(self, str):
        return np.where(self.headers == str)[0][0]

    def validateTeamMappings(self):
        teams = self.getTeams()
        missingTeams = []
        for t in teams:
            if TeamMappings.fanduel_to_cbs(t) is None:
                missingTeams.append(t)

        print("***************************")
        for missingTeam in missingTeams:
            print(f"""{{
    'fanduel': '{missingTeam}',
    'cbs': ''
}},""")
        print("***************************")

        if len(missingTeams) > 0:
            raise Exception("Unknown teams " + ", ".join(missingTeams))


    def validatePlayers(self):

        idCol = self.getHeaderNdx("Id")
        teamCol = self.getHeaderNdx("Team")
        salaryCol = self.getHeaderNdx("Salary")
        injuryCol = self.getHeaderNdx("Injury Indicator")

        missingPlayers = []

        for r in self.data:
            if PlayerMappings.fanduel_to_cbs(r[idCol]) == None and int(r[salaryCol]) > 3000 and r[injuryCol] == "":

                missingPlayers.append(r)
                self.guessCbsPlayer(r)

        if len(missingPlayers) > 0:

            print("*************************************")
            # for missingPlayer in missingPlayers:
            #     print(missingPlayer)
            #     print(GameRepo().getLastGame(TeamMappings.fanduel_to_cbs(missingPlayer[teamCol])).stats)
            print("*************************************")

            raise Exception("Missing players")

    def sanitizeName(self, name):
        name = name.replace(" III", "")
        name = name.replace(" II", "")
        name = name.replace(" Jr.", "")
        return name

    def guessCbsPlayer(self, row):
        team = row[self.getHeaderNdx("Team")]
        lastName = self.sanitizeName(row[self.getHeaderNdx("Last Name")])
        firstName = row[self.getHeaderNdx("First Name")]
        fanduelId = row[self.getHeaderNdx("Id")]

        lastGame = GameRepo().getLastGame(TeamMappings.fanduel_to_cbs(team))
        nameNdx = lastGame.getHeaderNdx("PLAYER")
        playerIdNdx = lastGame.getHeaderNdx("PlayerID")

        for row in lastGame.stats:
            cbsFullName = self.sanitizeName(row[nameNdx])
            cbsName = cbsFullName.split(" ")[-1]
            cbsName = cbsName.replace("0", "-")

            if cbsName == lastName and cbsFullName[0] == firstName[0]:
                print(f"""{{
    'fanduel': '{fanduelId}',\t # {firstName} {lastName} {team}
    'cbs': '{row[playerIdNdx]}'\t\t # {cbsFullName}
}},""")

                shouldAdd = input("Add mapping? Y/N")
                if shouldAdd == "Y" or shouldAdd == "y":
                    PlayerMappings.add(fanduelId, row[playerIdNdx])
                    PlayerMappings.save()

                break

        print(f'''{{
    "fanduel": "{fanduelId}", \t  # {firstName} {lastName} {team}
    "cbs": ""
}},''')

        return None


# Expected columns
# ['Id' 'Position' 'First Name' 'Nickname' 'Last Name' 'FPPG' 'Played', 'Salary' 'Game' 'Team' 'Opponent' 'Injury Indicator' 'Injury Details', 'Tier' '' '' 'Roster Position']

