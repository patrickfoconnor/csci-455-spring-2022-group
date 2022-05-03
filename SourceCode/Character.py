class Character(object):

    def __init__(self, name, HP, skills, attack, defense, loot, expget, flvrtxt):
        # Set name for enemy
        self.name = name
        self.HP = HP
        self.skills = skills
        self.attack = attack
        self.defense = defense
        self.loot = loot
        self.expget = expget
        self.flvrtxt = flvrtxt
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setHP(self, HP):
        self.HP = HP

    def getHP(self):
        return self.HP

    def setLoot(self, loot):
        self.loot = loot

    def getLoot(self):
        return self.loot


class Player(Character):

    def __init__(self):
        super(Player, self).__init__("Player01", 100, "fire", 50, 5, "None", 50, "Im a fucking winner")
        self.positionX = None
        self.positionY = None

    def setPosition(self, positionY, positionX):
        self.positionX = positionX
        self.positionY = positionY

    def getPosition(self):
        return self.positionY, self.positionX


class Easy(Character):

    def __init__(self):
        super(Easy, self).__init__("Bulbasaur", 50, "fire", 15, 5, "A Stick", 50, "Just a dumb bulbasaur")


class Hard(Character):

    def __init__(self):
        super(Hard, self).__init__("Mewtwo", 75, "none", 40, 10, "none", 150, "Are you ready for the boss")
