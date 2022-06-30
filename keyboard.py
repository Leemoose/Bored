import pygame

class Keyboard():
    def __init__(self):
        keys_to_string = {}
        keys_to_string[pygame.K_w] = "w"
        keys_to_string[pygame.K_a] = "a"
        keys_to_string[pygame.K_s] = "s"
        keys_to_string[pygame.K_d] = "d"
        keys_to_string[pygame.K_i] = "i"
        keys_to_string[pygame.K_g] = "g"
        keys_to_string[pygame.K_u] = "u"
        keys_to_string[pygame.K_e] = "e"
        keys_to_string[pygame.K_ESCAPE] = "esc"
        self.keys_to_string = keys_to_string

    def key_string(self, key):
        return self.keys_to_string[key]

    def key_action(self, event, player, floormap, monsterID, monster_map, item_ID, item_map, loop):
            key = self.key_string(event.key)
            if key == "w":
                player.attack_move(0, 1, floormap, player, monsterID, monster_map, item_ID)
            elif key == "a":
                player.attack_move(-1, 0, floormap, player, monsterID, monster_map, item_ID)
            elif key == "s":
                player.attack_move(0, -1, floormap, player, monsterID, monster_map, item_ID)
            elif key == "d":
                player.attack_move(1, 0, floormap, player, monsterID, monster_map, item_ID)
            elif key == "g":
                player.grab(player, item_map, item_ID)
            elif key == "i":
                loop.action = False
                loop.inventory = True
                loop.update_screen = True

    def key_inventory(self, event, loop, player, item_ID, item_map):
            key = self.key_string(event.key)
            if key == "esc":
                loop.inventory = False
                loop.action = True
                loop.update_screen = True
            elif key == "d":
                player.drop(item_ID, item_map)
                loop.update_screen = False
            elif key == "e":
                player.equip()
            elif key == "u":
                player.unequip()