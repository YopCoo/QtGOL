from data.DbConnection import DbConnection
from model.Cell import Cell
from model.StateCell import StateCell
from util.Log import Log

logger = Log().getLogger(__name__)

class DaoPattern(DbConnection):



    def getNamesByCategory(self, categorie):
        cur = self.getConnection().cursor()
        qry = "select PATTERN_NAME.ID,PATTERN_NAME.NAME from pattern_name inner join PATTERN_CATEGORY on PATTERN_NAME.CATEGORY = PATTERN_CATEGORY.ID where PATTERN_CATEGORY.CATEGORY='"+categorie+"';"
        logger.debug("getNamesByCategory query : " + qry)
        cur.execute(qry)
        list = cur.fetchall()
        cur.close()
        self.closeConnection()
        if list.__len__() == 0:
            raise Exception("No patterns for this category.")
        return list

    def getId(self, id):
        cur = self.getConnection().cursor()
        pattern =[]
        qry = "select CX,CY,STATE from PATTERN_CELL where PATTERN_CELL.NAME=" + str(id) + ";"
        logger.debug("getNamesByCategory query : " + qry)
        cur.execute(qry)
        list = cur.fetchall()
        cur.close()
        self.closeConnection()
        if list.__len__() == 0:
            raise Exception("No patterns for this category.")
        else:
            for cx, cy, state in list:
                stateCell = None
                if state == 0:
                    stateCell = StateCell.DEATH
                elif state == 1:
                    stateCell = StateCell.BORN
                elif state == 2:
                    stateCell = StateCell.LIFE
                pattern.append(Cell(cx, cy, stateCell))
        return pattern

    def PatternByName(self, name):
        pass
