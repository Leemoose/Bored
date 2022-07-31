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
        keys_to_string[pygame.K_1] = "1"
        self.keys_to_string = keys_to_string

    def key_string(self, key):
        return self.keys_to_string[key]

    def key_action(self, player, floormap, monsterID, monster_map, item_ID, item_map, loop, key):
            if key == "w":
                player.character.attack_move(0, 1, floormap, player, monsterID, monster_map, item_ID)
            elif key == "a":
                player.character.attack_move(-1, 0, floormap, player, monsterID, monster_map, item_ID)
            elif key == "s":
                player.character.attack_move(0, -1, floormap, player, monsterID, monster_map, item_ID)
            elif key == "d":
                player.character.attack_move(1, 0, floormap, player, monsterID, monster_map, item_ID)
            elif key == "g":
                player.character.grab(player, item_map, item_ID)
            elif key == "i":
                loop.action = False
                loop.inventory = True
                loop.update_screen = True

    def key_inventory(self, loop, player, item_dict, item_map, key):
            if key == "esc":
                loop.inventory = False
                loop.action = True
                loop.update_screen = True
            elif key == "e":
                player.character.equip()
            elif key == "u":
                player.character.unequip()

            for i in range(len(player.character.inventory)):
                print(str(i+1), key)
                if str(i + 1) == key:
                    loop.inventory = False
                    loop.items = True
                    loop.item_for_item_screen = player.character.inventory[i]

    def key_main_screen(self, key, loop):

        if key == "1":
            loop.main = False
            loop.race = True
            loop.update_screen = True

    def key_race_screen(self, key, loop):
        if key == "esc":
            loop.race = False
            loop.main = True
            loop.update_screen = True
        elif key == "1":
            loop.race = False
            loop.classes = True
            loop.update_screen = True

    def key_class_screen(self, key, loop):
        if key == "esc":
            loop.classes = False
            loop.race = True
            loop.update_screen = True        
        elif key == "1":
            loop.classes = False
            loop.action = True
            loop.update_screen = True
            loop.start_game()

    def key_item_screen(self, key, loop, item_dict, item_map, player, item):
            if key == "esc":
                loop.items = False
                loop.inventory = True
                loop.update_screen = True
            elif key == "d":
                player.character.drop(item.id_tag, item_dict, player.x, player.y, item_map)
                loop.items = False
                loop.inventory = True
                loop.update_screen = True
            elif key == "e":
                player.character.equip()
            elif key == "u":
                player.character.unequip()