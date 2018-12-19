from PyQt5.QtWidgets import QGraphicsScene, QMessageBox
from PyQt5.Qt import QPen, Qt, QBrush
from math import floor
from StateCell import StateCell


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
        self.active_patern = []
        self.import_patern = [[0, 0]]
        self.last_x_id = None
        self.last_y_id = None

        for cell in self.board.cells:
            brush = self.active_color if cell.state == StateCell.LIFE else self.inactive_color
            self.pixels['#'+str(cell.c_x)+'#'+str(cell.c_y)] = self.addRect(self.config.size_cell*cell.c_x,self.config.size_cell*cell.c_y,self.config.size_cell,self.config.size_cell, pen, brush)

    def mousePressEvent(self, event):
        super(GolGraphicScene, self).mousePressEvent(event)
        x_id = floor(event.pos().x() / self.config.size_cell)
        y_id = floor(event.pos().y() / self.config.size_cell)
        if self.board.getcelltocoord(x_id, y_id).state == StateCell.LIFE or self.board.getcelltocoord(x_id, y_id).state == StateCell.BORN:
            self.board.getcelltocoord(x_id, y_id).state = StateCell.DEATH
            self.setInativeCell(x_id, y_id)
        else:
            self.board.getcelltocoord(x_id, y_id).state = StateCell.BORN
            self.setNewCell(x_id, y_id)

    def mouseMoveEvent(self, event):
        super(GolGraphicScene, self).mouseMoveEvent(event)
        x_id = floor(event.pos().x() / self.config.size_cell)
        y_id = floor(event.pos().y() / self.config.size_cell)
        if self.last_x_id != x_id and self.last_y_id != y_id:
            self.last_x_id = x_id
            self.last_y_id = y_id
            self.active_patern.append([x_id,y_id])


    def setActiveCell(self,x,y):
        self.pixels['#' + str(x) + '#' + str(y)].setBrush(self.active_color)

    def setInativeCell(self,x,y):
        self.pixels['#' + str(x) + '#' + str(y)].setBrush(self.inactive_color)

    def setNewCell(self,x,y):
        self.pixels['#' + str(x) + '#' + str(y)].setBrush(self.new_color)
