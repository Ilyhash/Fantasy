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
        self.health = 35
        self.atk = 2
        self.str = 5
        self.agi = 3
        self.int = 1
        super().__init__(name, number)


class Assassin(Heroes):
    def __init__(self, name, number):
        self.name = name
        self.desc = 'silent killer'
        self.health = 25
        self.atk = 4
        self.str = 1
        self.agi = 6
        self.int = 2
        super().__init__(name, number)


class Mage(Heroes):
    def __init__(self, name, number):
        self.name = name
        self.desc = 'wise wizard'
        self.health = 20
        self.atk = 3
        self.str = 1
        self.agi = 2
        self.int = 6
        super().__init__(name, number)


class Hobbit(Heroes):
    def __init__(self, name, number):
        self.name = name
        self.desc = 'half-man'
        self.health = 20
        self.atk = 2
        self.str = 1
        self.agi = 4
        self.int = 1
        super().__init__(name, number)


Arthur = Knight('Arthur', 1)
Arthur.str = 10
Altair = Assassin('Altair', 2)
Gendalf = Mage('Gendalf', 3)
Boromir = Knight('Boromir', 4)
Frodo = Hobbit('Frodo', 5)
TheEmperorOfMankind = Knight('The Emperor', 6)
TheEmperorOfMankind.desc = 'of mankind'
TheEmperorOfMankind.health = 100
TheEmperorOfMankind.atk = 10
TheEmperorOfMankind.int += 1
Horus = Knight('Horus', 7)
Horus.desc = 'the Traitor'
Horus.health = 50
Horus.agi += 1


def fighter_choice():
    i = randint(1, len(Heroes.heroes))
    return Heroes.heroes[i]


def special_case(first, second):
    if first == 'Frodo' or second == 'Frodo':
        c = randint(1, 5)
        if c == 5 and first == 'Frodo':
            print('Frodo used the ring and killed {} \n{} is dead'.format(second, second))
            return
        elif c == 5 and second == 'Frodo':
            print('Frodo used the ring and killed {} \n{} is dead'.format(first, first))
            return
    if first == 'Horus' and second == 'The Emperor' or first == 'The Emperor' and second == 'Horus':
        Horus.atk = 25
    if first == 'Boromir' or second == 'Boromir':
        Boromir.health = 0
        print('{} is dead'.format(Boromir.name))


def death_confirm(fighter1, fighter2):
    while fighter1.health <= 0 or fighter2.health <= 0:
        if fighter1.health <= 0 and fighter2.health <= 0:
            print('Both are dead')
        elif fighter1.health <= 0:
            print('{} is dead.'.format(fighter1.name))
        elif fighter2.health <= 0:
            print('{} is dead.'.format(fighter2.name))
        break


def fighting():
    fighter1 = fighter_choice()
    fighter2 = fighter_choice()
    while fighter1 == fighter2:
        fighter2 = fighter_choice()
    print('{} the {}'.format(fighter1.name, fighter1.desc))
    print('{} the {}'.format(fighter2.name, fighter2.desc))
    special_case(fighter1.name, fighter2.name)
    while fighter1.health > 0 and fighter2.health > 0:
        c = randint(1, 3)
        if c == 1:
            if fighter1.str > fighter2.str:
                fighter2.health -= fighter1.atk
                print('{} gets hit for {} dmg, health is {}'.format(fighter2.name, fighter1.atk, fighter2.health))
            elif fighter1.str < fighter2.str:
                fighter1.health -= fighter2.atk
                print('{} gets hit for {} dmg, health is {}'.format(fighter1.name, fighter2.atk, fighter1.health))
            else:
                fighter1.health -= fighter2.atk
                fighter2.health -= fighter1.atk
                print("Both get hit, {}'s health is {} and {}'s health is {}".format(fighter1.name, fighter1.health,
                                                                                     fighter2.name,
                                                                                     fighter2.health))
            death_confirm(fighter1, fighter2)
        elif c == 2:
            if fighter1.agi > fighter2.agi:
                fighter2.health -= fighter1.atk
                print('{} gets hit for {} dmg, health is {}'.format(fighter2.name, fighter1.atk, fighter2.health))
            elif fighter1.agi < fighter2.agi:
                fighter1.health -= fighter2.atk
                print('{} gets hit for {} dmg, health is {}'.format(fighter1.name, fighter2.atk, fighter1.health))
            else:
                fighter1.health -= fighter2.atk
                fighter2.health -= fighter1.atk
                print("Both get hit, {}'s health is {} and {}'s health is {}".format(fighter1.name, fighter1.health,
                                                                                     fighter2.name,
                                                                                     fighter2.health))
            death_confirm(fighter1, fighter2)
        elif c == 3:
            if fighter1.int > fighter2.int:
                fighter2.health -= fighter1.atk
                print('{} gets hit for {} dmg, health is {}'.format(fighter2.name, fighter1.atk, fighter2.health))
            elif fighter1.int < fighter2.int:
                fighter1.health -= fighter2.atk
                print('{} gets hit for {} dmg, health is {}'.format(fighter1.name, fighter2.atk, fighter1.health))
            else:
                fighter1.health -= fighter2.atk
                fighter2.health -= fighter1.atk
                print("Both get hit, {}'s health is {} and {}'s health is {}".format(fighter1.name, fighter1.health,
                                                                                     fighter2.name,
                                                                                     fighter2.health))
            death_confirm(fighter1, fighter2)


fighting()
