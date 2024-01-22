import datetime
import pymysql


class DatabaseSport:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__open_connect()
        self.__cursor = None

    def __open_connect(self):
        # Попытка подключения к серверу
        try:
            self.__connect = pymysql.connect(
                host='XXXXX',
                user='XXXXX',
                passwd='XXXXX',
                database='XXXXX'
            )
        except Exception as ex:
            print(ex)

    def __close_connect(self):
        self.__connect.close()

    def __del__(self):
        DatabaseSport.__instance = None
        self.__close_connect()

    def __get_anything(self, procname: str, args: tuple = None):
        # Запрос к базе данных
        self.__cursor = self.__connect.cursor()
        # Определение того, является ли данная хранимая процедура с аргументами или без них
        if args is None:
            self.__cursor.callproc(procname)
        else:
            self.__cursor.callproc(procname, args)
        result = self.__cursor.fetchall()
        return result

    def get_parent(self, element_name: str, name: str) -> str:
        result = self.__get_anything('get_parent', (element_name, name))

        for row in result:
            for column in row:
                return column

    def get_items(self, items_name: str, criteria: str = 'Все'):
        result = self.__get_anything('get_items', (items_name, criteria))
        return result

    def get_sides_quantity(self, element_name: str, name: str) -> int:
        result = self.__get_anything('get_sides_quantity', (element_name, name))

        for row in result:
            for column in row:
                return column

    def get_data(self, training_name: str, week_number: str, day_number: str):
        result = self.__get_anything('get_data', (training_name,
                                                  0 if week_number == 'Все' else int(week_number),
                                                  0 if day_number == 'Все' else int(day_number)))
        return result

    def get_statistics(self, criteria: str):
        result = self.__get_anything('get_statistics', (criteria,))
        return result

    def get_numbers(self, training_name: str, criteria: str = ''):
        if criteria == '':
            # Случай, когда хотим получить week_numbers
            result = self.__get_anything('get_numbers', (training_name, -1))
        else:
            # Случай, когда хотим получить day_numbers
            result = self.__get_anything('get_numbers', (training_name, 0 if criteria == 'Все' else int(criteria)))
        return result

    def update_data_yoga(self,
                         pose_number: int,
                         asana_name: str,
                         yoga_date: str,
                         index_changeable_column: int,
                         new_side_or_note: str = 'Пусто',
                         new_time_work_or_rest: int = 0
                         ):
        # Запрос к базе данных
        self.__cursor = self.__connect.cursor()
        self.__cursor.callproc('update_data_yoga',
                               (pose_number,
                                asana_name,
                                yoga_date,
                                index_changeable_column,
                                new_side_or_note,
                                new_time_work_or_rest)
                               )
        self.__connect.commit()

    def update_data_workout(self,
                            exercise_name: str,
                            exercise_side: str,
                            workout_date: str,
                            index_changeable_column: int,
                            new_side_or_note: str = 'Пусто',
                            new_reps_quantity: int = 0,
                            new_time_rest_or_weight: float = 0.00,
                            new_qrl: int = 0,
                            new_training_volume: float = 0.00, ):
        # Запрос к базе данных
        self.__cursor = self.__connect.cursor()
        self.__cursor.callproc('update_data_workout',
                               (exercise_name,
                                exercise_side,
                                workout_date,
                                index_changeable_column,
                                new_side_or_note,
                                new_reps_quantity,
                                new_time_rest_or_weight,
                                new_qrl,
                                new_training_volume)
                               )
        self.__connect.commit()

    def update_data_stretching(self,
                               pose_number: int,
                               asana_name: str,
                               yoga_date: str,
                               index_changeable_column: int,
                               new_side_or_note: str = 'Пусто',
                               new_time_work_or_rest: int = 0
                               ):
        # Запрос к базе данных
        self.__cursor = self.__connect.cursor()
        self.__cursor.callproc('update_data_stretching',
                               (pose_number,
                                asana_name,
                                yoga_date,
                                index_changeable_column,
                                new_side_or_note,
                                new_time_work_or_rest)
                               )
        self.__connect.commit()

    def get_exercise_base_reps_quantity(self, exercise_name: str, exercise_side: str) -> int:
        result = self.__get_anything('get_exercise_base_reps_quantity', (exercise_name, exercise_side))

        for row in result:
            for column in row:
                return column

    def add_data_workout(self,
                         week_number: int,
                         day_number: int,
                         mesocycle: str,
                         microcycle: str,
                         muscle_group: str,
                         muscle: str,
                         exercise: str,
                         side: str,
                         warm_up_1_time_rest_minutes: float,
                         warm_up_1_weight_kg: float,
                         warm_up_1_rq_times: int,
                         warm_up_2_time_rest_minutes: float,
                         warm_up_2_weight_kg: float,
                         warm_up_2_rq_times: int,
                         pre_worker_time_rest_minutes: float,
                         pre_worker_weight_kg: float,
                         pre_worker_rq_times: int,
                         worker_1_time_rest_minutes: float,
                         worker_1_weight_kg: float,
                         worker_1_rq_times: int,
                         worker_2_time_rest_minutes: float,
                         worker_2_weight_kg: float,
                         worker_2_rq_times: int,
                         qrl: int,
                         training_volume: float,
                         note: str,
                         date_workout: str
                         ):
        # Запрос к базе данных
        self.__cursor = self.__connect.cursor()
        self.__cursor.callproc('add_data_workout',
                               (
                                   week_number,
                                   day_number,
                                   mesocycle,
                                   microcycle,
                                   muscle_group,
                                   muscle,
                                   exercise,
                                   side,
                                   warm_up_1_time_rest_minutes,
                                   warm_up_1_weight_kg,
                                   warm_up_1_rq_times,
                                   warm_up_2_time_rest_minutes,
                                   warm_up_2_weight_kg,
                                   warm_up_2_rq_times,
                                   pre_worker_time_rest_minutes,
                                   pre_worker_weight_kg,
                                   pre_worker_rq_times,
                                   worker_1_time_rest_minutes,
                                   worker_1_weight_kg,
                                   worker_1_rq_times,
                                   worker_2_time_rest_minutes,
                                   worker_2_weight_kg,
                                   worker_2_rq_times,
                                   qrl,
                                   training_volume,
                                   note,
                                   date_workout
                               ))
        self.__connect.commit()

    def add_data_yoga(self,
                      week_number: int,
                      day_number: int,
                      complex: str,
                      specialization: str,
                      pose_number: int,
                      asana: str,
                      side: str,
                      time_work: int,
                      time_rest: int,
                      note: str,
                      date_yoga: str
                      ):
        # Запрос к базе данных
        self.__cursor = self.__connect.cursor()
        self.__cursor.callproc('add_data_yoga',
                               (
                                   week_number,
                                   day_number,
                                   complex,
                                   specialization,
                                   pose_number,
                                   asana,
                                   side,
                                   time_work,
                                   time_rest,
                                   note,
                                   date_yoga
                               ))
        self.__connect.commit()

    def add_data_stretching(self,
                            week_number: int,
                            day_number: int,
                            pose_number: int,
                            asana: str,
                            side: str,
                            time_work: int,
                            time_rest: int,
                            note: str,
                            date_stretching: str
                            ):
        # Запрос к базе данных
        self.__cursor = self.__connect.cursor()
        self.__cursor.callproc('add_data_stretching',
                               (
                                   week_number,
                                   day_number,
                                   pose_number,
                                   asana,
                                   side,
                                   time_work,
                                   time_rest,
                                   note,
                                   date_stretching
                               ))
        self.__connect.commit()

    def get_training_schedule(self):
        result = self.__get_anything('get_training_schedule')
        return result

    def get_last_date_training(self, training_name: str) -> datetime.date:
        result = self.__get_anything('get_last_date_training', (training_name,))

        for row in result:
            for column in row:
                return column

    def get_sequence_number(self, asana_name: str) -> int:
        result = self.__get_anything('get_sequence_number', (asana_name,))

        for row in result:
            for column in row:
                return column

    def get_last_mesocycle(self) -> str:
        result = self.__get_anything('get_last_mesocycle')

        for row in result:
            for column in row:
                return column

    def get_last_microcycle(self) -> str:
        result = self.__get_anything('get_last_microcycle')

        for row in result:
            for column in row:
                return column

    def get_time_rest(self,
                      mesocycle_name: str,
                      microcycle_name: str,
                      muscle_group_name: str,
                      approach_name: str
                      ) -> float:
        result = self.__get_anything('get_time_rest',
                                     (mesocycle_name,
                                      microcycle_name,
                                      muscle_group_name,
                                      approach_name))

        for row in result:
            for column in row:
                return column
