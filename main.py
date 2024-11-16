import argparse
import numpy as np

from Fanduel import FanDuel
from FanduelEntry import FanduelEntry
from LinearOptimization import LinearOptimization
from Predict import Predict


def parse_float(string, default=0.0):
    try:
        return float(string)
    except ValueError:
        return default


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--excludeTeams", help="VCU,ARMY,etc")
    parser.add_argument("--excludePlayers", help="fanduel ids")
    parser.add_argument("--usePlayers", help="fanduel ids")
    parser.add_argument("--requireOdds", help="Error out if unable to retreive odds for a team")
    parser.add_argument("--noise", type=int, help="Add noise to expected points, int")

    args = parser.parse_args()

    fanduel = FanDuel()

    if args.excludeTeams is not None:
        fanduel.setExcludedTeams(args.excludeTeams.split(","))

    excludedPlayers = []
    if args.excludePlayers is not None:
        excludedPlayers = args.excludePlayers.split(",")

    usePlayers = []
    if args.usePlayers is not None:
        usePlayers = args.usePlayers.split(",")

    player_data = fanduel.load('./data/players.csv')

    ids = player_data[:, fanduel.getHeaderNdx("Id")]
    names = player_data[:, fanduel.getHeaderNdx("Last Name")]
    positions = player_data[:, fanduel.getHeaderNdx("Position")]
    salaries = player_data[:, fanduel.getHeaderNdx("Salary")].astype(int)
    teams = player_data[:, fanduel.getHeaderNdx("Team")]

    fppg = list(map(lambda x: parse_float(x), player_data[:, fanduel.getHeaderNdx("FPPG")]))

    predict = Predict(fanduel)
    if args.requireOdds == "False":
        predict.setRequireOdds(False)
    pts = predict.predict()



    entries = FanduelEntry()

    while True:

        ptsToUse = pts

        if args.noise is not None:
            ptsToUse = list(map(lambda x: x + np.random.uniform(-1 * args.noise, args.noise), ptsToUse))

        linearOpt = LinearOptimization()
        linearOpt.load(names, ids, positions, salaries, ptsToUse, teams, excludedPlayers)
        linearOpt.setUsePlayers(usePlayers)
        guards, forwards, util = linearOpt.solve()

        add = input("Add this lineup? Y/N")
        # add = "Y"
        if add == "Y" or add == "y":
            for g in guards:
                entries.addGuard(g)
            for f in forwards:
                entries.addForward(f)
            for u in util:
                entries.addUtil(u)

            entries.addEntry()
        else:
            entries.clear()

        cont = input("Create a new lineup? Y/N")
        if cont != "Y" and cont != "y":
            break

    entries.saveFile()
