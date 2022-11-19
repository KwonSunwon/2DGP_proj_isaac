from define import *

# Room types
# start room
start = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

type_02 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, ROCK, ROCK,JAR,JAR, None, None, None, FLY,None, ROCK, ROCK, None, WALL],
            [WALL, None, ROCK, ROCK,JAR,JAR, None, None, None, None,FLY, ROCK, ROCK, None, WALL],
            [DOOR_NORMAL, None, None, None, None, None, None, None, None, None,None, None, None, None, DOOR_BOSS],
            [WALL, None, ROCK, ROCK, None, None, None, None, None, None,None, ROCK, ROCK, None, WALL],
            [WALL, None, ROCK, ROCK, None, None, None, None, None, None,None, ROCK, ROCK, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_TREASURE, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

type_03 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, ROCK, ROCK,None, FLY, None, None, None, FLY,None, ROCK, ROCK, None, WALL],
            [WALL, None, ROCK, ROCK,FLY,None, None, None, None, None,FLY, ROCK, ROCK, None, WALL],
            [DOOR_NORMAL, None, None, None, None, None, None, None, None, None,None, None, None, None, DOOR_BOSS],
            [WALL, None, ROCK, ROCK, None, None, None, None, None, None,None, ROCK, ROCK, None, WALL],
            [WALL, None, ROCK, ROCK, None, None, None, None, None, None,None, ROCK, ROCK, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_TREASURE, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

type_04 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,CHARGER, None, None, None, WALL],
            [WALL, ROCK, ROCK, ROCK, None, None, None, None, None, None,None, ROCK, ROCK, ROCK, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [DOOR_NORMAL, None, None, None, None, None, None, None, None, None,None, None, None, None, DOOR_NORMAL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, ROCK, ROCK, ROCK, None, None, None, None, None, None,None, ROCK, ROCK, ROCK, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

type_05 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_BOSS, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, CHARGER, None, None, None, None, None, None, None,None, None, CHARGER, None, WALL],
            [WALL, None, None, None, None, None, None, ROCK, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, ROCK, ROCK, ROCK, ROCK, ROCK,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, ROCK, None, None,None, None, None, None, WALL],
            [WALL, None, CHARGER, None, None, None, None, None, None, None,None, None, CHARGER, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

type_06 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, FLY, FLY, None, None, None, None, None, None,None, FLY, FLY, None, WALL],
            [WALL, None, FLY, FLY, None, None, None, None, None, None,None, FLY, FLY, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

type_07 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, JAR, JAR, None, None, None, None, None, None, None,None, None, JAR, JAR, WALL],
            [WALL, JAR, JAR, None, MEAT, None, None, None, None, None,None, None, JAR, JAR, WALL],
            [WALL, JAR, JAR, None, None, None, None, None, None, None,None, None, JAR, JAR, WALL],
            [WALL, JAR, JAR, None, None, None, None, None, None, None,None, None, JAR, JAR, WALL],
            [WALL, JAR, JAR, None, None, None, None, None, None, None,None, None, JAR, JAR, WALL],
            [WALL, JAR, JAR, None, None, None, None, None, None, None,None, None, JAR, JAR, WALL],
            [WALL, JAR, JAR, None, None, None, None, None, None, None,None, None, JAR, JAR, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

type_boss = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, DOOR_TRAP, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_BOSS, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

type_08 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, POOP, None, SPIKE, None, ROCK, None, JAR, None,None, None, None, None, WALL],
            [WALL, None, POOP, None, SPIKE, None, ROCK, None, JAR, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, DOOR_TREASURE],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

treasure =[[WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [DOOR_TREASURE, None, None, None, None, None, None, TABLE, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

# Stage 1
stage_01 = [[None, None, type_boss, None, None],
            [None, None, type_05, None, None],
            [None, None, type_07, None, None],
            [None, None, type_06, None, None],
            [None, None, type_08, treasure, None]]