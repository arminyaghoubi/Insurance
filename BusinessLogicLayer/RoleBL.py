from DataAccessLayer import RoleDataAccessLayer


class RoleBusinessLogic:
    def __init__(self):
        self.repository = RoleDataAccessLayer()

    def getAll(self):
        return self.repository.getAll()
