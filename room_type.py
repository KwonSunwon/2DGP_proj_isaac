BASEMENT, CAVES = 0, 1
WALL = 20
DOOR_NORMAL = 21
DOOR_TREASURE = 22
DOOR_BOSS = 23
DOOR_TRAP = 24
ROCK = 30
JAR = 31
SPIKE = 32
POOP = 33

# start room
type_01 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [DOOR_NORMAL, None, None, None, None, None, None, None, None, None,None, None, None, None, DOOR_BOSS],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_TREASURE, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

type_02 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, ROCK, ROCK, None, None, None, None, None, None,None, ROCK, ROCK, None, WALL],
            [WALL, None, ROCK, ROCK, None, None, JAR, JAR, JAR, None,None, ROCK, ROCK, None, WALL],
            [DOOR_NORMAL, None, None, None, None, None, JAR, JAR, JAR, None,None, None, None, None, DOOR_BOSS],
            [WALL, None, ROCK, ROCK, None, None, JAR, JAR, JAR, None,None, ROCK, ROCK, None, WALL],
            [WALL, None, ROCK, ROCK, None, None, None, None, None, None,None, ROCK, ROCK, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_TREASURE, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]