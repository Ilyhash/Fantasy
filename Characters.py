class Heroes:
    heroes = {}

    def __init__(self, name, number):
        self.name = name
        self.number = number
        Heroes.heroes[self.number] = self


class Knight(Heroes):
    desc = 'the noble warrior'
    str = 5
    agi = 3
    int = 2
    health = 35
    min_atk = 2
    max_atk = 4

    def __init__(self, name, number):
        self.name = name
        super().__init__(name, number)


class Assassin(Heroes):
    desc = 'the silent killer'
    str = 1
    agi = 6
    int = 2
    health = 25
    min_atk = 3
    max_atk = 6

    def __init__(self, name, number):
        self.name = name
        super().__init__(name, number)


class Mage(Heroes):
    desc = 'the wise wizard'
    str = 1
    agi = 2
    int = 6
    health = 20
    min_atk = 3
    max_atk = 4

    def __init__(self, name, number):
        self.name = name
        super().__init__(name, number)


class Hobbit(Heroes):
    desc = 'the half-man'
    str = 1
    agi = 4
    int = 1
    health = 20
    min_atk = 2
    max_atk = 3

    def __init__(self, name, number):
        self.name = name
        super().__init__(name, number)


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
