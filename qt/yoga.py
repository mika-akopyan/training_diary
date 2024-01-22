from items import \
    Complexes, Complex, \
    Specializations, Specialization, \
    Asanas
from training import Training


class Yoga(Training):
    def __init__(self):
        super().__init__()
        self.complexes = Complexes()
        self.complex = Complex()
        self.specializations = Specializations()
        self.specialization = Specialization()
        self.asanas = Asanas()
