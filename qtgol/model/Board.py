from qtgol.model.Cell import Cell
from random import random
from qtgol.model.Generator import Generator
from qtgol.model.StateCell import StateCell

class Board:

    LIFE =  [0,0,1,1,0,0,0,0,0,0]
    DEATH = [0,0,0,1,0,0,0,0,0,0]

    def __init__(self, size_x, size_y, density=0.7, init=Generator.Random):
        self.SIZE_X = size_x
        self.SIZE_Y = size_y
        self.cells = []
        self.init = init
        self.density = density

        for x in range(self.SIZE_X):
            for y in range(self.SIZE_Y):
                cell = None
                if self.init == Generator.Random:
                    cell = Cell(x, y, StateCell.BORN if random() < self.density else StateCell.DEATH)
                if self.init == Generator.Blank:
                    cell = Cell(x, y, StateCell.DEATH)
                self.cells.append(cell)

        for cell in self.cells:
                cell.loadneighbours(self)

    def neighbour(self, cell):
        return list(filter(lambda c: c.state == StateCell.BORN or c.state == StateCell.LIFE, cell.neighbours)).__len__()

    def getcelltocoord(self, x, y):
        return list(filter(lambda c: c.c_x == x and c.c_y == y, self.cells)).__getitem__(0)

    def nextgen(self):
        for cell in self.cells:
            if cell.state == StateCell.LIFE or cell.state == StateCell.BORN:
                cell.nextState = StateCell.LIFE if self.LIFE[cell.cells_in_life()] == 1 else StateCell.DEATH
            else:
                cell.nextState = StateCell.BORN if self.DEATH[cell.cells_in_life()] == 1 else StateCell.DEATH

        for cell in self.cells:
            cell.state = cell.nextState

    def autogen(self):
        for cell in self.cells:
            if random() < self.density :
                cell.state = StateCell.BORN
            else:
                cell.state = StateCell.DEATH


    def __str__(self):
        str = ""
        for x in range(self.SIZE_X):
            for y in range(self.SIZE_Y):
                str = str + list(filter(lambda c: c.c_x == x and c.c_y == y , self.cells)).__getitem__(0).__str__()
            str = str + "\n"
        return str
