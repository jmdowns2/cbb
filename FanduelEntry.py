


class FanduelEntry:

    def __init__(self):
        self.forwards = None
        self.guards = None
        self.util = None
        self.clear()
        self.data = None
        self.loadTemplate()

    def clear(self):
        self.guards = []
        self.forwards = []
        self.util = []

    def addGuard(self, id):
        self.guards.append(id)

    def addForward(self, id):
        self.forwards.append(id)

    def addUtil(self, id):
        self.util.append(id)

    def addEntry(self):

        if len(self.guards) + len(self.forwards) + len(self.util) != 8:
            raise Exception("Invalid number of players")

        if len(self.guards) > 5:
            raise Exception("Invalid number of guards")

        if len(self.forwards) > 4:
            raise Exception("Invalid number of forwards")

        if len(self.guards) > 4:
            self.util.append(self.guards[0])
            self.guards = self.guards[1:]
        if len(self.forwards) > 3:
            self.util.append(self.forwards[0])
            self.forwards = self.forwards[1:]

        output = self.guards + self.forwards + self.util

        self.data = self.data + ",".join(output) + "\n"

        self.clear()


    def loadTemplate(self):
        with open("./data/template.csv", 'r', encoding='utf-8') as f:
            self.data = f.read()

    def saveFile(self):
        with open("./data/entry.csv", 'w', encoding='utf-8') as f:
            f.write(self.data)
