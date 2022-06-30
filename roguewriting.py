import sys, pygame, random
import generated_map as M
import display as D
import keyboard as K
import character as C
import items as I

#random.seed(420)
pygame.init()
pygame.font.init()

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

class FloorMap():
    def __init__(self, textSize, generated_map, width, height):
        self.blockSize = textSize
        self.width = width
        self.height = height
        self.size = (self.width, self.height)
        self.map_tile = generated_map

    def __str__(self):
        allrows = ""
        for x in range(self.width):
            row = ' '.join(self.get_tile(self.map_tile[x][y]) for y in range(self.height))
            allrows = allrows + row + "\n"      
        return allrows

    def get_position(self, x, y):
        return(x*self.blockSize, y*self.blockSize)

    def get_tag(self, x, y):
        return self.map_tile[x][y].number_tag

    def get_passable(self, x, y, monster_map):
        if ((x>=0) & (y>=0) & (x < self.width) & (y < self.height)):
            return ((self.map_tile[x][y].passable) & (monster_map.location(x,y) == 0))
        else:
            return False

class Loops(): 
    def __init__(self):
        self.action = True
        self.inventory = False
        self.update_screen = True

    def action_loop(self, player, floormap, monster_ID, monster_map, item_ID, item_map):
        if self.update_screen == True:
            display.update_display(colors, floormap, tileDict, monster_ID, item_ID, monster_map, player)
            self.update_screen = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                keyboard.key_action(event, player, floormap, monster_ID, monster_map, item_ID, item_map, self)
                self.update_screen = True
        return True

    def inventory_loop(self, keyboard, player):
        if self.update_screen == True:
            display.update_inventory(player)
            self.update_screen = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                keyboard.key_inventory(event, self, player)
                self.update_screen = True
        return True

textSize = 32
width = 100
height = 100
screen_width = 20
screen_height = 20
colors = ColorDict()
tileDict = M.TileDict(textSize, colors)
monster_ID = ID()
item_ID = ID()
loop = Loops()

generator = M.DungeonGenerator(width, height)
generated_map = generator.get_map()
floormap = FloorMap(textSize, generated_map, width, height)
monster_map = M.TrackingMap(width, height)
item_map = M.TrackingMap(width, height)
player = C.Player()

orc = C.Monster(101, 3, 1)
ax = I.Item(300, True, 2, 2)
ax1 = I.Item(300, True, 4, 2)

monster_ID.tag_subject(orc)
item_ID.tag_subject(ax)
item_ID.tag_subject(ax1)

monster_map.place_thing(player, (player.x, player.y))
monster_map.place_thing(orc, (orc.x, orc.y))
item_map.place_thing(ax, (2, 2))
item_map.place_thing(ax1, (4, 2))

display = D.Display(floormap, screen_width, screen_height, textSize)
keyboard = K.Keyboard()

player_turn = True
while player_turn:
    if loop.action == True:
        player_turn = loop.action_loop(player, floormap, monster_ID, monster_map, item_ID, item_map)
    elif loop.inventory == True:
        player_turn = loop.inventory_loop(keyboard, player)
    
                