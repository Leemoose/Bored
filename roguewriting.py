import sys, pygame, random
import mapping as M
import display as D
import keyboard as K
import character as C
import items as I
import loops as L

#random.seed(420)
pygame.init()
pygame.font.init()



textSize = 32
width = 1280
height = 720
textWidth = int(width / textSize)
textHeight = int(height / textSize)

colors = L.ColorDict()
tileDict = M.TileDict(textSize, colors)
monster_ID = L.ID()
item_ID = L.ID()
loop = L.Loops()

generator = M.DungeonGenerator(width, height)
generated_map = generator.get_map()
floormap = L.FloorMap(textSize, generated_map, width, height)
monster_map = M.TrackingMap(width, height)
item_map = M.TrackingMap(width, height)

player = C.Player()

orc = C.Monster(101, 3, 1)
ax = I.Ax(300, True, 2, 2)
ax1 = I.Ax(300, True, 4, 2)

monster_ID.tag_subject(orc)
item_ID.tag_subject(ax)
item_ID.tag_subject(ax1)

monster_map.place_thing(player, (player.x, player.y))
monster_map.place_thing(orc, (orc.x, orc.y))
item_map.place_thing(ax, (2, 2))
item_map.place_thing(ax1, (4, 2))

display = D.Display(floormap, width, height, textSize, textWidth, textHeight)
keyboard = K.Keyboard()

player_turn = True
loop.start_game(display)
while player_turn:
    if loop.update_screen == True:
        loop.change_screen(player, floormap, monster_ID, monster_map, item_ID, item_map, keyboard, display, colors, tileDict)
    player_turn = loop.action_loop(player, floormap, monster_ID, monster_map, item_ID, item_map, keyboard)