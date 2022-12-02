from DataAccessLayer import UserDataAccessLayer
from Model import User


class UserBusinessLogic:
    def __init__(self):
        self.repository = UserDataAccessLayer()

    def Insert(self, newUser: User):
        return self.repository.Insert(newUser)

    def GetUser(self, username, password):
        return self.repository.GetUser(username,password)