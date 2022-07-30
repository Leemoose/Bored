import sys, pygame, random
import mapping as M
import display as D
import keyboard as K
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
loop = L.Loops(width, height, textSize)



#orc = C.Monster(101, 3, 1)
#ax = I.Ax(300, True, 2, 2)
#ax1 = I.Ax(300, True, 4, 2)

#monster_ID.tag_subject(orc)
#item_ID.tag_subject(ax)
#item_ID.tag_subject(ax1)

#monster_map.place_thing(orc)
#item_map.place_thing(ax, (2, 2))
#item_map.place_thing(ax1, (4, 2))

display = D.Display(width, height, textSize, textWidth, textHeight)
keyboard = K.Keyboard()

player_turn = True
loop.init_game(display)
while player_turn:
    if loop.update_screen == True:
        loop.change_screen(monster_ID, item_ID, keyboard, display, colors, tileDict)
    player_turn = loop.action_loop(monster_ID, item_ID, keyboard)