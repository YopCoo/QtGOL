from qtgol.model.StateCell import StateCell


class Cell:
    def __init__(self, c_x, c_y, state):
        self.c_x = c_x
        self.c_y = c_y
        self.state = state
        self.nextState = StateCell.DEATH
        self.neighbours = []

    def __str__(self):
        if self.state:
            return " # "
        else:
            return " - "

    def loadneighbours(self, board):
        self.neighbours.extend(list(filter(lambda c: (c.c_x in [self.c_x-1, self.c_x, self.c_x+1]) and (c.c_y in [self.c_y-1, self.c_y, self.c_y+1]),board.cells)))

    def cells_in_life(self):
        living = list(filter(lambda c: c.state == StateCell.LIFE or c.state == StateCell.BORN, self.neighbours)).__len__()
        return (living - 1) if self.state == StateCell.LIFE or self.state == StateCell.BORN else living
