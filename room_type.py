from define import *

# stage 1
start_01 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]


s1_1 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, None, None, None, FLY, None, None, None, None, None,FLY, None, None, None, WALL],
            [WALL, None, ROCK, ROCK, None, FLY, None, None, None, FLY,None, ROCK, ROCK, None, WALL],
            [WALL, None, ROCK, ROCK, FLY, None, FLY, None, FLY, None,FLY, ROCK, ROCK, None, WALL],
            [DOOR_NORMAL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, ROCK, ROCK, None, None, None, None, None, None,None, ROCK, ROCK, None, WALL],
            [WALL, None, ROCK, ROCK, None, None, None, None, None, None,None, ROCK, ROCK, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

s1_2 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
            [WALL, ROCK, ROCK, CHARGER, None, None, None, None, None, None, None, None, None, None, WALL],
            [WALL, ROCK, ROCK, JAR ,None, None, None, None, None, None, None, None, None, None, WALL],
            [WALL, ROCK, ROCK, CHARGER, None, None, None, None, None, None, None, None, None, None, WALL],
            [WALL, ROCK, ROCK, JAR, None, None, None, None, None, None, None, None, None, None, DOOR_NORMAL],
            [WALL, ROCK, ROCK, CHARGER, None, None, None, None, None, None, None, None, None, None, WALL],
            [WALL, ROCK, ROCK, JAR, None, None, None, None, None, None, None, None, None, None, WALL],
            [WALL, ROCK, ROCK, CHARGER, None, None, None, None, None, None, None, None, None, None, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]]

s1_3 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, POOP, FLY, FLY, None, None, None, None, None, None,None, FLY, FLY, POOP, WALL],
            [WALL, ROCK, ROCK, ROCK, None, None, None, None, None, None,None, ROCK, ROCK, ROCK, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, SPIKE, None, None,None, None, None, None, DOOR_NORMAL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, ROCK, ROCK, ROCK, None, None, None, None, None, None,None, ROCK, ROCK, ROCK, WALL],
            [WALL, POOP, FLY, FLY, None, None, None, None, None, None,None, FLY, FLY, POOP, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

s1_4 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_BOSS, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, MEAT, None, None, None, MEAT,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, ROCK, None, None,None, None, None, None, WALL],
            [DOOR_NORMAL, None, None, None, None, ROCK, ROCK, ROCK, ROCK, ROCK,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, ROCK, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, MEAT, None, None, None, MEAT,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

s1_boss = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, DOOR_TRAP, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, BABY_PLUM, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_BOSS, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

start_02 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [DOOR_NORMAL, None, None, None, None, None, None, None, None, None,None, None, None, None, DOOR_NORMAL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

s2_1 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, None, None, None, None, None, ROCK, ROCK, ROCK, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, ROCK, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, POOP, None, None,None, None, None, None, WALL],
            [DOOR_NORMAL, None, None, None, None, None, POOP, None, None, None,None, None, None, None, DOOR_NORMAL],
            [WALL, None, None, None, None, None, None, POOP, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, ROCK, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, ROCK, ROCK, ROCK, None,None, None, None, None, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

s2_2 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, SPIKE, None, None,None, FLY, FLY, None, WALL],
            [WALL, None, None, None, None, None, SPIKE, SPIKE, SPIKE, None,None, None, None, None, WALL],
            [DOOR_NORMAL, None, None, None, None, SPIKE, SPIKE, SPIKE, SPIKE, SPIKE,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, SPIKE, SPIKE, SPIKE, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, SPIKE, None, None,None, FLY, FLY, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

s2_3 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, MEAT, None, ROCK, None, CHARGER,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, ROCK, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, ROCK, ROCK, ROCK, ROCK, ROCK,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, ROCK, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, CHARGER, None, ROCK, None, MEAT,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

s2_4 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, None, CHARGER, None, CHARGER, None, None, None, FLY,JAR,JAR,JAR,JAR, WALL],
            [WALL, None, None, None, None, None, None, None, FLY, None,JAR,JAR,JAR,JAR, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None,JAR,JAR,JAR, WALL],
            [DOOR_BOSS, None, None, None, None, None, None, None, None, None,None,JAR,JAR,JAR, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None,JAR,JAR, WALL],
            [WALL, None, MEAT, None, MEAT, None, None, None, None, None,None, None,JAR,JAR, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None,JAR, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

s2_5 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, POOP, POOP, POOP, POOP, POOP, POOP, POOP, POOP, POOP,POOP, POOP, POOP, POOP, WALL],
            [WALL, POOP, POOP, POOP, POOP, POOP, POOP, POOP, POOP, POOP,POOP, POOP, POOP, SPIKE, WALL],
            [WALL, POOP, POOP, POOP, POOP, POOP, POOP, POOP, POOP, POOP,POOP, POOP, SPIKE, None, WALL],
            [WALL, POOP, POOP, POOP, POOP, POOP, POOP, POOP, POOP, POOP,POOP, SPIKE, None, None, DOOR_NORMAL],
            [WALL, POOP, POOP, POOP, POOP, POOP, POOP, POOP, POOP, POOP,POOP, POOP, SPIKE, None, WALL],
            [WALL, POOP, POOP, POOP, POOP, POOP, POOP, POOP, POOP, POOP,POOP, POOP, POOP, SPIKE, WALL],
            [WALL, POOP, POOP, POOP, POOP, POOP, POOP, POOP, POOP, POOP,POOP, POOP, POOP, POOP, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

s2_boss = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, HEADLESS_HEAD, None, None, None, DOOR_TRAP, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, DOOR_BOSS],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, HEADLESS_BODY, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

# Stage 1
stage_01 = [[None, None, None, None, None],
            [None, None, None, s1_boss, None],
            [None, None, s1_3, s1_4, None],
            [None, s1_2, s1_1, None, None],
            [None, None, start_01, None, None]]

stage_02 = [[None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, s2_boss, s2_4],
            [None, None, None, None, s2_3],
            [None, s2_5, start_02, s2_1, s2_2]]