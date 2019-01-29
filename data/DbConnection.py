import sqlite3
from pathlib import Path
from util.Log import Log

logger = Log().getLogger(__name__)

class DbConnection:
    def __init__(self):
        logger.debug("Ouverture connection à la base de donnée.")
        self.db_file = Path("gol.db")
        logger.debug("chemin BDD : " + str(self.db_file.absolute()))
        self.script = Path("INIT_DB_STRUCT.sql")
        logger.debug("chemin script init BDD : " + str(self.script.absolute()))

    def getConnection(self):
        if self.db_file.is_file():
            logger.debug("Retour conection BDD")
            return sqlite3.connect(self.db_file.absolute())
        else:
            logger.info("Creation base de donnée depuis : " + str(self.script.absolute()))
            file = open(self.script.absolute(),"r").read()
            conn = sqlite3.connect(self.db_file.absolute())
            cur = conn.cursor()
            for stm in file.split(';'):
                logger.debug("requete : "+stm)
                cur.execute(stm)
            conn.commit()
            cur.close()
            logger.debug("Retour conection BDD")
            return conn

