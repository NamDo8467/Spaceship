from src.Brick import Brick


class LayerOfBrick:
    def __init__(self):
        self.__color_list = None
        self.layer = {}

    def addBrick(self, brick):
        self.layer[f'{brick.x}'] = brick

    def getAllIndexAndBricks(self):
        return self.layer.items()

    def getAllBricks(self):
        return self.layer.values()

    def getBrickByIndex(self, index):
        return self.layer[f'{index}']

    def removeBrick(self, x, y):
        empty_brick = None
        self.layer[f'{x}'] = empty_brick
