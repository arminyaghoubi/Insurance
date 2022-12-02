from DataAccessLayer import BaseAccessLayer


class RoleDataAccessLayer(BaseAccessLayer):
    def getAll(self):
        result = []
        data = super().getAllEntity("Select ID,RoleName from Role")
        for item in data:
            result.append(item[1])
        return result
