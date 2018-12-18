from Cell import Cell
from random import random
from Generator import Generator

class Board:

    LIFE =  [0,0,1,1,0,0,0,0,0,0]
    DEATH = [0,0,0,1,0,0,0,0,0,0]

    def __init__(self, size_x, size_y, tolerance=0.7, init=Generator.Random):
        self.SIZE_X = size_x
        self.SIZE_Y = size_y
        self.cells = []
        self.init = init

        for x in range(self.SIZE_X):
            for y in range(self.SIZE_Y):
                if self.init == Generator.Random:
                    cell = Cell(x, y, random() < tolerance)
                if self.init == Generator.Blank:
                    cell = Cell(x, y, False)
                self.cells.append(cell)

        for cell in self.cells:
                cell.loadneighbours(self)

    def neighbour(self, cell):
        return list(filter(lambda c: c.state, cell.neighbours)).__len__()

    def getcelltocoord(self, x, y):
        return list(filter(lambda c: c.c_x == x and c.c_y == y, self.cells)).__getitem__(0)

    def nextgen(self):
        for cell in self.cells:
            if cell.state:
                cell.nextState = self.LIFE[cell.cells_in_life()] == 1
            else:
                cell.nextState = self.DEATH[cell.cells_in_life()] == 1

        for cell in self.cells:
            cell.state = cell.nextState


    def __str__(self):
        str = ""
        for x in range(self.SIZE_X):
            for y in range(self.SIZE_Y):
                str = str + list(filter(lambda c: c.c_x == x and c.c_y == y , self.cells)).__getitem__(0).__str__()
            str = str + "\n"
        return str
