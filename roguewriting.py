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


textSize = 32
width = 100
height = 100
screen_width = 20
screen_height = 20
colors = ColorDict()
tileDict = M.TileDict(textSize, colors)
monster_ID = ID()
item_ID = ID()

generator = M.DungeonGenerator(width, height)
generated_map = generator.get_map()
floormap = FloorMap(textSize, generated_map, width, height)
monster_map = M.TrackingMap(width, height)
item_map = M.TrackingMap(width, height)
player = C.Player()

orc = C.Monster(101, 3, 1)
ax = I.Item(300, True, 2, 2)

monster_ID.tag_subject(orc)
item_ID.tag_subject(ax)

monster_map.place_thing(player, (player.x, player.y))
monster_map.place_thing(orc, (orc.x, orc.y))
item_map.place_thing(ax, (2, 2))

display = D.Display(floormap, screen_width, screen_height, textSize)
keyboard = K.Keyboard()

update = True
yes = True
while yes:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            yes = False
        elif event.type == pygame.KEYDOWN:
            keyboard.key_action(event, player, floormap, monster_ID, monster_map, item_ID, item_map)
            update = True

    if update == True:
        display.update_display(colors, floormap, tileDict, monster_ID, item_ID, monster_map, player)
        update = False
                