import sqlite3
from pathlib import Path
from qtgol.util.Log import Log

logger = Log().getLogger(__name__)


class DbConnection:
    def __init__(self):
        logger.debug("Ouverture connection à la base de donnée.")
        self.db_file = Path("qtgol/gol.db")
        logger.debug("chemin BDD : " + str(self.db_file.absolute()))
        self.script = Path("qtgol/INIT_DB_STRUCT.sql")
        logger.debug("chemin script init BDD : " + str(self.script.absolute()))
        self.conn = None

    def getConnection(self):
        if self.db_file.is_file():
            logger.debug("Retour conection BDD")
            self.conn = sqlite3.connect(self.db_file.absolute())
        else:
            logger.info("Creation base de donnée depuis : " + str(self.script.absolute()))
            file = open(self.script.absolute(),"r").read()
            self.conn = sqlite3.connect(self.db_file.absolute())
            cur = self.conn.cursor()
            for stm in file.split(';'):
                logger.debug("requete : "+stm)
                cur.execute(stm)
            self.conn.commit()
            cur.close()
        return self.conn

    def closeConnection(self):
        self.conn.close()
