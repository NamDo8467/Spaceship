from collections import deque
from src.Brick import Brick
from src.Colors import colors
from random import randrange


class Wall:
    __color_list = list(colors.values())
    __number_of_colors = 6

    def __init__(self):
        self.queue = deque()

        for i in range(0, 440, 20):  # range(start=0, stop=440 (not included), step=20)
            brick = Brick(i, 0, self.__color_list[randrange(0, self.__number_of_colors - 1)])
            self.queue.append(brick)
