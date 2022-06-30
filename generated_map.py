from pygame import image
import dice as R

class TileDict():
    def __init__(self, textSize, colors):
        file = 'P.png'
        player_image = image.load(file)
        basic_wall = image.load("basic_wall.png")
        tiles = {}
        tiles[0] = image.load("basic_floor.png")
        tiles[1] = basic_wall
        tiles[200] = player_image
        tiles[101] = image.load("orc.png")
        tiles[300] = image.load("basic_ax.png")
        self.tiles = tiles

    def tile_string(self, key):
        return self.tiles[key]

class Tile():
    def __init__(self, x, y, number_tag = 0, passable = False):
        self.passable = passable
        self.number_tag = number_tag
        self.x = x
        self.y = y

class DungeonGenerator():
    #Generates a width by height 2d array of tiles. Each type of tile has a unique tile
    #tag ranging from 0 to 99
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map_tile = []
        for x in range(self.width):
            self.map_tile.append([Tile(x, y, 1, False) for y in range(self.height)])
        
        rooms = R.roll_square_rooms(0, self.width, 3, 20, 0, self.height, 3, 20, 5)
        for room in rooms:
            startx = room[0]
            starty = room[1]
            length = room[2]
            depth = room[3]
            self.square_room(startx, starty, length, depth)

        rooms = R.roll_square_rooms(0, self.width, 1, 4, 0, self.height, 3, 20, 30)
        for room in rooms:
            startx = room[0]
            starty = room[1]
            length = room[2]
            depth = room[3]
            self.square_room(startx, starty, length, depth)

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
                tile = Tile(x, y, 0, True)
                self.map_tile[x][y] = tile

    def get_map(self):
        return self.map_tile

class TrackingMap():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.track_map = [x[:] for x in [[0] * self.width] * self.height]

    def place_thing(self, thing, location):
        self.track_map[location[0]][location[1]] = thing.ID

    def get_map(self):
        return self.track_map

    def location(self, x, y):
        return self.track_map[x][y]

    def clear_location(self, x, y):
        self.track_map[x][y] = 0

    def __str__(self):
        allrows = ""
        for x in range(self.width):
            row = ' '.join(str(self.track_map[x][y]) for y in range(self.height))
            allrows = allrows + row + "\n"      
        return allrows