import pulp
import numpy as np

class LinearOptimization:

    def __init__(self):
        self.teams = None
        self.is_f = None
        self.is_g = None
        self.names = None
        self.pts = None
        self.salaries = None
        self.ids = None
        self.positions = None

    def load(self, names, ids, positions, salaries, pts, teams):
        self.names = names
        self.ids = ids
        self.positions = positions
        self.salaries = salaries
        self.pts = pts
        self.is_g = list(map(lambda x: "G" in x, self.positions))
        self.is_f = list(map(lambda x: "F" in x, self.positions))
        self.teams = teams

    def solve(self):
        # Create a problem
        prob = pulp.LpProblem("MyProblem", pulp.LpMaximize)

        prob = pulp.LpProblem("FantasyFootballLineup", pulp.LpMaximize)

        player_vars = [pulp.LpVariable(id, cat='Binary') for id in self.ids]

        # maximize
        prob += pulp.lpSum(self.pts[i]*player_vars[i] for i in range(len(self.pts)))

        prob += pulp.lpSum(player_var for player_var in player_vars) == 8
        prob += pulp.lpSum(self.salaries[i] * player_vars[i] for i in range(len(self.salaries))) <= 50000
        prob += pulp.lpSum(self.is_g[i] * player_vars[i] for i in range(len(self.is_g))) >= 4
        prob += pulp.lpSum(self.is_f[i] * player_vars[i] for i in range(len(self.is_f))) >= 3


        # Solve the problem
        prob.solve()


        # Print the status of the solution
        print("Status:", pulp.LpStatus[prob.status])


        print("******************")
        ndx = 0
        guards = []
        forwards = []
        util = []
        for p in player_vars:
            if p.value() > 0:
                print(f"{p.name} -\t{self.teams[ndx]}\t{self.pts[ndx]}\t\t{self.names[ndx]} {self.positions[ndx]}\t\t{self.salaries[ndx]}")

                if self.positions[ndx] == "G":
                    guards.append(self.ids[ndx])
                elif self.positions[ndx] == "G/F":
                    util.append(self.ids[ndx])
                else:
                    forwards.append(self.ids[ndx])
            ndx = ndx + 1
        print("******************")

        return guards, forwards, util