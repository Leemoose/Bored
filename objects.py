
class Objects():
    def __init__(self, x, y, id_tag, render_tag, name):
        self.id_tag = id_tag
        self.render_tag = render_tag
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return self.name

class Tile(Objects):
    def __init__(self, x, y, render_tag = 0, passable = False, id_tag = 0):
        super().__init__(x, y, id_tag, render_tag, "Tile")
        self.passable = passable
        self.seen = False

class Item(Objects):
    def __init__(self, x, y, number_tag = 0, id_tag = 0):
        super().__init__(x, y, id_tag, number_tag, "Item")
        self.equipable = equipable 
        self.dropable = True
