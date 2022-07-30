import random
import dice as R
import objects as O

class Character():
    def __init__(self, endurance = 0, intelligence = 0, dexterity = 0, strength = 0, speed = 100, health = 100, mana = 0):
        self.endurance = endurance
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.strength = strength
        self.speed = speed
        self.health = health
        self.mana = mana
        self.stored_movement = 0
        self.alive = True
        self.inventory = []
        self.main_weapon = None

    def is_alive(self):
        if self.health <= 0:
            self.alive = False
            return False
        return True

    def take_damage(self, damage):
        self.health -= damage


    def attack_move(self, move_x, move_y, floormap, monster, monsterID, monster_map, item_ID):
        x = monster.x + move_x
        y = monster.y - move_y
        if ((x>=0) & (y>=0) & (x < floormap.width) & (y < floormap.height)):
            if (monster_map.track_map[x][y]) != 0:
                defender = monsterID.get_subject(monster_map.track_map[x][y])
                monster.attack(monster, defender)
            else:
                self.move(move_x, move_y, floormap, monster, monster_map)


    def move(self, move_x, move_y, floormap, monster, monster_map):
        speed_to_space = 100
        speed = self.speed + self.dexterity // 10
        if floormap.get_passable(monster.x + move_x, monster.y - move_y, monster_map):
            spaces = speed // speed_to_space
            self.stored_movement += speed % speed_to_space
            if self.stored_movement >= speed_to_space:
                spaces += self.stored_movement // speed_to_space
                self.stored_movement = self.stored_movement % speed_to_space
            monster_map.track_map[monster.x][monster.y] = 0
            while spaces > 0 & floormap.get_passable(monster.x + move_x, monster.y - move_y, monster_map):
                monster.y -= move_y
                monster.x += move_x
                spaces -= 1
            monster_map.track_map[monster.x][monster.y] = monster.id_tag

    def attack(self, attacker, defender):
        if self.main_weapon == None:
            damage = R.roll_dice(1, 20)[0]
        else:
            damage = self.main_weapon.attack()
        defense = defender.defend()
        if damage - defense > 0:
            defender.take_damage(damage - defense)

    def defend(self):
        defense = R.roll_dice(1, 1)[0]
        return defense

    def grab(self, player, item_map, item_ID):
        key = item_map.location(player.x,player.y)
        if key != 0:
            item = item_ID.get_subject(key)
            self.inventory.append(item)
            item_ID.remove_subject(key)
            item_map.clear_location(item.x, item.y)

    def drop(self, item_ID, item_map):
        if len(self.inventory) != 0 and self.inventory[-1].dropable == True:
            item = self.inventory.pop()
            item_ID.add_subject(item.ID, item)
            item_map.place_thing(item, (self.x, self.y))
            item.x = self.x
            item.y = self.y

    def equip(self):
        if len(self.inventory) != 0:
            item = self.inventory[-1]
            self.main_weapon = item
            item.dropable = False
            item.name = "Main Weapon"

    def unequip(self):
        if self.main_weapon != None:
            item = self.main_weapon
            self.main_weapon = None
            item.name = "Item"
            item.dropable = True


class Player(O.Objects):
    def __init__(self, x, y):
        super().__init__(x, y, 1, 200, "Player")
        self.character = Character()


class Monster(Character):
    def __init__(self, number_tag, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.number_tag = number_tag
        self.ID = 0

    def gain_ID(self, ID):
        self.ID = ID

    def get_number_tag(self):
        return self.number_tag