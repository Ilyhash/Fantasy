class Heroes:
    heroes = {}

    def __init__(self, name, number):
        self.name = name
        self.number = number
        Heroes.heroes[self.number] = self


class Knight(Heroes):

    def __init__(self, name, number):
        self.name = name
        super().__init__(name, number)
        self.desc = 'the noble warrior'
        self.str = 5
        self.agi = 3
        self.int = 2
        self.health = 35
        self.min_atk = 2
        self.max_atk = 4


class Assassin(Heroes):

    def __init__(self, name, number):
        self.name = name
        super().__init__(name, number)
        self.desc = 'the silent killer'
        self.str = 1
        self.agi = 6
        self.int = 2
        self.health = 25
        self.min_atk = 3
        self.max_atk = 6


class Mage(Heroes):

    def __init__(self, name, number):
        self.name = name
        super().__init__(name, number)
        self.desc = 'the wise wizard'
        self.str = 1
        self.agi = 2
        self.int = 6
        self.health = 20
        self.min_atk = 3
        self.max_atk = 4


class Hobbit(Heroes):

    def __init__(self, name, number):
        self.name = name
        super().__init__(name, number)
        self.desc = 'the half-man'
        self.str = 1
        self.agi = 4
        self.int = 1
        self.health = 20
        self.min_atk = 2
        self.max_atk = 3


Arthur = Knight('Arthur', 1)
Arthur.str = 10
Altair = Assassin('Altair', 2)
Altair.agi += 1
Gendalf = Mage('Gendalf', 3)
Boromir = Knight('Boromir', 4)
Frodo = Hobbit('Frodo', 5)
TheEmperor = Knight('The Emperor', 6)
TheEmperor.desc = 'of mankind'
TheEmperor.health = 100
TheEmperor.min_atk = 7
TheEmperor.max_atk = 11
TheEmperor.int += 1
Horus = Knight('Horus', 7)
Horus.desc = 'the Traitor'
Horus.health = 50
Horus.agi += 1
Hitman = Assassin('Hitman', 8)
Hitman.int += 1
Aqua = Mage('Aqua', 9)
Aqua.desc = 'the useless goddess'
Aqua.str += 3
Aqua.agi += 1
Aqua.int = 1
ChaosKnight = Knight('Chaos knight', 10)
ChaosKnight.desc = 'the random everything'
