from items import \
    Mesocycles, Mesocycle, \
    Microcycles, Microcycle, \
    MuscleGroups, MuscleGroup, \
    Muscles, Muscle, \
    Exercises, Exercise
from training import Training


class Workout(Training):
    def __init__(self):
        super().__init__()
        self.mesocycles = Mesocycles()
        self.mesocycle = Mesocycle()
        self.microcycles = Microcycles()
        self.microcycle = Microcycle()
        self.muscle_groups = MuscleGroups()
        self.muscle_group = MuscleGroup()
        self.muscles = Muscles()
        self.muscle = Muscle()
        self.exercises = Exercises()
        self.exercise = Exercise()
