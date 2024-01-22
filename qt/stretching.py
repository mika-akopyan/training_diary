from items import \
    InvolvedMuscles, \
    InvolvedMuscle, \
    Asanas
from training import Training


class Stretching(Training):
    def __init__(self):
        super().__init__()
        self.involved_muscles = InvolvedMuscles()
        self.involved_muscle = InvolvedMuscle()
        self.asanas = Asanas()
