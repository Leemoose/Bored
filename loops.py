import pygame
import display as D
import mapping as M
import character as C
import items as I
import random

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
    def __init__(self, width, height, textSize):
        self.action = False
        self.inventory = False
        self.race = False
        self.update_screen = True
        self.main = True
        self.classes = False
        self.width = width
        self.height = height
        self.textSize = textSize
        self.monster_dict = ID()
        self.item_dict = ID()

    def action_loop(self, keyboard):
        action = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                key = keyboard.key_string(event.key)
                if self.action == True:
                    keyboard.key_action(event, self.player, self.tile_map, self.monster_dict, self.monster_map, self.item_dict, self.item_map, self, key)
                elif self.inventory == True:
                    keyboard.key_inventory(event, self, self.player, self.item_dict, self.item_map, key)
                elif self.main == True:
                    keyboard.key_main_screen(key, self)
                elif self.race == True:
                    keyboard.key_race_screen(key, self)
                elif self.classes == True:
                    keyboard.key_class_screen(key, self)
                self.update_screen = True

            elif event.type == pygame.MOUSEBUTTONUP:
                x,y = pygame.mouse.get_pos()
                if self.main == True:
                    for button in self.main_buttons.buttons:
                        if self.main_buttons.buttons[button].clicked(x, y):
                            key = self.main_buttons.buttons[button].action
                            keyboard.key_main_screen(key, self)
                            break

                elif self.race == True:
                    for button in self.race_buttons.buttons:
                        if self.race_buttons.buttons[button].clicked(x, y):
                            key = self.race_buttons.buttons[button].action
                            keyboard.key_race_screen(key, self)
                            break

                elif self.classes == True:
                    for button in self.class_buttons.buttons:
                        if self.class_buttons.buttons[button].clicked(x, y):
                            key = self.class_buttons.buttons[button].action
                            keyboard.key_class_screen(key, self)
                            break
                self.update_screen = True
        return True

    def change_screen(self,  keyboard, display, colors, tileDict):
        if self.action == True:
            display.update_display(colors, self.tile_map, tileDict, self.monster_dict, self.item_dict, self.monster_map, self.player)
        elif self.inventory == True:
            display.update_inventory(self.player)
        elif self.main == True:
            display.update_main()
        elif self.race == True:
            display.update_race()
        elif self.classes == True:
            display.update_class()
        pygame.display.update()
        self.update_screen = False

    def init_game(self, display):
        self.main_buttons = D.create_main_screen(display)
        self.race_buttons = D.create_race_screen(display)
        self.class_buttons = D.create_class_screen(display)

    def start_game(self):
        wid = 60
        hei = 60
        generator = M.DungeonGenerator(wid, hei)
        generated_map = generator.get_map()
        self.tile_map = M.TileMap(wid, hei, generated_map)
        self.monster_map = M.TrackingMap(wid, hei)
        self.item_map = M.TrackingMap(wid, hei)
        startx = random.randint(0, wid-1)
        starty = random.randint(0,hei-1)
        while (self.tile_map.tile_map[startx][starty].passable == False):
            startx = random.randint(0, wid-1)
            starty = random.randint(0,hei-1)
        self.player = C.Player(startx, starty)
        self.monster_map.place_thing(self.player)

        ax = I.Ax(300, True, startx, starty)
        self.item_dict.tag_subject(ax)
        self.item_map.place_thing(ax)  
        
        number_of_orcs = random.randint(20, 30)
        for i in range(number_of_orcs):
            startx = random.randint(0, wid-1)
            starty = random.randint(0,hei-1)

            while (self.tile_map.tile_map[startx][starty].passable == False):
                startx = random.randint(0, wid-1)
                starty = random.randint(0,hei-1)

            orc = C.Monster(101, startx, starty)
            self.monster_dict.tag_subject(orc)
            self.monster_map.place_thing(orc)

        number_of_axes = random.randint(15,20)
        for i in range(number_of_axes):
            startx = random.randint(0, wid-1)
            starty = random.randint(0,hei-1)

            while (self.tile_map.tile_map[startx][starty].passable == False):
                startx = random.randint(0, wid-1)
                starty = random.randint(0,hei-1)

            ax = I.Ax(300, True, startx, starty)
            self.item_dict.tag_subject(ax)
            self.item_map.place_thing(ax)        