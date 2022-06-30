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
        keys_to_string[pygame.K_ESCAPE] = "esc"
        self.keys_to_string = keys_to_string

    def key_string(self, key):
        return self.keys_to_string[key]

    def key_action(self, event, player, floormap, monsterID, monster_map, item_ID, item_map, loop):
        try: 
            key = self.key_string(event.key)
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
        except:
            return

    def key_inventory(self, event, loop, player):
        try:
            key = self.key_string(event.key)
            if key == "esc":
                loop.inventory = False
                loop.action = True
                loop.update_screen = True
        except:
            pass