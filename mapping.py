from pygame import image
import dice as R
import objects as O

class TileDict():
    def __init__(self, textSize, colors):
        file = 'assets/P.png'
        player_image = image.load(file)
        basic_wall = image.load("assets/basic_wall.png")
        tiles = {}
        tiles[0] = image.load("assets/basic_floor.png")
        tiles[1] = basic_wall
        tiles[200] = player_image
        tiles[101] = image.load("assets/orc.png")
        tiles[300] = image.load("assets/basic_ax.png")
        self.tiles = tiles

    def tile_string(self, key):
        return self.tiles[key]

class DungeonGenerator():
    #Generates a width by height 2d array of tiles. Each type of tile has a unique tile
    #tag ranging from 0 to 99
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map_tile = []
        for x in range(self.width):
            self.map_tile.append([O.Tile(x, y, 1, False) for y in range(self.height)])
        
        rooms = R.roll_square_rooms(0, self.width, 3, 20, 0, self.height, 3, 20, 5)
        for room in rooms:
            startx = room[0]
            starty = room[1]
            length = room[2]
            depth = room[3]
            self.square_room(startx, starty, length, depth)

        rooms = R.roll_square_rooms(0, self.width, 1, 4, 0, self.height, 3, 20, 30)
        for room in rooms:
            startx1 = room[0]
            starty2 = room[1]
            length = room[2]
            depth = room[3]
            self.square_room(startx, starty, length, depth)
        
 #       self.square_room(startx, starty, startx1 - startx, 1)

        rooms = R.roll_square_rooms(0, self.width, 3, 20, 0, self.height, 1, 4, 30)
        for room in rooms:
            startx = room[0]
            starty = room[1]
            length = room[2]
            depth = room[3]
            self.square_room(startx, starty, length, depth)


    def square_room(self, startx, starty, length, depth):
        for x in range(length):
            for y in range(depth):
                if startx + x >= 0 and startx + x < self.width and starty+y >= 0 and starty + y < self.height:
                    tile = O.Tile(startx + x, starty + y, 0, True)
                    self.map_tile[startx + x][starty + y] = tile

    def get_map(self):
        return self.map_tile

class Maps():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.track_map = [x[:] for x in [[0] * self.width] * self.height]

    def locate(self, x, y):
        return self.track_map[x][y]

class TrackingMap(Maps):
    def __init__(self, width, height):
        super().__init__(width, height)

    def place_thing(self, thing):
        self.track_map[thing.x][thing.y] = thing.id_tag

    def clear_location(self, x, y):
        self.track_map[x][y] = 0

    def __str__(self):
        allrows = ""
        for x in range(self.width):
            row = ' '.join(str(self.track_map[x][y]) for y in range(self.height))
            allrows = allrows + row + "\n"      
        return allrows


class TileMap(TrackingMap):
    def __init__(self, width, height, generated_map):
        super().__init__(width, height)
        self.tile_map = generated_map

    def get_tag(self, x, y):
        return self.tile_map[x][y].render_tag

    def place_tile(self, tile):
        self.tile_map[tile.x][tile.y] = tile

    def get_passable(self, x, y, monster_map):
        if ((x>=0) & (y>=0) & (x < self.width) & (y < self.height)):
            return (self.tile_map[x][y].passable)# & (monster_map.locate(x,y) == 0))
        else:
            return False