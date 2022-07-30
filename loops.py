import pygame
import display as D

class ColorDict():
    #Just a dictionary of colors that I decide to use
    def __init__(self):
        colors = {}
        colors["white"] = (255,255,255)
        colors["green"] = (0,255,0)
        colors["blue"] = (0,0,128)
        colors["black"] = (0,0,0)
        self.colors = colors

    def getColor(self, color):
        return self.colors[color]

class ID():
    def __init__(self):
        self.subjects = {}
        self.ID_count = 0

    def tag_subject(self, subject):
        self.ID_count += 1
        subject.gain_ID(self.ID_count)
        self.subjects[self.ID_count] = subject

    def get_subject(self, key):
        return self.subjects[key]

    def remove_subject(self, key):
        self.subjects.pop(key)

    def add_subject(self, key, subject):
        self.subjects[key] = subject

class Loops(): 
    def __init__(self):
        self.action = False
        self.inventory = False
        self.race = False
        self.update_screen = True
        self.main = True
        self.classes = False
        self.main_buttons = None

    def action_loop(self, player, floormap, monster_ID, monster_map, item_ID, item_map, keyboard):
        action = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                key = keyboard.key_string(event.key)
                if self.action == True:
                    keyboard.key_action(event, player, floormap, monster_ID, monster_map, item_ID, item_map, self, key)
                elif self.inventory == True:
                    keyboard.key_inventory(event, self, player, item_ID, item_map, key)
                elif self.main == True:
                    keyboard.key_main_screen(key, self)
                elif self.race == True:
                    keyboard.key_race_screen(key, self)
                self.update_screen = True

            elif event.type == pygame.MOUSEBUTTONUP:
                x,y = pygame.mouse.get_pos()
                if self.main == True:
                    for button in self.main_buttons.buttons:
                        if self.main_buttons.buttons[button].clicked(x, y):
                            key = self.main_buttons.buttons[button].action
                        break
                    keyboard.key_main_screen(key, self)

                elif self.race == True:
                    for button in self.race_buttons.buttons:
                        if self.race_buttons.buttons[button].clicked(x, y):
                            key = self.race_buttons.buttons[button].action
                        break
                    keyboard.key_race_screen(key, self)

                elif self.classes == True:
                    for button in self.class_buttons.buttons:
                        if self.class_buttons.buttons[button].clicked(x, y):
                            key = self.class_buttons.buttons[button].action
                        break
                    keyboard.key_class_screen(key, self)
                self.update_screen = True
        return True

    def change_screen(self, player, floormap, monster_ID, monster_map, item_ID, item_map, keyboard, display, colors, tileDict):
        if self.action == True:
            display.update_display(colors, floormap, tileDict, monster_ID, item_ID, monster_map, player)
        elif self.inventory == True:
            display.update_inventory(player)
        elif self.main == True:
            display.update_main()
        elif self.race == True:
            display.update_race()
        elif self.classes == True:
            display.update_class()
        pygame.display.update()
        self.update_screen = False

    def start_game(self, display):
        self.main_buttons = D.create_main_screen(display)
        self.race_buttons = D.create_race_screen(display)
        self.class_buttons = D.create_class_screen(display)