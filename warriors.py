class Warrior:
    def __init__(self, health = 50, attack = 5):
        self.health = health
        self.attack = attack
        self.is_alive = True if health > 0 else False


class Knight(Warrior):      # zdedi po Warrior
    # def __init__(self, health = 50, attack = 7):
    #     self.health = health
    #     self.attack = attack
    #     self.is_alive = True # if health > 0 else False
    def __init__(self, health=50, attack=7):
        super().__init__(health, attack)        # odkazuje sa na konstruktor predchodcu


def fight(w1, w2):
    while w1.is_alive and w2.is_alive:
        w2.health -= w1.attack
        w2.is_alive = True if w2.health > 0 else False
        if w2.is_alive:
            w1.health -= w2.attack
            w1.is_alive = True if w2.health > 0 else False
        else:
            break
        # print(w1.health, w2.health)
    return w1.is_alive


chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()

print(fight(chuck, bruce))