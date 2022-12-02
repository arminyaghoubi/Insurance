from Model.UserModel import User


class Pharmacy(User):
    def __init__(self, username=None, password=None, roleName=None, pharmacyName=None, gln=None, address=None,
                 phone=None):
        super().__init__(username, password, roleName)
        self.PharmacyName = pharmacyName
        self.GLN = gln
        self.Address = address
        self.Phone = phone
