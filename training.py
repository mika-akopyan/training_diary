class Training:
    def __init__(self):
        self.week_numbers = []
        self.__week_number = None
        self.day_numbers = []
        self.__day_number = None
        self.__date = None

    @property
    def week_number(self) -> int:
        return self.__week_number

    @week_number.setter
    def week_number(self, week_number: int):
        self.__week_number = week_number

    @property
    def day_number(self) -> int:
        return self.__day_number

    @day_number.setter
    def day_number(self, day_number: int):
        self.__day_number = day_number

    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: tuple[int, int, int]):
        self.__date = f'{date[0]}-{date[1]}-{date[2]}'