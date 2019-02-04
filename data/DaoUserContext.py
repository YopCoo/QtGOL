from util.Log import Log
from data.DbConnection import DbConnection
from model.UserContext import UserContext
from PyQt5.Qt import QColor

logger = Log().getLogger(__name__)


class DaoUserContext(DbConnection):

    def getUserContext(self, id):
        cur = self.getConnection().cursor()
        qry = "select * from config where id='"+id+"';"
        logger.debug(qry)
        cur.execute(qry)
        cr=cur.fetchone()
        if cr is None:
            return None
        else:
            inactive_color = QColor.fromRgb(cr[6], cr[7], cr[8])
            active_color = QColor.fromRgb(cr[9], cr[10], cr[11])
            new_color = QColor.fromRgb(cr[12], cr[13], cr[14])
            uc = UserContext(cr[1], cr[2], cr[3], cr[4], cr[5], inactive_color, active_color, new_color)
            logger.info("Loading User context")
            logger.info("User context : "+uc.__str__())
        cur.close()
        self.closeConnection()
        return uc

    def isExistUserContextId(self, id):
        cur = self.getConnection().cursor()
        qry = "select count(*) from config where id='"+id+"';"
        cur.execute(qry)
        res = cur.fetchone()[0]
        if res == 1:
            return True
        else:
            return False

    def saveOrUpdateUserContext(self,config,id):
        if self.isExistUserContextId(id):
            self.updateUserContext(config,id)
        else:
            self.saveUserContext(config,id)

    def saveUserContext(self,config,id):
        cur = self.getConnection().cursor()
        qry = "INSERT INTO CONFIG VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"
        cur.execute(qry, (id, str(config.x_cell),
                          str(config.y_cell),
                          str(config.size_cell),
                          str(config.density),
                          str(config.speed),
                          str(config.inactive_color.red()),
                          str(config.inactive_color.green()),
                          str(config.inactive_color.blue()),
                          str(config.active_color.red()),
                          str(config.active_color.green()),
                          str(config.active_color.blue()),
                          str(config.new_color.red()),
                          str(config.new_color.green()),
                          str(config.new_color.blue())))
        logger.debug(cur.__str__())
        cur.connection.commit()
        cur.close()
        self.closeConnection()

    def updateUserContext(self,config,id):
        cur = self.getConnection().cursor()
        qry = "UPDATE CONFIG SET " \
              "XCELL = ? , YCELL = ? , SIZECELL = ? , DENSITY = ? , SPEED = ?, " \
              "INACTIVE_COLOR_R = ?, INACTIVE_COLOR_G = ?, INACTIVE_COLOR_B = ?, " \
              "ACTIVE_COLOR_R = ?, ACTIVE_COLOR_G = ?, ACTIVE_COLOR_B = ?," \
              "NEW_COLOR_R = ?, NEW_COLOR_G = ?, NEW_COLOR_B = ? WHERE ID = ?;"
        cur.execute(qry, (str(config.x_cell),
                          str(config.y_cell),
                          str(config.size_cell),
                          str(config.density),
                          str(config.speed),
                          str(config.inactive_color.red()),
                          str(config.inactive_color.green()),
                          str(config.inactive_color.blue()),
                          str(config.active_color.red()),
                          str(config.active_color.green()),
                          str(config.active_color.blue()),
                          str(config.new_color.red()),
                          str(config.new_color.green()),
                          str(config.new_color.blue()),
                          id))
        logger.debug(cur.__str__())
        cur.connection.commit()
        cur.close()
        self.closeConnection()

    def deleteUserContext(self,id):
        cur = self.getConnection().cursor()
        qry = "DELETE FROM CONFIG WHERE ID='"+id+"';"
        cur.execute(qry)
        cur.connection.commit()
        cur.close()
        self.closeConnection()
