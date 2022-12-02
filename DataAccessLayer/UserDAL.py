from DataAccessLayer import BaseAccessLayer
from Model import *


class UserDataAccessLayer(BaseAccessLayer):
    def Insert(self, newUser: User):
        return super().execute(
            "InsertUser @UserName=?,@Password=?,@RoleName=?",
            (newUser.UserName, newUser.Password, newUser.RoleName))

    def GetUser(self, username, password):
        return super().getFirstEntity("GetUser @UserName=?,@Password=?", (username, password))
