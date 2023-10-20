from __future__ import annotations
from database_sport import DatabaseSport


class Element:
    """Базовый класс, представляющий элемент, предназначенный для заполнения экземпляра класса Items"""

    def __init__(self):
        self.__name = None
        self.db_sport = DatabaseSport()

    @property
    def name(self) -> str:
        """Чтение имени"""
        return self.__name

    @name.setter
    def name(self, name: str):
        """Запись имени"""
        self.__name = name

    def __str__(self):
        return f"{type(self)} по имени: {self.name}"

    def __repr__(self):
        return f"{type(self)} по имени: {self.name}"

    def parent(self, element_name: str):
        """Чтение родительского объекта"""
        return self.db_sport.get_parent(element_name, self.name)


class Items:
    """Базовый класс, представляющий словарь, состоящий из элементов класса Element"""

    def __init__(self):
        self.__dict = dict()  # Словарь элементов
        self.db_sport = DatabaseSport()

    def __setitem__(self, key: str, value: Element):
        """Добавляет элемент в словарь"""
        self.__dict[key] = value

    def __getitem__(self, item: str) -> Element:
        """Возвращает элемент словаря"""
        return self.__dict[item]

    def __delitem__(self, key):
        """Удаляет элемент словаря"""
        del self.__dict[key]

    def __len__(self):
        """Возвращает количество элементов в словаре"""
        return len(self.__dict)

    def _form_dict(self, items_name: str, criteria: str = 'Все'):
        """Формирует словарь элементов"""
        result = self.db_sport.get_items(items_name, criteria)

        for row in result:
            # Создание экземпляра класса (Element) в зависимости от активного базового класса (Items)
            match items_name:
                case 'mesocycles':
                    element = Mesocycle()
                case 'microcycles':
                    element = Microcycle()
                case 'muscle_groups':
                    element = MuscleGroup()
                case 'muscles':
                    element = Muscle()
                case 'exercises':
                    element = Exercise()
                case 'complexes':
                    element = Complex()
                case 'specializations':
                    element = Specialization()
                case 'asanas':
                    element = Asana()
                case 'involved_muscles':
                    element = InvolvedMuscle()
            element.name = row[0]
            self[element.name] = element

    def clear(self):
        """Очищает словарь элементов"""
        self.__dict.clear()

    def __str__(self):
        return f"Словарь {type(self)}"

    def __iter__(self):
        self.__index = -1
        self.__list = []
        for key in self.__dict:
            self.__list.append(key)
        return self

    def __next__(self):
        if self.__index < len(self.__list) - 1:
            self.__index += 1
            key = self.__list[self.__index]
            return self.__dict[key]
        else:
            raise StopIteration


class Approach(Element):
    """Элемент, предназначенный для заполнения экземпляра класса Approaches"""

    def __init__(self):
        super().__init__()
        self.__time_rest = None
        self.__weight = None
        self.__reps_quantity = None

    def time_rest(self, mesocycle_name: str, microcycle_name: str, muscle_group_name: str) -> float:
        """Возвращает время отдыха"""
        self.__time_rest = self.db_sport.get_time_rest(mesocycle_name, microcycle_name, muscle_group_name, self.name)
        return self.__time_rest

        # # Определение времени отдыха в зависимости от подхода и мышечной группы
        # match self.name:
        #     case 'Разминка 1':
        #         match muscle_group_name:
        #             case 'Ноги' | 'Голень' | 'Спина' | 'Грудь':
        #                 self.__time_rest = 0.75
        #             case _:
        #                 self.__time_rest = 0.5
        #     case 'Разминка 2':
        #         match muscle_group_name:
        #             case 'Ноги' | 'Голень' | 'Спина' | 'Грудь':
        #                 self.__time_rest = 0.75
        #             case _:
        #                 self.__time_rest = 0.5
        #     case 'Предрабочий':
        #         match muscle_group_name:
        #             case 'Ноги' | 'Голень' | 'Спина' | 'Грудь':
        #                 self.__time_rest = 0.75
        #             case _:
        #                 self.__time_rest = 0.5
        #     case 'Рабочий 1':
        #         match muscle_group_name:
        #             case 'Ноги' | 'Голень' | 'Спина' | 'Грудь':
        #                 self.__time_rest = 1
        #             case _:
        #                 self.__time_rest = 0.75
        #     case 'Рабочий 2':
        #         match muscle_group_name:
        #             case 'Ноги' | 'Голень' | 'Спина' | 'Грудь':
        #                 self.__time_rest = 1
        #             case _:
        #                 self.__time_rest = 0.75

    def weight(self, base_weight: float) -> float:
        """Возвращает вес"""
        # Определение веса в зависимости от подхода и базового веса
        match self.name:
            case 'Разминка 1':
                self.__weight = base_weight * 0.25
            case 'Разминка 2':
                self.__weight = base_weight * 0.4
            case 'Предрабочий':
                self.__weight = base_weight * 0.8
            case 'Рабочий 1':
                self.__weight = base_weight
            case 'Рабочий 2':
                self.__weight = base_weight

        return self.__weight

    def reps_quantity(self, base_reps_quantity: int) -> int:
        """Возвращает количество повторений"""
        # Вычисление количества повторений во всех подходах в зависимости от базового количества повторений
        if base_reps_quantity < 14:
            reps_quantity_warm_up_1 = 12
            reps_quantity_warm_up_2 = 8
            reps_quantity_pre_worker = 4
        elif base_reps_quantity < 20:
            reps_quantity_warm_up_1 = 14
            reps_quantity_warm_up_2 = 10
            reps_quantity_pre_worker = 6
        elif base_reps_quantity < 26:
            reps_quantity_warm_up_1 = 16
            reps_quantity_warm_up_2 = 12
            reps_quantity_pre_worker = 8
        elif base_reps_quantity < 31:
            reps_quantity_warm_up_1 = 18
            reps_quantity_warm_up_2 = 14
            reps_quantity_pre_worker = 10

        reps_quantity_worker_1 = base_reps_quantity + 2
        reps_quantity_worker_2 = base_reps_quantity

        # Определение количества повторений в зависимости от подхода
        match self.name:
            case 'Разминка 1':
                self.__reps_quantity = reps_quantity_warm_up_1
            case 'Разминка 2':
                self.__reps_quantity = reps_quantity_warm_up_2
            case 'Предрабочий':
                self.__reps_quantity = reps_quantity_pre_worker
            case 'Рабочий 1':
                self.__reps_quantity = reps_quantity_worker_1
            case 'Рабочий 2':
                self.__reps_quantity = reps_quantity_worker_2

        return self.__reps_quantity


class Approaches(Items):
    """Словарь, состоящий из экземпляров класса Approach"""
    pass


class Asana(Element):
    """Элемент, предназначенный для заполнения экземпляра класса Asanas"""

    def __init__(self):
        super().__init__()
        self.__side = None
        self.__time_work = None
        self.__time_rest = None

    @property
    def sides_quantity(self) -> int:
        """Возвращает количество сторон"""
        return self.db_sport.get_sides_quantity('asana', self.name)

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side: str):
        self.__side = side

    @property
    def time_work(self):
        return self.__time_work

    @time_work.setter
    def time_work(self, time_work: int):
        self.__time_work = time_work

    @property
    def time_rest(self):
        return self.__time_rest

    @time_rest.setter
    def time_rest(self, time_rest: int):
        self.__time_rest = time_rest

    @property
    def sequence_number(self) -> int:
        return self.db_sport.get_sequence_number(self.name)


class Asanas(Items):
    """Словарь, состоящий из экземпляров класса Asana"""

    def __init__(self):
        super().__init__()
        super()._form_dict('asanas')


class Complex(Element):
    """Элемент, предназначенный для заполнения экземпляра класса Complexes"""

    @property
    def specializtions(self) -> Specializations:
        self.__specializtions = Specializations()
        return self.__specializtions


class Complexes(Items):
    """Словарь, состоящий из экземпляров класса Complex"""

    def __init__(self):
        super().__init__()
        super()._form_dict("complexes")


class Exercise(Element):
    """Элемент, предназначенный для заполнения экземпляра класса Exercises"""

    def __init__(self):
        super().__init__()
        self.approaches = Approaches()
        self.__side = None
        self.__reps_quantity = None
        self.__base_weight = None
        self.__qrl = None
        self.__training_volume = None

    @property
    def side(self) -> str:
        """Возвращает сторону"""
        return self.__side

    @side.setter
    def side(self, side: str):
        self.__side = side

    @property
    def sides_quantity(self) -> int:
        """Возвращает количество сторон"""
        return self.db_sport.get_sides_quantity('exercise', self.name)

    @property
    def base_reps_quantity(self):
        """Возвращает базовое количество повторений"""
        return self.db_sport.get_exercise_base_reps_quantity(self.name, self.side)

    @property
    def base_weight(self) -> float:
        """Возвращает базовый вес"""
        return self.__base_weight

    @base_weight.setter
    def base_weight(self, base_weight: float):
        self.__base_weight = base_weight

    def qrl(self,
            warm_up_1_reps_quantity: int,
            warm_up_2_reps_quantity: int,
            pre_worker_reps_quantity: int,
            worker_1_reps_quantity: int,
            worker_2_reps_quantity: int) -> int:
        """Возвращает КПШ"""
        self.__qrl = warm_up_1_reps_quantity + \
                     warm_up_2_reps_quantity + \
                     pre_worker_reps_quantity + \
                     worker_1_reps_quantity + \
                     worker_2_reps_quantity
        return self.__qrl

    def training_volume(self,
                        warm_up_1_reps_quantity: int,
                        warm_up_1_weight: float,
                        warm_up_2_reps_quantity: int,
                        warm_up_2_weight: float,
                        pre_worker_reps_quantity: int,
                        pre_worker_weight: float,
                        worker_1_reps_quantity: int,
                        worker_1_weight: float,
                        worker_2_reps_quantity: int,
                        worker_2_weight: float) -> float:
        self.__training_volume = warm_up_1_reps_quantity * warm_up_1_weight + \
                                 warm_up_2_reps_quantity * warm_up_2_weight + \
                                 pre_worker_reps_quantity * pre_worker_weight + \
                                 worker_1_reps_quantity * worker_1_weight + \
                                 worker_2_reps_quantity * worker_2_weight
        return self.__training_volume


class Exercises(Items):
    """Словарь, состоящий из экземпляров класса Exercise"""

    def __init__(self):
        super().__init__()
        super()._form_dict("exercises")


class InvolvedMuscle(Element):
    """Элемент, предназначенный для заполнения экземпляра класса InvolvedMuscles"""
    pass


class InvolvedMuscles(Items):
    """Словарь, состоящий из экземпляров класса InvolvedMuscle"""

    def __init__(self):
        super().__init__()
        super()._form_dict("involved_muscles")


class Mesocycle(Element):
    """Элемент, предназначенный для заполнения экземпляра класса Mesocycles"""
    pass


class Mesocycles(Items):
    """Словарь, состоящий из экземпляров класса Mesocycle"""

    def __init__(self):
        super().__init__()
        super()._form_dict('mesocycles')


class Microcycle(Element):
    """Элемент, предназначенный для заполнения экземпляра класса Microcycles"""
    pass


class Microcycles(Items):
    """Словарь, состоящий из экземпляров класса Microcycle"""

    def __init__(self):
        super().__init__()
        super()._form_dict('microcycles')


class MuscleGroup(Element):
    """Элемент, предназначенный для заполнения экземпляра класса MuscleGroups"""

    @property
    def muscles(self) -> Muscles:
        self.__muscles = Muscles()
        return self.__muscles


class MuscleGroups(Items):
    """Словарь, состоящий из экземпляров класса MuscleGroup"""

    def __init__(self):
        super().__init__()
        super()._form_dict("muscle_groups")


class Muscle(Element):
    """Элемент, предназначенный для заполнения экземпляра класса Muscles"""

    @property
    def exercises(self) -> Exercises:
        self.__exercises = Exercises()
        return self.__exercises


class Muscles(Items):
    """Словарь, состоящий из экземпляров класса Muscle"""

    def __init__(self):
        super().__init__()
        super()._form_dict("muscles")


class Specialization(Element):
    """Элемент, предназначенный для заполнения экземпляра класса Specializations"""

    @property
    def asanas(self) -> Asanas:
        self.__asanas = Asanas()
        return self.__asanas


class Specializations(Items):
    """Словарь, состоящий из экземпляров класса Specialization"""

    def __init__(self):
        super().__init__()
        super()._form_dict("specializations")
