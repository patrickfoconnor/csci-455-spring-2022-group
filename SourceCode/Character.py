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


class Player(Character):

    def __init__(self):
        super(Player, self).__init__("Player01", 10, "fire", 0, 5, "A Stick", 50, "Just a bush, it cannot attack")

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setHP(self, HP):
        self.HP = HP

    def getHP(self):
        return self.HP


class Easy(Character):

    def __init__(self):
        super(Easy, self).__init__("Bulbasaur", 10, "fire", 0, 5, "A Stick", 50, "Just a bush, it cannot attack")


class Hard(Character):

    def __init__(self):
        super(Hard, self).__init__("Mewtwo", 50, "none", 10, 10, "none", 150, "Cliche RPG enemy")
