import pygame

class Display():
    def __init__(self, floormap, width, height, textSize):
        pygame.display.set_caption('Tiles')
        self.win = pygame.display.set_mode(floormap.get_position(width,height))
        self.screen_width = width
        self.screen_height = height
        self.textSize = textSize

    def update_display(self, colorDict, floormap, tileDict, monsterID, item_ID, monster_map, player):
        self.win.fill(colorDict.getColor("black"))
        r_x = self.screen_width // 2
        r_y = self.screen_height // 2
        x_start = player.x - r_x
        x_end = player.x + r_x
        y_start = player.y - r_y
        y_end = player.y + r_y

        for x in range(x_start, x_end):
            for y in range(y_start, y_end):
                if (x < 0 or x >= floormap.width or y < 0 or y >= floormap.height):
                    pass
                else:
                    tag = tileDict.tile_string(floormap.get_tag(x,y))
                    self.win.blit(tag, floormap.get_position(x - x_start,y - y_start))

        for key in item_ID.subjects:
            item = item_ID.get_subject(key)
            if (item.x >= x_start and item.x < x_end and item.y >= y_start and item.y < y_end):
                item_tile = tileDict.tile_string(item.get_number_tag())
                self.win.blit(item_tile, floormap.get_position(item.x - x_start,item.y - y_start))

        dead_monsters = []
        for key in monsterID.subjects:
            monster = monsterID.get_subject(key)
            if monster.character.is_alive():
                if (monster.x >= x_start and monster.x < x_end and monster.y >= y_start and monster.y < y_end):
                    monster_tile = tileDict.tile_string(monster.get_number_tag())
                    self.win.blit(monster_tile, floormap.get_position(monster.x - x_start,monster.y - y_start))
            else:
                dead_monsters.append(key)
                monster_map.clear_location(monster.x, monster.y)

        self.win.blit(tileDict.tile_string(200), floormap.get_position(r_x, r_y))

        for key in dead_monsters:
            monsterID.subjects.pop(key)

        pygame.display.update()
