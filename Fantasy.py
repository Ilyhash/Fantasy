from random import randint


class Heroes:
    heroes = {}

    def __init__(self, name, number):
        self.name = name
        self.number = number
        Heroes.heroes[self.number] = self


class Knight(Heroes):
    def __init__(self, name, number):
        self.name = name
        self.desc = 'noble warrior'
        self.health = 7
        self.str = 5
        self.agi = 3
        self.int = 1
        super().__init__(name, number)


class Assassin(Heroes):
    def __init__(self, name, number):
        self.name = name
        self.desc = 'silent killer'
        self.health = 5
        self.str = 1
        self.agi = 6
        self.int = 2
        super().__init__(name, number)


class Mage(Heroes):
    def __init__(self, name, number):
        self.name = name
        self.desc = 'wise wizard'
        self.health = 5
        self.str = 1
        self.agi = 2
        self.int = 6
        super().__init__(name, number)


class Hobbit(Heroes):
    def __init__(self, name, number):
        self.name = name
        self.desc = 'half-man'
        self.health = 4
        self.str = 1
        self.agi = 4
        self.int = 1
        super().__init__(name, number)


Arthur = Knight('Arthur', 1)
Arthur.str = 10
Altair = Assassin('Altair', 2)
Gendalf = Mage('Gendalf', 3)
Boromir = Knight('Boromir', 4)
Boromir.health = 0
Frodo = Hobbit('Frodo', 5)


def fighter_choice():
    i = randint(1, len(Heroes.heroes))
    return Heroes.heroes[i]


def fighting():
    fighter1 = fighter_choice()
    fighter2 = fighter_choice()
    while fighter1 == fighter2:
        fighter2 = fighter_choice()
    print('{} the {}'.format(fighter1.name, fighter1.desc))
    print('{} the {}'.format(fighter2.name, fighter2.desc))
    if fighter1.name == 'Frodo' or fighter2.name == 'Frodo':
        c = randint(1, 5)
        if c == 5 and fighter1.name == 'Frodo':
            print('Frodo used the ring and killed {}'.format(fighter2.name))
            return
        elif c == 5 and fighter2.name == 'Frodo':
            print('Frodo used the ring and killed {} \n{}'.format(fighter2.name, fighter2.name))
            return
    while fighter1.health >= 0 and fighter2.health >= 0:
        if fighter1.health == 0 and fighter2.health == 0:
            print('Both are dead')
            break
        elif fighter1.health == 0:
            print('{} is dead.'.format(fighter1.name))
            break
        elif fighter2.health == 0:
            print('{} is dead.'.format(fighter2.name))
            break
        else:
            c = randint(1, 3)
            if c == 1:
                if fighter1.str > fighter2.str:
                    fighter2.health -= 1
                    print('{} gets hit, health is {}'.format(fighter2.name, fighter2.health))
                elif fighter1.str < fighter2.str:
                    fighter1.health -= 1
                    print('{} gets hit, health is {}'.format(fighter1.name, fighter1.health))
                else:
                    fighter1.health -= 1
                    fighter2.health -= 1
                    print("Both get hit, {}'s health is {} and {}'s health is {}".format(fighter1.name, fighter1.health,
                                                                                         fighter2.name,
                                                                                         fighter2.health))
            elif c == 2:
                if fighter1.agi > fighter2.agi:
                    fighter2.health -= 1
                    print('{} gets hit, health is {}'.format(fighter2.name, fighter2.health))
                elif fighter1.agi < fighter2.agi:
                    fighter1.health -= 1
                    print('{} gets hit, health is {}'.format(fighter1.name, fighter1.health))
                else:
                    fighter1.health -= 1
                    fighter2.health -= 1
                    print("Both get hit, {}'s health is {} and {}'s health is {}".format(fighter1.name, fighter1.health,
                                                                                         fighter2.name,
                                                                                         fighter2.health))
            elif c == 3:
                if fighter1.int > fighter2.int:
                    fighter2.health -= 1
                    print('{} gets hit, health is {}'.format(fighter2.name, fighter2.health))
                elif fighter1.int < fighter2.int:
                    fighter1.health -= 1
                    print('{} gets hit, health is {}'.format(fighter1.name, fighter1.health))
                else:
                    fighter1.health -= 1
                    fighter2.health -= 1
                    print("Both get hit, {}'s health is {} and {}'s health is {}".format(fighter1.name, fighter1.health,
                                                                                         fighter2.name,
                                                                                         fighter2.health))


fighting()
