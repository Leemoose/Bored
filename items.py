import dice as R
import objects as O

class Weapon(O.Item):
    def __init__(self, number_tag, equipable, x, y):
        super().__init__(number_tag, equipable, x, y)

class Ax(Weapon):
    def __init__(self, number_tag, equipable, x, y):
        super().__init__(number_tag, equipable, x, y)
        self.melee = True

    def attack(self):
        damage = R.roll_dice(100, 200)[0]
        return damage

