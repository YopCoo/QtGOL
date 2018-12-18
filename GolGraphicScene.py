from PyQt5.QtWidgets import QGraphicsScene, QMessageBox
from PyQt5.Qt import QPen, Qt, QBrush, QColor


class GolGraphicScene(QGraphicsScene):
    def __init__(self, board, config):
        super(GolGraphicScene,self).__init__()
        self.board = board
        pen = QPen(Qt.black)
        self.active_color = QBrush(config.active_color)
        self.active_color.setStyle(Qt.SolidPattern)
        self.inactive_color = QBrush()
        self.inactive_color.setStyle(0)
        self.pixels = {}
        for cell in self.board.cells:
            brush = self.active_color if cell.state else self.inactive_color
            self.pixels['#'+str(cell.c_x)+'#'+str(cell.c_y)] = self.addRect(config.size_cell*cell.c_x,config.size_cell*cell.c_y,config.size_cell,config.size_cell, pen, brush)

    def mousePressEvent(self, event):
        super(GolGraphicScene, self).mousePressEvent(event)
        msgBox = QMessageBox()
        msgBox.setText("Information")
        msgBox.setInformativeText("Pos X : "+str(event.pos().x())+ " - Pos Y :"+str(event.pos().y()))
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def setActiveCell(self,x,y):
        self.pixels['#' + str(x) + '#' + str(y)].setBrush(self.active_color)

    def setInativeCell(self,x,y):
        self.pixels['#' + str(x) + '#' + str(y)].setBrush(self.inactive_color)

