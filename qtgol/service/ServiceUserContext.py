from qtgol.data.DaoUserContext import DaoUserContext
from qtgol.util.Log import Log

logger = Log().getLogger(__name__)


class ServiceUserContext:

    def __init__(self):
        self.daoUserContext = DaoUserContext()

    def getUserContext(self, id):
        return self.daoUserContext.getUserContext(id)

    def getLastUserContext(self):
        if self.daoUserContext.isExistUserContextId("LAST_CONFIG"):
            return self.getUserContext("LAST_CONFIG")
        else:
            return self.getUserContext("DEFAUT")

    def saveOrUpdateUserContext(self,config,id):
        self.daoUserContext.saveOrUpdateUserContext(config,id)

    def deleteUserContext(self,id):
        self.daoUserContext.deleteUserContext(id)
