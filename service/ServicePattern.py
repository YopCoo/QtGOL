from data.DaoPattern import DaoPattern

class ServicePattern:
    def __init__(self):
        self.dao = DaoPattern()
    def getNamesByCategory(self, categorie):
        return self.dao.getNamesByCategory(categorie)
    def getPatternById(self,id):
        return self.dao.getId(id)
    def getPatternByName(self,name):
        pattern = self.dao.PatternByName(name)
        if pattern.__lenll() == 1:
            return pattern
