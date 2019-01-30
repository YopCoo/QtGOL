from data.DaoUserContext import DaoUserContext
from util.Log import Log

logger = Log().getLogger(__name__)


class ServiceUserContext:

    def __init__(self):
        self.daoUserContext = DaoUserContext()

    def getUserContext(self, id):
        return self.daoUserContext.getUserContext(id)
