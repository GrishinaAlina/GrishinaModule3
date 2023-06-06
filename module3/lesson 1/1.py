class Warrior:

    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True

    def damage(self, hero2):
        self.health -= hero2.attack
        if self.health <= 0:
            self.is_alive = False


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 3
        self.health = 60
        self.defen = 2

    def damage(self, hero2, sun=True):
        if self.defen < hero2.attack:
            self.health -= hero2.attack - self.defen
            if self.health <= 0:
                self.is_alive = False

class Vampire(Warrior):

    def __init__(self):
        super().__init__()
        self.attack = 4
        self.health = 40
        self.vampirism = 50 # в процентах

class Army:
    def __init__(self):
        self.reserv = []


    def add_units(self, who, coll):
        for _ in range(coll):
            self.reserv.append(who())

def chek(who1: object, who2: object):
    if isinstance(who1, Vampire):
        if isinstance(who2, Defender):
            who1.health += \
                0 if who1.attack < who2.defen \
                    else (who1.attack - who2.defen) * (who1.vampirism / 100)
        else:
            who1.health += who1.attack * (who1.vampirism / 100)


def fight(who1: object, who2):
    while who1.is_alive:
        who1.damage(who2)
        chek(who1, who2)
        if who2.is_alive:
            who2.damage(who1)
            chek(who2, who1)
        else:
            return True
    return False


class Battle:

    def fight(self, ar1, ar2):
        while len(ar1.reserv) > 0 and len(ar2.reserv) > 0:
            if fight(ar1.reserv[0], ar2.reserv[0]):
                ar2.reserv.pop(0)
            else:
                ar1.reserv.pop(0)
        if len(ar1.reserv) > 0:
            return True
        else:
            return False


w1 = Warrior()
k1 = Knight()
ar1 = Army()
ar1.add_units(Warrior, 10)
ar1.add_units(Defender, 5)
ar1.add_units(Knight, 5)
ar1.add_units(Vampire, 6)

ar2 = Army()
ar2.add_units(Knight, 3)
ar2.add_units(Vampire, 123)
ar2.add_units(Warrior, 10)
ar2.add_units(Defender, 10)

b = Battle()
print(b.fight(ar1, ar2))
print()
print()
print()