from PyQt5.QtWidgets import QGraphicsScene, QMessageBox


class GolGraphicScene(QGraphicsScene):
    def __init__(self, board):
        super(GolGraphicScene,self).__init__()
        self.board = board

    def mousePressEvent(self, event):
        super(GolGraphicScene, self).mousePressEvent(event)
        msgBox = QMessageBox()
        msgBox.setText("Question?")
        msgBox.setInformativeText("Pos X : "+str(event.pos().x())+ " - Pos Y :"+str(event.pos().y()))
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.exec_()

