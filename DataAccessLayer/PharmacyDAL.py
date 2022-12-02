from DataAccessLayer import BaseAccessLayer
from Model import *


class PharmacyDataAccessLayer(BaseAccessLayer):
    def Insert(self, newPharmacy: Pharmacy):
        return super().execute(
            "InsertPharmacy @UserName=?,@Password=?,@RoleName=?,@PharmacyName=?,@GLN=?,@Address=?,@Phone=?",
            (newPharmacy.UserName, newPharmacy.Password, newPharmacy.RoleName, newPharmacy.PharmacyName,
             newPharmacy.GLN, newPharmacy.Address, newPharmacy.Phone))
