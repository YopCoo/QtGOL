import unittest
from qtgol.data.DaoUserContext import DaoUserContext


class DaoUserContextTest(unittest.TestCase):
    service = DaoUserContext()

    def isExiste(self):
        assert(self.service.isExistUserContextId("DEFAUT"))
