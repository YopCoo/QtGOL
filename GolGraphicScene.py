from PyQt5.QtWidgets import QGraphicsScene, QMessageBox
from PyQt5.Qt import QPen, Qt, QBrush
from math import floor
from StateCell import StateCell
from Cell import Cell
from copy import copy


class GolGraphicScene(QGraphicsScene):
    def __init__(self, board, config):
        super(GolGraphicScene,self).__init__()
        self.board = board
        self.config = config
        pen = QPen(Qt.black)
        self.active_color = QBrush(self.config.active_color)
        self.active_color.setStyle(Qt.SolidPattern)
        self.new_color = QBrush(self.config.new_color)
        self.active_color.setStyle(Qt.SolidPattern)
        self.inactive_color = QBrush()
        self.inactive_color.setStyle(0)
        self.pixels = {}
        self.actual_area = []
        self.import_patern = [Cell(0, 0, StateCell.BORN)]
        self.last_x_id = None
        self.last_y_id = None

        for cell in self.board.cells:
            brush = self.active_color if cell.state == StateCell.LIFE else self.inactive_color
            self.pixels['#'+str(cell.c_x)+'#'+str(cell.c_y)] = self.addRect(self.config.size_cell*cell.c_x,self.config.size_cell*cell.c_y,self.config.size_cell,self.config.size_cell, pen, brush)

    def mousePressEvent(self, event):
        super(GolGraphicScene, self).mousePressEvent(event)
        x_id = self.getPosId(event.scenePos().x())
        y_id = self.getPosId(event.scenePos().y())
        for cell in self.import_patern:
            if cell.state == StateCell.BORN:
                self.board.getcelltocoord(x_id+cell.c_x, y_id+cell.c_y).state = StateCell.BORN
                self.setNewCell(x_id+cell.c_x, y_id+cell.c_y)
            elif cell.state == StateCell.LIFE:
                self.board.getcelltocoord(x_id+cell.c_x, y_id+cell.c_y).state = StateCell.LIFE
                self.setActiveCell(x_id+cell.c_x, y_id+cell.c_y)
            elif cell.state == StateCell.DEATH:
                self.board.getcelltocoord(x_id+cell.c_x, y_id+cell.c_y).state = StateCell.DEATH
                self.setInativeCell(x_id+cell.c_x, y_id+cell.c_y)

    def mouseMoveEvent(self, event):
        super(GolGraphicScene, self).mouseMoveEvent(event)
        x_id = self.getPosId(event.scenePos().x())
        y_id = self.getPosId(event.scenePos().y())
        if self.last_x_id != x_id or self.last_y_id != y_id:
            # Restore saved Area
            if self.actual_area.__len__() != 0:
                for cell in self.actual_area:
                    if cell.state == StateCell.BORN:
                        self.setNewCell(cell.c_x, cell.c_y)
                    elif cell.state == StateCell.LIFE:
                        self.setActiveCell(cell.c_x, cell.c_y)
                    elif cell.state == StateCell.DEATH:
                        self.setInativeCell(cell.c_x, cell.c_y)
                self.actual_area.clear()
            # Save new position
            self.last_x_id = x_id
            self.last_y_id = y_id
            # Save actual area for new pattern
            for cell in self.import_patern:
                self.actual_area.append(Cell(x_id + cell.c_x, y_id + cell.c_y, self.board.getcelltocoord(x_id + cell.c_x, y_id + cell.c_y).state))
            # Show pattern
            for cell in self.import_patern:
                if cell.state == StateCell.BORN:
                    self.setNewCell(x_id+cell.c_x, y_id+cell.c_y)
                elif cell.state == StateCell.LIFE:
                    self.setActiveCell(x_id+cell.c_x, y_id+cell.c_y)
                elif cell.state == StateCell.DEATH:
                    self.setInativeCell(x_id+cell.c_x, y_id+cell.c_y)

    def getPosId(self,pos):
        return floor(pos / self.config.size_cell)

    def setActiveCell(self,x,y):
        self.pixels['#' + str(x) + '#' + str(y)].setBrush(self.active_color)

    def setInativeCell(self,x,y):
        self.pixels['#' + str(x) + '#' + str(y)].setBrush(self.inactive_color)

    def setNewCell(self,x,y):
        self.pixels['#' + str(x) + '#' + str(y)].setBrush(self.new_color)

    def refreshScene(self):
        for cell in self.board.cells:
            if cell.state == StateCell.LIFE:
                self.setActiveCell(cell.c_x,cell.c_y)
            elif cell.state == StateCell.BORN:
                self.setNewCell(cell.c_x,cell.c_y)
            elif cell.state == StateCell.DEATH:
                self.setInativeCell(cell.c_x, cell.c_y)

    def clean(self):
        for cell in self.board.cells:
            cell.state = StateCell.DEATH
            self.setInativeCell(cell.c_x, cell.c_y)
