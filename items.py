import dice as R

class Item():
    def __init__(self, number_tag, equipable, x, y):
        self.equipable = equipable
        self.number_tag = number_tag 
        self.name = "Item"
        self.x = x
        self.y = y

    def __str__(self):
        return self.name

    def gain_ID(self, ID):
        self.ID = ID

    def get_number_tag(self):
        return self.number_tag

class Weapon(Item):
    def __init__(self, number_tag, equipable, x, y):
        super().__init__(number_tag, equipable, x, y)

class Ax(Weapon):
    def __init__(self, number_tag, equipable, x, y):
        super().__init__(number_tag, equipable, x, y)
        self.melee = True

    def attack(self):
        damage = R.roll_dice(5, 20)[0]
        return damage

