from random import randint
import time
import Characters as Ch


def fighter_choice():
    i = randint(1, len(Ch.Heroes.heroes))
    return Ch.Heroes.heroes[i]


def special_case(fighter1, fighter2):
    if fighter1 == Ch.Frodo or fighter2 == Ch.Frodo:
        c = randint(1, 5)
        if c == 5 and fighter1 == Ch.Frodo:
            print('Frodo used the ring and killed {} \n{} is dead'.format(fighter2.name, fighter2.name))
            fighter2.health = 0
            return
        elif c == 5 and fighter2 == Ch.Frodo:
            print('Frodo used the ring and killed {} \n{} is dead'.format(fighter1.name, fighter1.name))
            fighter1.health = 0
            return
    if fighter1 == Ch.Horus and fighter2 == Ch.TheEmperor or fighter1 == Ch.TheEmperor and fighter2 == Ch.Horus:
        Ch.Horus.min_atk = 20
        Ch.Horus.max_atk = 30
    if fighter1 == Ch.Boromir or fighter2 == Ch.Boromir:
        Ch.Boromir.health = 0
        print('{} dies'.format(Ch.Boromir.name))
    if fighter1 == Ch.ChaosKnight or fighter2 == Ch.ChaosKnight:
        r = randint(1, 5)
        Ch.ChaosKnight.str = randint(Ch.Knight.str - r, Ch.Knight.str + r)
        Ch.ChaosKnight.agi = randint(Ch.Knight.agi - r, Ch.Knight.agi + r)
        Ch.ChaosKnight.int = randint(Ch.Knight.int - r, Ch.Knight.int + r)
        Ch.ChaosKnight.min_atk = randint(1, 5)
        Ch.ChaosKnight.max_atk = Ch.ChaosKnight.min_atk + randint(0, 2)


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
    return randint(self.min_atk, self.max_atk)


def stat_choice(fighter1, fighter2):
    par1 = 0
    par2 = 0
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
    return [par1, par2]


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
