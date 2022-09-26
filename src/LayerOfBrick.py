class LayerOfBrick:
    def __init__(self):
        self.layer = {}

    def getAllBrick(self):
        return self.layer.items()

    def getBrickByIndex(self, index):
        return self.layer[f'{index}']
