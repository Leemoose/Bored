import pygame


class Buttons():
    def __init__(self):
        self.buttons = {}

    def add(self, button, name):
        self.buttons[name] = button

class Button():
    def __init__(self, width, height, asset, modx, mody, action, positionx, positiony):
        self.width = width * modx
        self.height = height * mody
        self.modx = modx
        self.mody = mody
        self.img = pygame.transform.scale(pygame.image.load("assets/button.png"),(self.width, self.height))
        self.action = action
        self.positionx = positionx
        self.positiony = positiony

    def scale(self, screen_width, screen_height):
        self.img = pygame.transform.scale(self.img, (screen_width * self.modx, screen_height * self.mody))

    def clicked(self, x, y):
        pressed = False
        if self.positionx < x and x < self.positionx + self.width:
            return (self.positionx < x and x < self.positionx + self.width) and (self.positiony < y and y < self.positiony + self.height)



class Display():
    def __init__(self, width, height, textSize, textWidth, textHeight):
        pygame.display.set_caption('Tiles')
        self.win = pygame.display.set_mode((width, height))
        self.screen_width = width
        self.screen_height = height
        self.textWidth = textWidth
        self.textHeight = textHeight
        self.textSize = textSize

    def update_display(self, colorDict, floormap, tileDict, monsterID, item_ID, monster_map, player):
        self.win.fill(colorDict.getColor("black"))
        r_x = self.textWidth // 2
        r_y = self.textHeight // 2

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
                    self.win.blit(tag, (self.textSize * (x - x_start), self.textSize * (y - y_start)))

        for key in item_ID.subjects:
            item = item_ID.get_subject(key)
            if (item.x >= x_start and item.x < x_end and item.y >= y_start and item.y < y_end):
                item_tile = tileDict.tile_string(item.get_number_tag())
                self.win.blit(item_tile, (item.x - x_start, item.y - y_start))

        dead_monsters = []
        for key in monsterID.subjects:
            monster = monsterID.get_subject(key)
            if monster.is_alive():
                if (monster.x >= x_start and monster.x < x_end and monster.y >= y_start and monster.y < y_end):
                    monster_tile = tileDict.tile_string(monster.get_number_tag())
                    self.win.blit(monster_tile, (monster.x - x_start, monster.y - y_start))
            else:
                dead_monsters.append(key)
                monster_map.clear_location(monster.x, monster.y)

        self.win.blit(tileDict.tile_string(200), (r_x * self.textSize, r_y * self.textSize))

        for key in dead_monsters:
            monsterID.subjects.pop(key)



    def update_inventory(self, player):
        font2 = pygame.font.SysFont('didot.ttc', 32)
        inv = pygame.image.load("assets/inventory.png")
        self.win.blit(inv, (128, 64))
        for i, item in enumerate(player.inventory):
            text = font2.render(item.name, True, (0,255,0))
            num = font2.render(str(i+1) + ".", True, (0,255,0))
            self.win.blit(num, (132, 128 + 32 * i))
            self.win.blit(text, (156, 128 + 32 * i))



    def update_main(self):
        main_background = pygame.image.load("assets/main_screen.png")
        main_background = pygame.transform.scale(main_background, (self.screen_width, self.screen_height))
        self.win.blit(main_background, (0,0))

        

    def update_race(self):
        race_background = pygame.image.load("assets/race_screen.png")
        race_background = pygame.transform.scale(race_background, (self.screen_width, self.screen_height))
        self.win.blit(race_background, (0,0))

    def update_class(self):
        class_background = pygame.image.load("assets/class_screen.png")
        class_background = pygame.transform.scale(class_background, (self.screen_width, self.screen_height))
        self.win.blit(class_background, (0,0))


def create_main_screen(scr):
    background = pygame.image.load("assets/homescreen.png")
    background = pygame.transform.scale(background, (scr.screen_width, scr.screen_height))
    scr.win.blit(background, (0,0))

    buttons = Buttons()
    button = Button(scr.screen_width, scr.screen_height, "assets/button.png", 15/100, 11/100, "1", scr.screen_width / 2 - scr.screen_width*15/200, scr.screen_height * 85/100)
    buttons.add(button, "Play!")
    scr.win.blit(button.img, (button.positionx, button.positiony))

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Play!', True, (255, 255, 255))
    text_width, text_height = font.size("Play!")
    scr.win.blit(text, (scr.screen_width / 2 - text_width / 2, scr.screen_height * 85/100 + button.height / 2 - text_height / 2))

    pygame.image.save(scr.win, "assets/main_screen.png")
    return buttons

def create_race_screen(scr):
    background = pygame.image.load("assets/race_background.png")
    background = pygame.transform.scale(background, (scr.screen_width, scr.screen_height))
    scr.win.blit(background, (0,0))
    buttons = Buttons()
    button = Button(scr.screen_width, scr.screen_height, "assets/button.png", 15/100, 11/100, "1", scr.screen_width / 2 - scr.screen_width*15/200, scr.screen_height * 85/100)
    buttons.add(button, "Human")
    scr.win.blit(button.img, (button.positionx, button.positiony))

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Human', True, (255, 255, 255))
    text_width, text_height = font.size("Human")
    scr.win.blit(text, (scr.screen_width / 2 - text_width / 2, scr.screen_height * 85/100 + button.height / 2 - text_height / 2))

    pygame.image.save(scr.win, "assets/race_screen.png")
    return buttons

def create_class_screen(scr):
    background = pygame.image.load("assets/class_background.png")
    background = pygame.transform.scale(background, (scr.screen_width, scr.screen_height))
    scr.win.blit(background, (0,0))
    buttons = Buttons()
    button = Button(scr.screen_width, scr.screen_height, "assets/button.png", 15/100, 11/100, "1", scr.screen_width / 2 - scr.screen_width*15/200, scr.screen_height * 85/100)
    buttons.add(button, "Warrior")
    scr.win.blit(button.img, (button.positionx, button.positiony))

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Warrior', True, (255, 255, 255))
    text_width, text_height = font.size("Warrior")
    scr.win.blit(text, (scr.screen_width / 2 - text_width / 2, scr.screen_height * 85/100 + button.height / 2 - text_height / 2))

    pygame.image.save(scr.win, "assets/class_screen.png")
    return buttons