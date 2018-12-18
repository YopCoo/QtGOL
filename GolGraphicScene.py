from PyQt5.QtWidgets import QGraphicsScene, QMessageBox
from PyQt5.Qt import QPen, Qt, QBrush
from math import floor


class GolGraphicScene(QGraphicsScene):
    def __init__(self, board, config):
        super(GolGraphicScene,self).__init__()
        self.board = board
        self.config = config
        pen = QPen(Qt.black)
        self.active_color = QBrush(self.config.active_color)
        self.active_color.setStyle(Qt.SolidPattern)
        self.inactive_color = QBrush()
        self.inactive_color.setStyle(0)
        self.pixels = {}
        for cell in self.board.cells:
            brush = self.active_color if cell.state else self.inactive_color
            self.pixels['#'+str(cell.c_x)+'#'+str(cell.c_y)] = self.addRect(self.config.size_cell*cell.c_x,self.config.size_cell*cell.c_y,self.config.size_cell,self.config.size_cell, pen, brush)

    def mousePressEvent(self, event):
        super(GolGraphicScene, self).mousePressEvent(event)
        x_id = floor(event.pos().x() / self.config.size_cell)
        y_id = floor(event.pos().y() / self.config.size_cell)
        if self.board.getcelltocoord(x_id, y_id).state:
            self.board.getcelltocoord(x_id, y_id).state = False
            self.setInativeCell(x_id, y_id)
        else:
            self.board.getcelltocoord(x_id, y_id).state = True
            self.setActiveCell(x_id, y_id)


    def setActiveCell(self,x,y):
        self.pixels['#' + str(x) + '#' + str(y)].setBrush(self.active_color)

    def setInativeCell(self,x,y):
        self.pixels['#' + str(x) + '#' + str(y)].setBrush(self.inactive_color)

