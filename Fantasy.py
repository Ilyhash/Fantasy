from random import randint
import time


class Heroes:
    heroes = {}

    def __init__(self, name, number):
        self.name = name
        self.number = number
        Heroes.heroes[self.number] = self


class Knight(Heroes):
    def __init__(self, name, number):
        self.name = name
        self.desc = 'the noble warrior'
        self.health = 35
        self.minatk = 2
        self.maxatk = 4
        self.str = 5
        self.agi = 3
        self.int = 1
        super().__init__(name, number)


class Assassin(Heroes):
    def __init__(self, name, number):
        self.name = name
        self.desc = 'the silent killer'
        self.health = 25
        self.minatk = 3
        self.maxatk = 6
        self.str = 1
        self.agi = 6
        self.int = 2
        super().__init__(name, number)


class Mage(Heroes):
    def __init__(self, name, number):
        self.name = name
        self.desc = 'the wise wizard'
        self.health = 20
        self.minatk = 3
        self.maxatk = 4
        self.str = 1
        self.agi = 2
        self.int = 6
        super().__init__(name, number)


class Hobbit(Heroes):
    def __init__(self, name, number):
        self.name = name
        self.desc = 'the half-man'
        self.health = 20
        self.minatk = 2
        self.maxatk = 3
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
TheEmperor = Knight('The Emperor', 6)
TheEmperor.desc = 'of mankind'
TheEmperor.health = 100
TheEmperor.minatk = 8
TheEmperor.maxatk = 12
TheEmperor.int += 1
Horus = Knight('Horus', 7)
Horus.desc = 'the Traitor'
Horus.health = 50
Horus.agi += 1


def fighter_choice():
    i = randint(1, len(Heroes.heroes))
    return Heroes.heroes[i]


def special_case(fighter1, fighter2):
    if fighter1 == Frodo or fighter2 == Frodo:
        c = randint(1, 5)
        if c == 5 and fighter1 == Frodo:
            print('Frodo used the ring and killed {} \n{} is dead'.format(fighter2.name, fighter2.name))
            fighter2.health = 0
            return
        elif c == 5 and fighter2 == Frodo:
            print('Frodo used the ring and killed {} \n{} is dead'.format(fighter1.name, fighter1.name))
            fighter1.health = 0
            return
    if fighter1 == Horus and fighter2 == TheEmperor or fighter1 == TheEmperor and fighter2 == Horus:
        Horus.minatk = 20
        Horus.maxatk = 30
    if fighter1 == Boromir or fighter2 == Boromir:
        Boromir.health = 0
        print('{} dies'.format(Boromir.name))


def death_confirm(fighter1, fighter2):
    while fighter1.health <= 0 or fighter2.health <= 0:
        if fighter1.health <= 0 and fighter2.health <= 0:
            print('Both are dead')
        elif fighter1.health <= 0:
            print('{} is dead.'.format(fighter1.name))
        elif fighter2.health <= 0:
            print('{} is dead.'.format(fighter2.name))
        break


def atk(self):
    return randint(self.minatk, self.maxatk)


def stat_choice(fighter1, fighter2):
    c = randint(1, 3)
    if c == 1:
        par1 = fighter1.str
        par2 = fighter2.str
    elif c == 2:
        par1 = fighter1.agi
        par2 = fighter2.agi
    elif c == 3:
        par1 = fighter1.int
        par2 = fighter2.int
    return par1, par2

def fighting():
    fighter1 = fighter_choice()
    fighter2 = fighter_choice()
    while fighter1 == fighter2:
        fighter2 = fighter_choice()
    print('{} {}'.format(fighter1.name, fighter1.desc))
    time.sleep(1)
    print('vs')
    time.sleep(1)
    print('{} the {} \n'.format(fighter2.name, fighter2.desc))
    time.sleep(1)
    special_case(fighter1, fighter2)
    while fighter1.health > 0 and fighter2.health > 0:
        par1, par2 = stat_choice(fighter1, fighter2)
        if par1 > par2:
            attack = atk(fighter1)
            fighter2.health = fighter2.health - attack if fighter2.health >= attack else 0
            print('{} gets hit for {} dmg, health is {}'.format(fighter2.name, attack, fighter2.health))
        elif par1 < par2:
            attack = atk(fighter2)
            fighter1.health = fighter1.health - attack if fighter1.health >= attack else 0
            print('{} gets hit for {} dmg, health is {}'.format(fighter1.name, attack, fighter1.health))
        else:
            attack1 = atk(fighter1)
            attack2 = atk(fighter2)
            fighter1.health = fighter1.health - attack2 if fighter1.health >= attack2 else 0
            fighter2.health = fighter2.health - attack1 if fighter2.health >= attack1 else 0
            print("Both get hit, {}'s health is {} and {}'s health is {}".format(fighter1.name, fighter1.health,
                                                                                 fighter2.name,
                                                                                 fighter2.health))
        time.sleep(1)
        death_confirm(fighter1, fighter2)


fighting()
