from Cell import Cell
from StateCell import StateCell


class PatternFactory():
    def __init__(self):
        self.staticPatterns = {}
        self.staticPattern_db= open("staticPattern.ini", "r")
        self.fillDict(self.staticPattern_db,self.staticPatterns)
        self.periodicPatterns = {}
        self.periodicPattern_db = open("periodicPattern.ini", "r")
        self.fillDict(self.periodicPattern_db, self.periodicPatterns)
        self.movingPatterns = {}
        self.movingPattern_db = open("movingPattern.ini", "r")
        self.fillDict(self.movingPattern_db, self.movingPatterns)

    def fillDict(self,file,dict):
        for line in file:
            key = line.split("|")[0].strip()
            val = line.split("|")[1].strip().split(":")
            pattern = []
            for cell in val:
                state = None
                if int(cell.split(",")[2].strip()) == 0:
                    state = StateCell.DEATH
                elif int(cell.split(",")[2].strip()) == 1:
                    state = StateCell.BORN
                elif int(cell.split(",")[2].strip()) == 2:
                    state = StateCell.LIFE
                pattern.append(Cell(int(cell.split(",")[0].strip()), int(cell.split(",")[1].strip()), state))
                dict[key] = pattern.copy()
