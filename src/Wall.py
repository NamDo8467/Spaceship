from collections import deque
from src.Brick import Brick
from src.Colors import colors
from random import randrange
from src.LayerOfBrick import LayerOfBrick


class Wall:
    __color_list = list(colors.values())
    __number_of_colors = 6
    __distance_between_layer = -10

    def __init__(self):
        self.queue = deque()
        self.firstLayer = LayerOfBrick()
        for i in range(0, 440, 20):  # range(start=0, stop=440 (not included), step=20)
            brick = Brick(i, 0, self.__color_list[randrange(0, self.__number_of_colors - 1)])
            self.firstLayer.addBrick(brick)
        self.queue.append(self.firstLayer)

    def addLayerOfBricks(self):
        for layer in self.queue:
            for brick in layer.getAllBricks():
                if brick is not None:
                    if brick.y == 410 or brick.y > 410:  # 410 is the Y-coordinate that hits the spaceship which will make the game stops
                        return
                    brick.y += 1

        new_layer = LayerOfBrick()
        for i in range(0, 440, 20):  # range(start=0, stop=440 (not included), step=20)
            brick = Brick(i, self.__distance_between_layer, self.__color_list[randrange(0, self.__number_of_colors - 1)])
            new_layer.addBrick(brick)
        self.queue.append(new_layer)
        self.__distance_between_layer -= 10
