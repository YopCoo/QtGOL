from data.DbConnection import DbConnection
from model.PatternCategorie import PatternCategorie
from util.Log import Log

logger = Log().getLogger(__name__)


class DaoPattern:

    def __init__(self):
        self.conn = DbConnection().getConnection()

    def getNamesByCategory(self, categorie):
        cur = self.conn.cursor()
        qry = "select PATTERN_NAME.NAME from pattern_name inner join PATTERN_CATEGORY on PATTERN_NAME.CATEGORY = PATTERN_CATEGORY.ID where PATTERN_CATEGORY.CATEGORY='"+categorie+"';"
        logger.debug("getNamesByCategory query : " + qry)
        cur.execute(qry)
        list = cur.fetchall()
        cur.close()
        self.conn.close()
        if list.__len__() == 0:
            raise Exception("No patterns for this category.")
        return list

    def getId(self, id):
        pass

    def PatternByName(self, name):
        pass
