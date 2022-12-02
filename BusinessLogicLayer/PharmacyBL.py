from DataAccessLayer import PharmacyDataAccessLayer
from Model import Pharmacy


class PharmacyBusinessLogic:
    def __init__(self):
        self.repository = PharmacyDataAccessLayer()

    def Insert(self, newPharmacy: Pharmacy):
        return self.repository.Insert(newPharmacy)
