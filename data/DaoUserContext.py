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
            raise Exception("No data for User Context from id : "+id)
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
