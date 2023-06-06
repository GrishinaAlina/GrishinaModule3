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


class Army:
    def __init__(self):
        self.reserv = []


    def add_units(self, who, coll):
        for _ in range(coll):
            self.reserv.append(who())


def fight(who1: object, who2):
    while who1.is_alive:
        who1.damage(who2)
        if who2.is_alive:
            who2.damage(who1)
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

ar2 = Army()
ar2.add_units(Knight, 3)
ar2.add_units(Warrior, 10)
ar2.add_units(Defender, 10)

b = Battle()
print(b.fight(ar1, ar2))
