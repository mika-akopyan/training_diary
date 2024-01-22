import datetime
from sport import *
import sys
from items import *
from stretching import Stretching
from yoga import Yoga
from workout import Workout


# ОБЩЕЕ
def open_or_close_main_menu():
    # Определение того, раскрыто или закрыто меню на момент вызова,
    # чтобы настроить размеры окна меню, его элементов и stackedWidget
    if ui.f_menu.width() == 151:
        ui.f_menu.setGeometry(10, 20, 51, 481)
        ui.f_main_menu.setGeometry(0, 70, 51, 271)
        ui.pb_open_close_main_menu.setGeometry(10, 10, 31, 31)
        ui.pb_home.setGeometry(10, 0, 31, 31)
        ui.pb_yoga.setGeometry(10, 40, 31, 31)
        ui.pb_workout.setGeometry(10, 80, 31, 31)
        ui.pb_stretching.setGeometry(10, 120, 31, 31)

        ui.pb_home.setText('')
        ui.pb_yoga.setText('')
        ui.pb_workout.setText('')
        ui.pb_stretching.setText('')

        ui.f_auxiliary_menu.setVisible(False)

        ui.stackedWidget.setGeometry(70, 10, 1001, 501)
    else:
        ui.stackedWidget.setGeometry(160, 10, 911, 501)

        ui.f_menu.setGeometry(10, 20, 151, 481)
        ui.f_main_menu.setGeometry(0, 70, 151, 271)
        ui.pb_open_close_main_menu.setGeometry(10, 10, 131, 31)
        ui.pb_home.setGeometry(10, 0, 131, 31)
        ui.pb_yoga.setGeometry(10, 40, 131, 31)
        # Определение активной кнопки на главном меню, чтобы настроить размеры элементов окна меню
        if ui.pb_home.isChecked():
            ui.pb_workout.setGeometry(10, 80, 131, 31)
            ui.pb_stretching.setGeometry(10, 120, 131, 31)
            ui.f_auxiliary_menu.setVisible(False)
        elif ui.pb_yoga.isChecked():
            ui.pb_workout.setGeometry(10, 200, 131, 31)
            ui.pb_stretching.setGeometry(10, 240, 131, 31)
            ui.f_auxiliary_menu.setGeometry(0, 80, 141, 111)
            ui.f_auxiliary_menu.setVisible(True)
        elif ui.pb_workout.isChecked():
            ui.pb_workout.setGeometry(10, 80, 131, 31)
            ui.pb_stretching.setGeometry(10, 240, 131, 31)
            ui.f_auxiliary_menu.setGeometry(0, 120, 151, 111)
            ui.f_auxiliary_menu.setVisible(True)
        else:
            ui.pb_workout.setGeometry(10, 80, 131, 31)
            ui.pb_stretching.setGeometry(10, 120, 131, 31)
            ui.f_auxiliary_menu.setGeometry(0, 160, 151, 111)
            ui.f_auxiliary_menu.setVisible(True)

        ui.pb_home.setText('  Главная')
        ui.pb_yoga.setText('  Йога')
        ui.pb_workout.setText('  Тренировка')
        ui.pb_stretching.setText('  Растяжка')


def page_home_activate():
    ui.pb_home.setChecked(True)
    ui.pb_yoga.setChecked(False)
    ui.pb_workout.setChecked(False)
    ui.pb_stretching.setChecked(False)

    ui.stackedWidget.setCurrentWidget(ui.home_page)

    # Определение того, раскрыто или закрыто меню на момент вызова, чтобы настроить размеры элементов окна меню
    if ui.f_menu.width() == 151:
        ui.pb_yoga.setGeometry(10, 40, 131, 31)
        ui.pb_workout.setGeometry(10, 80, 131, 31)
        ui.pb_stretching.setGeometry(10, 120, 131, 31)
    else:
        ui.pb_yoga.setGeometry(10, 40, 31, 31)
        ui.pb_workout.setGeometry(10, 80, 31, 31)
        ui.pb_stretching.setGeometry(10, 120, 31, 31)
    ui.f_auxiliary_menu.setVisible(False)


def page_yoga_activate():
    global last_page_yoga

    ui.pb_home.setChecked(False)
    ui.pb_yoga.setChecked(True)
    ui.pb_workout.setChecked(False)
    ui.pb_stretching.setChecked(False)

    # Определение того, раскрыто или закрыто меню на момент вызова, чтобы настроить размеры элементов окна меню
    if ui.f_menu.width() == 151:
        ui.pb_workout.setGeometry(10, 200, 131, 31)
        ui.pb_stretching.setGeometry(10, 240, 131, 31)
        ui.f_auxiliary_menu.setGeometry(0, 80, 151, 111)
        ui.f_auxiliary_menu.setVisible(True)

    match last_page_yoga:
        case None:
            ui.pb_creature.setChecked(True)
            ui.stackedWidget.setCurrentWidget(ui.y_page_creature)
            last_page_yoga = 'creature'
        case 'creature':
            ui.pb_creature.setChecked(True)
            ui.stackedWidget.setCurrentWidget(ui.y_page_creature)
            last_page_yoga = 'creature'
        case 'viewing':
            ui.pb_viewing.setChecked(True)
            ui.stackedWidget.setCurrentWidget(ui.y_page_viewing)
            last_page_yoga = 'viewing'
        case 'statistic':
            ui.pb_statistic.setChecked(True)
            ui.stackedWidget.setCurrentWidget(ui.y_page_statistic)
            last_page_yoga = 'statistic'


def page_workout_activate():
    global last_page_workout

    ui.pb_home.setChecked(False)
    ui.pb_yoga.setChecked(False)
    ui.pb_workout.setChecked(True)
    ui.pb_stretching.setChecked(False)

    # Определение того, раскрыто или закрыто меню на момент вызова, чтобы настроить размеры элементов окна меню
    if ui.f_menu.width() == 151:
        ui.pb_workout.setGeometry(10, 80, 131, 31)
        ui.pb_stretching.setGeometry(10, 240, 131, 31)
        ui.f_auxiliary_menu.setGeometry(0, 120, 151, 111)
        ui.f_auxiliary_menu.setVisible(True)

    match last_page_workout:
        case None:
            ui.pb_creature.setChecked(True)
            ui.stackedWidget.setCurrentWidget(ui.w_page_creature)
            last_page_workout = 'creature'
        case 'creature':
            ui.pb_creature.setChecked(True)
            ui.stackedWidget.setCurrentWidget(ui.w_page_creature)
            last_page_workout = 'creature'
        case 'viewing':
            ui.pb_viewing.setChecked(True)
            ui.stackedWidget.setCurrentWidget(ui.w_page_viewing)
            last_page_workout = 'viewing'
        case 'statistic':
            ui.pb_statistic.setChecked(True)
            ui.stackedWidget.setCurrentWidget(ui.w_page_statistic)
            last_page_workout = 'statistic'


def page_stretching_activate():
    global last_page_stretching

    ui.pb_home.setChecked(False)
    ui.pb_yoga.setChecked(False)
    ui.pb_workout.setChecked(False)
    ui.pb_stretching.setChecked(True)

    # Определение того, раскрыто или закрыто меню на момент вызова, чтобы настроить размеры элементов окна меню
    if ui.f_menu.width() == 151:
        ui.pb_workout.setGeometry(10, 80, 131, 31)
        ui.pb_stretching.setGeometry(10, 120, 131, 31)
        ui.f_auxiliary_menu.setGeometry(0, 160, 151, 111)
        ui.f_auxiliary_menu.setVisible(True)

    match last_page_stretching:
        case None:
            ui.pb_creature.setChecked(True)
            ui.stackedWidget.setCurrentWidget(ui.s_page_creature)
            last_page_stretching = 'creature'
        case 'creature':
            ui.pb_creature.setChecked(True)
            ui.stackedWidget.setCurrentWidget(ui.s_page_creature)
            last_page_stretching = 'creature'
        case 'viewing':
            ui.pb_viewing.setChecked(True)
            ui.stackedWidget.setCurrentWidget(ui.s_page_viewing)
            last_page_stretching = 'viewing'
        case 'statistic':
            ui.pb_statistic.setChecked(True)
            ui.stackedWidget.setCurrentWidget(ui.s_page_statistic)
            last_page_stretching = 'statistic'


def pb_creature_clicked():
    global last_page_yoga
    global last_page_workout
    global last_page_stretching

    # Определение активной кнопки на главном меню
    if ui.pb_yoga.isChecked():
        ui.stackedWidget.setCurrentWidget(ui.y_page_creature)
        last_page_yoga = 'creature'
    elif ui.pb_workout.isChecked():
        ui.stackedWidget.setCurrentWidget(ui.w_page_creature)
        last_page_workout = 'creature'
    elif ui.pb_stretching.isChecked():
        ui.stackedWidget.setCurrentWidget(ui.s_page_creature)
        last_page_stretching = 'creature'


def pb_viewing_clicked():
    global last_page_yoga
    global last_page_workout
    global last_page_stretching

    # Определение активной кнопки на главном меню
    if ui.pb_yoga.isChecked():
        ui.stackedWidget.setCurrentWidget(ui.y_page_viewing)
        last_page_yoga = 'viewing'
    elif ui.pb_workout.isChecked():
        ui.stackedWidget.setCurrentWidget(ui.w_page_viewing)
        last_page_workout = 'viewing'
    elif ui.pb_stretching.isChecked():
        ui.stackedWidget.setCurrentWidget(ui.s_page_viewing)
        last_page_stretching = 'viewing'


def pb_statistic_clicked():
    global last_page_yoga
    global last_page_workout
    global last_page_stretching

    # Определение активной кнопки на главном меню
    if ui.pb_yoga.isChecked():
        ui.stackedWidget.setCurrentWidget(ui.y_page_statistic)
        last_page_yoga = 'statistic'
    elif ui.pb_workout.isChecked():
        ui.stackedWidget.setCurrentWidget(ui.w_page_statistic)
        last_page_workout = 'statistic'
    elif ui.pb_stretching.isChecked():
        ui.stackedWidget.setCurrentWidget(ui.s_page_statistic)
        last_page_stretching = 'statistic'


def page_from_auxiliary_menu_activate():
    global last_page_yoga
    global last_page_workout
    global last_page_stretching

    # Определение активной кнопки на главном меню
    if ui.pb_yoga.isChecked():
        # Определение активной кнопки на второстепенном меню
        if ui.pb_creature.isChecked():
            ui.stackedWidget.setCurrentWidget(ui.y_page_creature)
            last_page_yoga = 'creature'
        elif ui.pb_viewing.isChecked():
            ui.stackedWidget.setCurrentWidget(ui.y_page_viewing)
            last_page_yoga = 'viewing'
        elif ui.pb_statistic.isChecked():
            ui.stackedWidget.setCurrentWidget(ui.y_page_statistic)
            last_page_yoga = 'statistic'
    elif ui.pb_workout.isChecked():
        # Определение активной кнопки на второстепенном меню
        if ui.pb_creature.isChecked():
            ui.stackedWidget.setCurrentWidget(ui.w_page_creature)
            last_page_workout = 'creature'
        elif ui.pb_viewing.isChecked():
            ui.stackedWidget.setCurrentWidget(ui.w_page_viewing)
            last_page_workout = 'viewing'
        elif ui.pb_statistic.isChecked():
            ui.stackedWidget.setCurrentWidget(ui.w_page_statistic)
            last_page_workout = 'statistic'
    elif ui.pb_stretching.isChecked():
        # Определение активной кнопки на второстепенном меню
        if ui.pb_creature.isChecked():
            ui.stackedWidget.setCurrentWidget(ui.s_page_creature)
            last_page_stretching = 'creature'
        elif ui.pb_viewing.isChecked():
            ui.stackedWidget.setCurrentWidget(ui.s_page_viewing)
            last_page_stretching = 'viewing'
        elif ui.pb_statistic.isChecked():
            ui.stackedWidget.setCurrentWidget(ui.s_page_statistic)
            last_page_stretching = 'statistic'


def form_training_schedule():
    result = db_sport.get_training_schedule()

    ui.home_tbl_training_schedule.setRowCount(len(result))
    ui.home_tbl_training_schedule.setColumnCount(6)
    ui.home_tbl_training_schedule.setHorizontalHeaderLabels([
        'Занятие',
        'Неделя №',
        'День №',
        'Неизвестно 1',
        'Неизвестно 2',
        'Дата',
    ])

    fill_table(result, ui.home_tbl_training_schedule)


# СХОЖИЕ ФУНКЦИИ
# Страница "Создание". GroupBox "Этап"
def set_value_sb_week_number(week_numbers: list, sb_week_number: QtWidgets.QSpinBox):
    # Проверка того, существуют ли записи в базе данных
    if len(week_numbers) == 0:
        sb_week_number.setValue(1)
        sb_week_number.setDisabled(True)

        # Определение текущей страницы
        match ui.stackedWidget.currentWidget().objectName():
            case 'y_page_creature':
                ui.y_pb_information_first_yoga.setVisible(True)
            case 'w_page_creature':
                ui.w_pb_information_first_workout.setVisible(True)
    else:
        sb_week_number.setMinimum(int(week_numbers[len(week_numbers) - 1]))
        sb_week_number.setMaximum(int(week_numbers[len(week_numbers) - 1]) + 1)
        sb_week_number.setValue(sb_week_number.minimum())

        # Определение текущей страницы
        match ui.stackedWidget.currentWidget().objectName():
            case 'y_page_creature':
                ui.y_pb_information_first_yoga.setVisible(False)
                ui.y_sb_week_number.setEnabled(True)
            case 'w_page_creature':
                ui.w_pb_information_first_workout.setVisible(False)
                ui.w_sb_week_number.setEnabled(True)


def week_number_value_changed():
    # Определение текущей страницы
    match ui.stackedWidget.currentWidget().objectName():
        case 'y_page_creature':
            yoga.week_number = ui.y_sb_week_number.value()

            # День номер
            if yoga.week_number == ui.y_sb_week_number.minimum():
                form_day_numbers(ui.y_sb_week_number.text())
                ui.y_sb_day_number.setValue(int(yoga.day_numbers[len(yoga.day_numbers) - 1]) + 1)
            else:
                ui.y_sb_day_number.setValue(1)
        case 'w_page_creature':
            workout.week_number = ui.w_sb_week_number.value()

            # День номер
            if workout.week_number == ui.w_sb_week_number.minimum():
                form_day_numbers(ui.w_sb_week_number.text())
                ui.w_sb_day_number.setMinimum(int(workout.day_numbers[len(workout.day_numbers) - 1]))
                ui.w_sb_day_number.setMaximum(int(workout.day_numbers[len(workout.day_numbers) - 1]) + 1)
                ui.w_sb_day_number.setValue(ui.w_sb_day_number.minimum())
                ui.w_sb_day_number.setEnabled(True)
            else:
                ui.w_sb_day_number.setMinimum(1)
                ui.w_sb_day_number.setValue(1)
                ui.w_sb_day_number.setDisabled(True)

            # Дата
            # Изменение минимальной даты в случае, если это не инициализация
            if ui.w_tbl_data_workout.rowCount() > 0:
                form_minimum_date()
                ui.w_cw_workout.setMinimumDate(minimum_date_workout)
                ui.w_cw_workout.setSelectedDate(ui.w_cw_workout.minimumDate())
                workout.date = ui.w_cw_workout.selectedDate().getDate()

            # Определение того, является ли это продолжением крайней тренировкой
            if (ui.w_sb_week_number.value() == ui.w_sb_week_number.minimum()) and \
                    (ui.w_sb_day_number.value() == ui.w_sb_day_number.minimum()):
                # Микроцикл
                ui.w_cb_mesocycle.setCurrentText(db_sport.get_last_mesocycle())
                ui.w_cb_mesocycle.setDisabled(True)
                # Мезоцикл
                ui.w_cb_microcycle.setCurrentText(db_sport.get_last_microcycle())
                ui.w_cb_microcycle.setDisabled(True)
                # Дата
                ui.w_cw_workout.setDisabled(True)

                ui.w_pb_information_like_last_workout.setVisible(True)
            else:
                # Микроцикл
                ui.w_cb_mesocycle.setEnabled(True)
                # Мезоцикл
                ui.w_cb_microcycle.setEnabled(True)
                # Дата
                ui.w_cw_workout.setEnabled(True)

                ui.w_pb_information_like_last_workout.setVisible(False)
        case 's_page_creature':
            stretching.week_number = ui.s_sb_week_number.value()

            # День номер
            if stretching.week_number == ui.s_sb_week_number.minimum():
                form_day_numbers(ui.s_sb_week_number.text())
                ui.s_sb_day_number.setValue(int(stretching.day_numbers[len(stretching.day_numbers) - 1]))
            else:
                ui.s_sb_day_number.setValue(1)


def day_number_value_changed():
    # Определение текущей страницы
    match ui.stackedWidget.currentWidget().objectName():
        case 'y_page_creature':
            yoga.day_number = ui.y_sb_day_number.value()
        case 'w_page_creature':
            workout.day_number = ui.w_sb_day_number.value()

            # Дата
            # Изменение минимальной даты в случае, если это не инициализация
            if ui.w_tbl_data_workout.rowCount() > 0:
                form_minimum_date()
                ui.w_cw_workout.setMinimumDate(minimum_date_workout)
                ui.w_cw_workout.setSelectedDate(ui.w_cw_workout.minimumDate())
                workout.date = ui.w_cw_workout.selectedDate().getDate()

            # Определение того, является ли это продолжением крайней тренировкой
            if (ui.w_sb_week_number.value() == ui.w_sb_week_number.minimum()) and \
                    (ui.w_sb_day_number.value() == ui.w_sb_day_number.minimum()):
                # Микроцикл
                ui.w_cb_mesocycle.setCurrentText(db_sport.get_last_mesocycle())
                ui.w_cb_mesocycle.setDisabled(True)
                # Мезоцикл
                ui.w_cb_microcycle.setCurrentText(db_sport.get_last_microcycle())
                ui.w_cb_microcycle.setDisabled(True)
                # Дата
                ui.w_cw_workout.setDisabled(True)

                ui.w_pb_information_like_last_workout.setVisible(True)
            else:
                # Микроцикл
                ui.w_cb_mesocycle.setEnabled(True)
                # Мезоцикл
                ui.w_cb_microcycle.setEnabled(True)
                # Дата
                ui.w_cw_workout.setEnabled(True)

                ui.w_pb_information_like_last_workout.setVisible(False)
        case 's_page_creature':
            stretching.day_number = ui.s_sb_day_number.value()

            # Дата
            try:
                last_date = db_sport.get_last_date_training('workout')

                stretching.date = (last_date.year,
                                   last_date.month,
                                   last_date.day)
            except AttributeError:
                pass


def date_changed():
    # Определение текущей страницы
    match ui.stackedWidget.currentWidget().objectName():
        case 'y_page_creature':
            yoga.date = ui.y_cw_yoga.selectedDate().getDate()
        case 'w_page_creature':
            workout.date = ui.w_cw_workout.selectedDate().getDate()


def form_minimum_date():
    # Определение текущей страницы
    match ui.stackedWidget.currentWidget().objectName():
        case 'y_page_creature':
            global minimum_date_yoga

            # Проверка того, есть ли записи в таблице "Йога данные"
            try:
                last_date = db_sport.get_last_date_training('yoga')
                minimum_date_yoga.setDate(last_date.year, last_date.month, last_date.day)
                minimum_date_yoga = minimum_date_yoga.addDays(1)
            except AttributeError:
                minimum_date_yoga.setDate(datetime.datetime.now().year,
                                          datetime.datetime.now().month,
                                          datetime.datetime.now().day)
        case 'w_page_creature':
            global minimum_date_workout

            # Проверка того, есть ли записи в таблице "Тренировка данные"
            try:
                last_date = db_sport.get_last_date_training('workout')
                minimum_date_workout.setDate(last_date.year, last_date.month, last_date.day)
                # Изменение минимальной даты в зависимости от выбранного номера дня тренировочной недели
                if not ((ui.w_sb_week_number.value() == ui.w_sb_week_number.minimum()) and
                        (ui.w_sb_day_number.value() == ui.w_sb_day_number.minimum())):
                    minimum_date_workout = minimum_date_workout.addDays(1)
            except AttributeError:
                minimum_date_workout.setDate(datetime.datetime.now().year,
                                             datetime.datetime.now().month,
                                             datetime.datetime.now().day)


def is_all_field_filled() -> bool:
    """Проверяет, заполнены ли все поля на окне"""
    is_filled = True

    # Определение текущей страницы
    match ui.stackedWidget.currentWidget().objectName():
        case 'y_page_creature':
            if ui.y_rb_left_side.isChecked() is False and ui.y_rb_right_side.isChecked() is False:
                is_filled = False
                ui.y_l_error_choose_side.setVisible(True)
        case 'w_page_creature':
            if workout.exercise.base_weight is None:
                is_filled = False
                ui.w_l_error_choose_base_weight.setVisible(True)
        case 's_page_creature':
            if ui.s_lstw_selected_asanas.count() == 0:
                is_filled = False
                ui.s_lstw_asana.setGeometry(160, 170, 381, 81)
                ui.s_l_error_choose_asana.setVisible(True)
            if ui.s_rb_left_side.isChecked() is False and ui.s_rb_right_side.isChecked() is False:
                is_filled = False
                ui.s_l_error_choose_side.setVisible(True)

    return is_filled


def msg_box_successful_saving():
    """Информирует, при успешеном занесении данных"""
    msg_box.information(Sport,
                        'Сохранение данных',
                        'Данные успешно сохранены!\n\n'
                        'Вы можете взглянуть на них на странице "Просмотр".')


def msg_box_incorrect_value(info_acceptable_value: str):
    """Информирует при введении некорректного значения"""
    msg_box.critical(Sport,
                     'Изменение данных',
                     'Данные не изменены, так как введено некорректное значение.\n\n'
                     f'{str(info_acceptable_value)}')


# Общее
def form_week_numbers():
    # Определение текущей страницы
    match ui.stackedWidget.currentWidget().objectName():
        case 'y_page_creature':
            yoga.week_numbers.clear()

            result = db_sport.get_numbers('yoga')

            for row in result:
                yoga.week_numbers.append(str(row[0]))
        case 'w_page_creature':
            workout.week_numbers.clear()

            result = db_sport.get_numbers('workout')

            for row in result:
                workout.week_numbers.append(str(row[0]))
        case 's_page_creature':
            stretching.week_numbers.clear()

            result = db_sport.get_numbers('stretching')

            for row in result:
                stretching.week_numbers.append(str(row[0]))


def form_day_numbers(week_number: str):
    # Определение текущей страницы
    match ui.stackedWidget.currentWidget().objectName():
        case 'y_page_creature' | 'y_page_viewing':
            yoga.day_numbers.clear()

            result = db_sport.get_numbers('yoga', week_number)

            for row in result:
                yoga.day_numbers.append(str(row[0]))
        case 'w_page_creature' | 'w_page_viewing':
            workout.day_numbers.clear()

            result = db_sport.get_numbers('workout', week_number)

            for row in result:
                workout.day_numbers.append(str(row[0]))
        case 's_page_creature' | 's_page_viewing':
            stretching.day_numbers.clear()

            result = db_sport.get_numbers('stretching', week_number)

            for row in result:
                stretching.day_numbers.append(str(row[0]))


def fill_table(result, table_name: QtWidgets.QTableWidget):
    """Заполняет QTableWidget данными"""
    row_number = 0

    for row in result:
        column_number = 0
        for column in row:
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(column))
            table_name.setItem(row_number, column_number, item)
            column_number += 1
        row_number += 1

    table_name.resizeColumnsToContents()


# Страница "Просмотр". GroupBox "Этап"
def cb_week_number_text_changed():
    # Определение текущей страницы
    match ui.stackedWidget.currentWidget().objectName():
        case 'y_page_creature' | 'y_page_viewing':
            # Номера практик
            if not ui.y_cb_week_number.currentText() == '':
                if ui.y_cb_week_number.currentText() == 'Все':
                    yoga.day_numbers.clear()
                    ui.y_cb_day_number.clear()

                    ui.y_cb_day_number.addItem('Все')
                else:
                    yoga.day_numbers.clear()
                    ui.y_cb_day_number.clear()

                    form_day_numbers(ui.y_cb_week_number.currentText())
                    ui.y_cb_day_number.addItem('Все')
                    ui.y_cb_day_number.addItems(yoga.day_numbers)
        case 'w_page_creature' | 'w_page_viewing':
            # Номера дней
            if not ui.w_cb_week_number.currentText() == '':
                if ui.w_cb_week_number.currentText() == 'Все':
                    workout.day_numbers.clear()
                    ui.w_cb_day_number.clear()

                    ui.w_cb_day_number.addItem('Все')
                else:
                    workout.day_numbers.clear()
                    ui.w_cb_day_number.clear()

                    form_day_numbers(ui.w_cb_week_number.currentText())
                    ui.w_cb_day_number.addItem('Все')
                    ui.w_cb_day_number.addItems(workout.day_numbers)
        case 's_page_creature' | 's_page_viewing':
            # Номера дней
            if not ui.s_cb_week_number.currentText() == '':
                if ui.s_cb_week_number.currentText() == 'Все':
                    stretching.day_numbers.clear()
                    ui.s_cb_day_number.clear()

                    ui.s_cb_day_number.addItem('Все')
                else:
                    stretching.day_numbers.clear()
                    ui.s_cb_day_number.clear()

                    form_day_numbers(ui.s_cb_week_number.currentText())
                    ui.s_cb_day_number.addItem('Все')
                    ui.s_cb_day_number.addItems(stretching.day_numbers)


def cb_day_number_text_changed():
    # Определение текущей страницы
    match ui.stackedWidget.currentWidget().objectName():
        case 'y_page_creature' | 'y_page_viewing':
            if not ui.y_cb_day_number.currentText() == '':
                ui.y_tbl_data_yoga.clearContents()
                form_data_yoga(ui.y_cb_week_number.currentText(), ui.y_cb_day_number.currentText())
        case 'w_page_creature' | 'w_page_viewing':
            # Номера дней
            if not ui.w_cb_day_number.currentText() == '':
                ui.w_tbl_data_workout.clearContents()
                form_data_workout(ui.w_cb_week_number.currentText(), ui.w_cb_day_number.currentText())
        case 's_page_creature' | 's_page_viewing':
            if not ui.s_cb_day_number.currentText() == '':
                ui.s_tbl_data_stretching.clearContents()
                form_data_stretching(ui.s_cb_week_number.currentText(), ui.s_cb_day_number.currentText())


# ЙОГА
# Страница "Создание". Кнопки
def y_insert_data_yoga():
    # Проверка заполненности полей перед сохранением данных
    if is_all_field_filled():
        # Определение выбранной стороны
        if ui.y_rb_left_side.isChecked():
            side = 'Л'
        else:
            side = 'П'

        asana = Asana()

        # Занесение данных в базу данных
        for i in range(0, ui.y_lw_asanas.count()):
            asana.name = ui.y_lw_asanas.item(i).text()

            db_sport.add_data_yoga(
                yoga.week_number,
                yoga.day_number,
                yoga.complex.name,
                yoga.specialization.name,
                int(i + 1),
                ui.y_lw_asanas.item(i).text(),
                'О' if asana.sides_quantity == 1 else side,
                0 if asana.name == 'Поза трупа' else ui.y_sb_time_work.value(),
                0 if asana.name == 'Поза трупа' else ui.y_sb_time_rest.value(),
                '',
                yoga.date
            )

        # Информирование при успешном занесении данных
        msg_box_successful_saving()

        # Обновление информации на странице "Просмотр", чтобы там появились внесенные данные
        yoga.week_numbers.clear()
        ui.y_cb_week_number.clear()

        form_week_numbers()
        ui.y_cb_week_number.addItem('Все')
        ui.y_cb_week_number.addItems(yoga.week_numbers)

        ui.y_pb_hint_changing_data_yoga.setVisible(False)
        ui.y_tbl_data_yoga.setGeometry(20, 110, 871, 381)

        # Сброс всех виджетов на странице "Создание" до изначальных настроек
        y_clear_data_on_page_creature()

        # Обновление номера дня, так его не происходит в момент сброса всех виджетов до изначальных настроек
        ui.y_sb_day_number.setValue(ui.y_sb_day_number.value() + 1)

        # Сброс всех кнопок на странице "Статистика" на False, чтобы там не отображались старые данные
        radio_buttons = [ui.y_rb_complexes,
                         ui.y_rb_specializations,
                         ui.y_rb_asanas_on_the_sides,
                         ui.y_rb_week_number,
                         ui.y_rb_day_number,
                         ui.y_rb_last_training_complex,
                         ui.y_rb_last_training_specialization]

        for radio_button in radio_buttons:
            radio_button.setAutoExclusive(False)
            radio_button.setChecked(False)
            radio_button.setAutoExclusive(True)

        # Сброс всех данных в таблице "Статистика", чтобы там не отображались старые данные
        ui.y_tbl_statistics.clearContents()
        ui.y_tbl_statistics.setRowCount(0)
        ui.y_tbl_statistics.setColumnCount(0)

        # Обновление информации в таблице "Расписание занятий"
        ui.home_tbl_training_schedule.clearContents()
        form_training_schedule()


def y_clear_data_on_page_creature():
    # Сброс всех виджетов на странице "Создание" до изначальных настроек
    # GroupBox "Этап"
    # Номер недели и номер дня
    form_week_numbers()
    set_value_sb_week_number(yoga.week_numbers, ui.y_sb_week_number)

    # Дата
    form_minimum_date()
    ui.y_cw_yoga.setMinimumDate(minimum_date_yoga)
    ui.y_cw_yoga.setSelectedDate(minimum_date_yoga)
    yoga.date = ui.y_cw_yoga.selectedDate().getDate()

    # GroupBox "Описание"
    # Комплекс, специализация, асаны
    ui.y_cb_complex.setCurrentText('По воздействию на позвоночник')

    # Сторона
    ui.y_l_error_choose_side.setVisible(False)
    radio_buttons = [ui.y_rb_left_side, ui.y_rb_right_side]

    for radio_button in radio_buttons:
        radio_button.setAutoExclusive(False)
        radio_button.setChecked(False)
        radio_button.setAutoExclusive(True)

    # Время работы и время отдыха
    ui.y_sb_time_work.setValue(1)
    ui.y_sb_time_rest.setValue(1)


# Страница "Создание". GroupBox "Описание"
def y_complex_name_changed():
    yoga.complex.name = ui.y_cb_complex.currentText()

    # Специализация
    yoga.specializations.clear()
    ui.y_cb_specialization.clear()

    yoga.specializations._form_dict('specializations', yoga.complex.name)
    for element in yoga.specializations:
        ui.y_cb_specialization.addItem(element.name)


def y_specialization_name_changed():
    yoga.specialization.name = ui.y_cb_specialization.currentText()

    # Асаны
    yoga.asanas.clear()
    ui.y_lw_asanas.clear()

    yoga.asanas._form_dict('asanas', yoga.specialization.name)
    for element in yoga.asanas:
        ui.y_lw_asanas.addItem(element.name)


def y_side_changed():
    ui.y_l_error_choose_side.setVisible(False)


# Страница "Статистика". GroupBox "Критерий"
def y_rb_complexes_clicked():
    result = db_sport.get_statistics('complexes_quantity')

    ui.y_tbl_statistics.clear()

    ui.y_tbl_statistics.setRowCount(len(result))
    ui.y_tbl_statistics.setColumnCount(2)
    ui.y_tbl_statistics.setHorizontalHeaderLabels([
        'Комплекс',
        'Количество выполнений'
    ])

    fill_table(result, ui.y_tbl_statistics)


def y_rb_specializations_clicked():
    result = db_sport.get_statistics('specializations_quantity')

    ui.y_tbl_statistics.clear()

    ui.y_tbl_statistics.setRowCount(len(result))
    ui.y_tbl_statistics.setColumnCount(2)
    ui.y_tbl_statistics.setHorizontalHeaderLabels([
        'Специализация',
        'Количество выполнений'
    ])

    fill_table(result, ui.y_tbl_statistics)


def y_rb_asanas_on_the_sides_clicked():
    result = db_sport.get_statistics('asanas_on_the_sides_quantity')

    ui.y_tbl_statistics.clear()

    ui.y_tbl_statistics.setRowCount(len(result))
    ui.y_tbl_statistics.setColumnCount(3)
    ui.y_tbl_statistics.setHorizontalHeaderLabels([
        'Асана',
        'Сторона',
        'Количество выполнений'
    ])

    fill_table(result, ui.y_tbl_statistics)


def y_rb_week_number_clicked():
    result = db_sport.get_statistics('for_yoga_number')

    ui.y_tbl_statistics.clear()

    ui.y_tbl_statistics.setRowCount(len(result))
    ui.y_tbl_statistics.setColumnCount(3)
    ui.y_tbl_statistics.setHorizontalHeaderLabels([
        'Неделя №',
        'Время работы (циклов вдох-выдох)',
        'Время отдыха (циклов вдох-выдох)',
    ])

    fill_table(result, ui.y_tbl_statistics)


def y_rb_day_number_clicked():
    result = db_sport.get_statistics('per_practice_number')

    ui.y_tbl_statistics.clear()

    ui.y_tbl_statistics.setRowCount(len(result))
    ui.y_tbl_statistics.setColumnCount(4)
    ui.y_tbl_statistics.setHorizontalHeaderLabels([
        'Неделя №',
        'День №',
        'Время работы (циклов вдох-выдох)',
        'Время отдыха (циклов вдох-выдох)',
    ])

    fill_table(result, ui.y_tbl_statistics)


def y_rb_last_training_complex_clicked():
    result = db_sport.get_statistics('last_training_complex')

    ui.y_tbl_statistics.clear()

    ui.y_tbl_statistics.setRowCount(len(result))
    ui.y_tbl_statistics.setColumnCount(2)
    ui.y_tbl_statistics.setHorizontalHeaderLabels([
        'Комплекс',
        'Количество прошедших дней',
    ])

    fill_table(result, ui.y_tbl_statistics)


def y_rb_last_training_specialization_clicked():
    result = db_sport.get_statistics('last_training_specialization')

    ui.y_tbl_statistics.clear()

    ui.y_tbl_statistics.setRowCount(len(result))
    ui.y_tbl_statistics.setColumnCount(2)
    ui.y_tbl_statistics.setHorizontalHeaderLabels([
        'Специализация',
        'Количество прошедших дней',
    ])

    fill_table(result, ui.y_tbl_statistics)


# Страница "Просмотр"
def form_data_yoga(week_number, day_number):
    result = db_sport.get_data('yoga', week_number, day_number)

    ui.y_tbl_data_yoga.setRowCount(len(result))
    ui.y_tbl_data_yoga.setColumnCount(11)
    ui.y_tbl_data_yoga.setHorizontalHeaderLabels([
        'Неделя №',
        'День №',
        'Комплекс',
        'Специализация',
        '№ позы',
        'Асана',
        'Сторона',
        'Время работы (циклов вдох-выдох)',
        'Время отдыха (циклов вдох-выдох)',
        'Комментарий',
        'Дата',
    ])

    fill_table(result, ui.y_tbl_data_yoga)


def y_tbl_data_yoga_cellPressed():
    global connect_y_update_data_yoga

    # Проверка того, был ли установлен connect с функцией изменения значения в ячейке до этого
    if not connect_y_update_data_yoga:
        ui.y_tbl_data_yoga.cellChanged.connect(y_update_data_yoga)
        connect_y_update_data_yoga = True

    # Проверка доступности изменения значения выбранной ячейки
    if ui.y_tbl_data_yoga.currentColumn() in range(0, 6) or ui.y_tbl_data_yoga.currentColumn() == 10:
        ui.y_pb_hint_changing_data_yoga.setVisible(False)
        ui.y_tbl_data_yoga.setGeometry(20, 110, 871, 381)

        msg_box.warning(Sport,
                        'Изменение данных',
                        'Данные столбцы не подлежат изменению:\n\n'
                        '"Неделя №";\n'
                        '"День №";\n'
                        '"Комплекс";\n'
                        '"Специализация";\n'
                        '"№ позы";\n'
                        '"Асана".\n'
                        '"Дата".\n\n'
                        'Будьте внимательны!')
    else:
        global tbl_data_text_before_change

        # Запись значения в ячейке до изменения,
        # чтобы в дальнейшем при некорректном введенном значения выставить исходное значение
        current_row = ui.y_tbl_data_yoga.currentRow()
        current_column = ui.y_tbl_data_yoga.currentColumn()
        tbl_data_text_before_change = ui.y_tbl_data_yoga.item(current_row, current_column).text()

        # Отображение подсказки по поводу допустимого значения в корректируемой ячейке
        # в зависимости от активного столбца
        match current_column:
            case 6:
                ui.y_tbl_data_yoga.setGeometry(20, 110, 871, 341)
                ui.y_pb_hint_changing_data_yoga.setVisible(True)

                asana = Asana()
                asana.name = ui.y_tbl_data_yoga.item(current_row, 5).text()

                if asana.sides_quantity == 1:
                    ui.y_pb_hint_changing_data_yoga.setText(f'Сторона у асаны "{asana.name}" может быть равной '
                                                            f'только "О".')
                elif asana.sides_quantity == 2:
                    ui.y_pb_hint_changing_data_yoga.setText(f'Сторона у асаны "{asana.name}" может быть равной '
                                                            f'только "Л" или "П".')
            case 7 | 8:
                ui.y_tbl_data_yoga.setGeometry(20, 110, 871, 341)
                ui.y_pb_hint_changing_data_yoga.setVisible(True)
                ui.y_pb_hint_changing_data_yoga.setText('Время работы и время отдыха может быть только целым числом '
                                                        'от 0 до 127.')
            case 9:
                ui.y_pb_hint_changing_data_yoga.setVisible(False)
                ui.y_tbl_data_yoga.setGeometry(20, 110, 871, 381)


def y_update_data_yoga():
    current_row = ui.y_tbl_data_yoga.currentRow()
    current_column = ui.y_tbl_data_yoga.currentColumn()

    # Проверка того, что выбрана какая-либо ячейка
    if current_row != -1:
        cell_new_text = ui.y_tbl_data_yoga.item(current_row, current_column).text()

        # Определение колонки, в которой происходят изменения
        match current_column:
            case 6:
                asana = Asana()
                asana.name = ui.y_tbl_data_yoga.item(current_row, 5).text()

                # Проверка количества сторон у асаны
                if asana.sides_quantity == 1:
                    # Проверка корректности введенного значения
                    if cell_new_text == 'О':
                        db_sport.update_data_yoga(int(ui.y_tbl_data_yoga.item(current_row, 4).text()),
                                                  ui.y_tbl_data_yoga.item(current_row, 5).text(),
                                                  ui.y_tbl_data_yoga.item(current_row, 10).text(),
                                                  current_column,
                                                  ui.y_tbl_data_yoga.item(current_row, current_column).text(),
                                                  0)
                    else:
                        msg_box_incorrect_value(f'Сторона у асаны "{asana.name}" может быть равной только "О".')

                        ui.y_tbl_data_yoga.item(current_row, current_column).setText(tbl_data_text_before_change)
                elif asana.sides_quantity == 2:
                    # Проверка корректности введенного значения
                    if cell_new_text == 'Л' or cell_new_text == 'П':
                        db_sport.update_data_yoga(int(ui.y_tbl_data_yoga.item(current_row, 4).text()),
                                                  ui.y_tbl_data_yoga.item(current_row, 5).text(),
                                                  ui.y_tbl_data_yoga.item(current_row, 10).text(),
                                                  current_column,
                                                  ui.y_tbl_data_yoga.item(current_row, current_column).text(),
                                                  0)
                    else:
                        msg_box_incorrect_value(f'Сторона у асаны "{asana.name}" может быть равной только "Л" или "П".')

                        ui.y_tbl_data_yoga.item(current_row, current_column).setText(tbl_data_text_before_change)
            case 7 | 8:
                # Проверка корректности введенного значения
                if cell_new_text.isdigit() and not (len(cell_new_text) >= 2 and cell_new_text[0] == '0'):
                    if int(cell_new_text) < 128:
                        db_sport.update_data_yoga(int(ui.y_tbl_data_yoga.item(current_row, 4).text()),
                                                  ui.y_tbl_data_yoga.item(current_row, 5).text(),
                                                  ui.y_tbl_data_yoga.item(current_row, 10).text(),
                                                  current_column,
                                                  'Пусто',
                                                  int(ui.y_tbl_data_yoga.item(current_row, current_column).text()))
                    else:
                        msg_box_incorrect_value('Время работы и время отдыха может быть\n'
                                                'только целым числом от 0 до 127.')

                        ui.y_tbl_data_yoga.item(current_row, current_column).setText(tbl_data_text_before_change)
                else:
                    msg_box_incorrect_value('Время работы и время отдыха может быть\n'
                                            'только целым числом от 0 до 127.')

                    ui.y_tbl_data_yoga.item(current_row, current_column).setText(tbl_data_text_before_change)
            case 9:
                db_sport.update_data_yoga(int(ui.y_tbl_data_yoga.item(current_row, 4).text()),
                                          ui.y_tbl_data_yoga.item(current_row, 5).text(),
                                          ui.y_tbl_data_yoga.item(current_row, 10).text(),
                                          current_column,
                                          ui.y_tbl_data_yoga.item(current_row, current_column).text(),
                                          0)


# ТРЕНИРОВКА
# Страница "Создание". GroupBox "Этап"
def w_mesocycle_name_changed():
    workout.mesocycle.name = ui.w_cb_mesocycle.currentText()

    # Микроцикл
    workout.microcycles.clear()
    ui.w_cb_microcycle.clear()

    workout.microcycles._form_dict('microcycles', workout.mesocycle.name)
    for element in workout.microcycles:
        ui.w_cb_microcycle.addItem(element.name)


def w_microcycle_name_changed():
    workout.microcycle.name = ui.w_cb_microcycle.currentText()


# Страница "Создание". Общее
def w_insert_data_workout():
    # Проверка заполненности полей перед сохранением данных
    if is_all_field_filled():
        # Определение необходимости дублирования введенных данных с изменением стороны
        number_additions = 1
        side_second_addition = ''
        match workout.muscle_group.name:
            case 'Бицепс' | 'Плечи' | 'Предплечья' | 'Спина' | 'Трицепс':
                number_additions = 2
                match workout.exercise.side:
                    case 'О':
                        side_second_addition = 'ОО'
                    case 'Л':
                        side_second_addition = 'ЛП'
                    case 'П':
                        side_second_addition = 'ПЛ'
            case 'Ноги' | 'Голень' | 'Грудь' | 'Шея' | 'Пресс' | 'Поясница':
                match workout.exercise.side:
                    case 'Л':
                        number_additions = 2
                        side_second_addition = 'ЛП'
                    case 'П':
                        number_additions = 2
                        side_second_addition = 'ПЛ'

        # Занесение данных в базу данных
        for number_addition in range(1, number_additions + 1):
            db_sport.add_data_workout(
                workout.week_number,
                workout.day_number,
                workout.mesocycle.name,
                workout.microcycle.name,
                workout.muscle_group.name,
                workout.muscle.name,
                workout.exercise.name,
                workout.exercise.side if number_addition == 1 else side_second_addition,
                warm_up_1.time_rest(workout.mesocycle.name, workout.microcycle.name, workout.muscle_group.name),
                warm_up_1.weight(workout.exercise.base_weight),
                warm_up_1.reps_quantity(workout.exercise.base_reps_quantity),
                warm_up_2.time_rest(workout.mesocycle.name, workout.microcycle.name, workout.muscle_group.name),
                warm_up_2.weight(workout.exercise.base_weight),
                warm_up_2.reps_quantity(workout.exercise.base_reps_quantity),
                pre_worker.time_rest(workout.mesocycle.name, workout.microcycle.name, workout.muscle_group.name),
                pre_worker.weight(workout.exercise.base_weight),
                pre_worker.reps_quantity(workout.exercise.base_reps_quantity),
                worker_1.time_rest(workout.mesocycle.name, workout.microcycle.name, workout.muscle_group.name),
                worker_1.weight(workout.exercise.base_weight),
                worker_1.reps_quantity(workout.exercise.base_reps_quantity),
                worker_2.time_rest(workout.mesocycle.name, workout.microcycle.name, workout.muscle_group.name),
                worker_2.weight(workout.exercise.base_weight),
                worker_2.reps_quantity(workout.exercise.base_reps_quantity),
                workout.exercise.qrl(warm_up_1.reps_quantity(workout.exercise.base_reps_quantity),
                                     warm_up_2.reps_quantity(workout.exercise.base_reps_quantity),
                                     pre_worker.reps_quantity(workout.exercise.base_reps_quantity),
                                     worker_1.reps_quantity(workout.exercise.base_reps_quantity),
                                     worker_2.reps_quantity(workout.exercise.base_reps_quantity)),
                workout.exercise.training_volume(warm_up_1.reps_quantity(workout.exercise.base_reps_quantity),
                                                 warm_up_1.weight(workout.exercise.base_weight),
                                                 warm_up_2.reps_quantity(workout.exercise.base_reps_quantity),
                                                 warm_up_2.weight(workout.exercise.base_weight),
                                                 pre_worker.reps_quantity(workout.exercise.base_reps_quantity),
                                                 pre_worker.weight(workout.exercise.base_weight),
                                                 worker_1.reps_quantity(workout.exercise.base_reps_quantity),
                                                 worker_1.weight(workout.exercise.base_weight),
                                                 worker_2.reps_quantity(workout.exercise.base_reps_quantity),
                                                 worker_2.weight(workout.exercise.base_weight), ),
                '',
                workout.date
            )

        # Информирование при успешном занесении данных
        msg_box_successful_saving()

        # Обновление информации на странице "Просмотр", чтобы там появились внесенные данные
        workout.week_numbers.clear()
        ui.w_cb_week_number.clear()

        form_week_numbers()
        ui.w_cb_week_number.addItem('Все')
        ui.w_cb_week_number.addItems(workout.week_numbers)

        ui.w_pb_hint_changing_data_workout.setVisible(False)
        ui.w_tbl_data_workout.setGeometry(20, 100, 871, 391)

        # Сброс всех виджетов на странице "Создание" до изначальных настроек
        w_clear_data_on_page_creature()

        # День номер (необходимо его отдельно проработать после добавления самой первой тренировки)
        form_day_numbers(ui.w_sb_week_number.text())
        if len(workout.week_numbers) == 1 and len(workout.day_numbers) == 1:
            ui.w_sb_day_number.setMinimum(int(workout.day_numbers[len(workout.day_numbers) - 1]))
            ui.w_sb_day_number.setMaximum(int(workout.day_numbers[len(workout.day_numbers) - 1]) + 1)
            ui.w_sb_day_number.setValue(ui.w_sb_day_number.minimum())
            ui.w_sb_day_number.setEnabled(True)

        # Сброс всех кнопок на странице "Статистика" на False, чтобы там не отображались старые данные
        radio_buttons = [ui.w_rb_muscle_groups,
                         ui.w_rb_muscles,
                         ui.w_rb_exercises_on_the_sides,
                         ui.w_rb_week_number,
                         ui.w_rb_day_number,
                         ui.w_rb_last_training_muscle_group,
                         ui.w_rb_last_training_muscle,
                         ui.w_rb_last_training_exercise]

        for radio_button in radio_buttons:
            radio_button.setAutoExclusive(False)
            radio_button.setChecked(False)
            radio_button.setAutoExclusive(True)

        # Сброс всех данных в таблице "Статистика", чтобы там не отображались старые данные
        ui.w_tbl_statistics.clearContents()
        ui.w_tbl_statistics.setRowCount(0)
        ui.w_tbl_statistics.setColumnCount(0)

        # Обновление информации в таблице "Расписание занятий"
        ui.home_tbl_training_schedule.clearContents()
        form_training_schedule()

        # РАСТЯЖКА
        ui.s_sb_week_number.setValue(ui.w_sb_week_number.value())
        stretching.week_number = ui.s_sb_week_number.value()
        ui.s_sb_day_number.setValue(ui.w_sb_day_number.value())
        stretching.day_number = ui.s_sb_day_number.value()


def w_clear_data_on_page_creature():
    # Сброс всех виджетов на странице "Создание" до изначальных настроек
    # GroupBox "Этап"
    # Номер недели и номер дня
    form_week_numbers()
    set_value_sb_week_number(workout.week_numbers, ui.w_sb_week_number)
    # Специально самостоятельно вызываю метод, чтобы в дальнейшем правильно сформировалась дата
    week_number_value_changed()

    # Мезоцикл и микроцикл
    for element in workout.mesocycles:
        ui.w_cb_mesocycle.addItem(element.name)

    # Дата
    form_minimum_date()
    ui.w_cw_workout.setMinimumDate(minimum_date_workout)
    ui.w_cw_workout.setSelectedDate(minimum_date_workout)
    workout.date = ui.w_cw_workout.selectedDate().getDate()

    # GroupBox "Описание"
    # Мышечная группа, мышца, упражнение и сторона
    ui.w_cb_muscle_group.setCurrentText('Бицепс')

    # Базовый вес
    ui.w_l_error_choose_base_weight.setVisible(False)
    ui.w_dsb_base_weight.setValue(0.00)


# Страница "Создание". GroupBox "Описание"
def w_muscle_group_name_changed():
    workout.muscle_group.name = ui.w_cb_muscle_group.currentText()

    # Мышца
    workout.muscles.clear()
    ui.w_cb_muscle.clear()

    workout.muscles._form_dict('muscles', workout.muscle_group.name)
    for element in workout.muscles:
        ui.w_cb_muscle.addItem(element.name)


def w_muscle_name_changed():
    workout.muscle.name = ui.w_cb_muscle.currentText()

    # Упражнение
    workout.exercises.clear()
    ui.w_cb_exercise.clear()

    workout.exercises._form_dict('exercises', workout.muscle.name)
    for element in workout.exercises:
        ui.w_cb_exercise.addItem(element.name)


def w_exercise_name_changed():
    workout.exercise.name = ui.w_cb_exercise.currentText()

    ui.w_cb_side.clear()

    match workout.exercise.sides_quantity:
        case 1:
            ui.w_cb_side.addItem('О')
        case 2:
            ui.w_cb_side.addItem('Л')
            ui.w_cb_side.addItem('П')
        case 3:
            ui.w_cb_side.addItem('О')
            ui.w_cb_side.addItem('Л')
            ui.w_cb_side.addItem('П')


def w_side_changed():
    workout.exercise.side = ui.w_cb_side.currentText()


def w_base_weight_value_changed():
    if ui.w_dsb_base_weight.value() > 0.00:
        ui.w_l_error_choose_base_weight.setVisible(False)
        workout.exercise.base_weight = ui.w_dsb_base_weight.value()
    elif ui.w_dsb_base_weight.value() == 0.00:
        workout.exercise.base_weight = None


# Страница "Статистика". GroupBox "Критерий"
def w_rb_muscle_groups_clicked():
    result = db_sport.get_statistics('muscle_groups_quantity')

    ui.w_tbl_statistics.clear()

    ui.w_tbl_statistics.setRowCount(len(result))
    ui.w_tbl_statistics.setColumnCount(2)
    ui.w_tbl_statistics.setHorizontalHeaderLabels([
        'Мышечная группа',
        'Количество выполнений'
    ])

    fill_table(result, ui.w_tbl_statistics)


def w_rb_muscles_clicked():
    result = db_sport.get_statistics('muscles_quantity')

    ui.w_tbl_statistics.clear()

    ui.w_tbl_statistics.setRowCount(len(result))
    ui.w_tbl_statistics.setColumnCount(2)
    ui.w_tbl_statistics.setHorizontalHeaderLabels([
        'Мышца',
        'Количество выполнений'
    ])

    fill_table(result, ui.w_tbl_statistics)


def w_rb_exercises_on_the_sides_clicked():
    result = db_sport.get_statistics('exercises_on_the_sides_quantity')

    ui.w_tbl_statistics.clear()

    ui.w_tbl_statistics.setRowCount(len(result))
    ui.w_tbl_statistics.setColumnCount(3)
    ui.w_tbl_statistics.setHorizontalHeaderLabels([
        'Упражнение',
        'Сторона',
        'Количество выполнений'
    ])

    fill_table(result, ui.w_tbl_statistics)


def w_rb_week_number_clicked():
    result = db_sport.get_statistics('for_workout_number')

    ui.w_tbl_statistics.clear()

    ui.w_tbl_statistics.setRowCount(len(result))
    ui.w_tbl_statistics.setColumnCount(3)
    ui.w_tbl_statistics.setHorizontalHeaderLabels([
        'Неделя №',
        'КПШ',
        'Тренировочный объем',
    ])

    fill_table(result, ui.w_tbl_statistics)


def w_rb_day_number_clicked():
    result = db_sport.get_statistics('per_day_number')

    ui.w_tbl_statistics.clear()

    ui.w_tbl_statistics.setRowCount(len(result))
    ui.w_tbl_statistics.setColumnCount(4)
    ui.w_tbl_statistics.setHorizontalHeaderLabels([
        'Неделя №',
        'День №',
        'КПШ',
        'Тренировочный объем',
    ])

    fill_table(result, ui.w_tbl_statistics)


def w_rb_last_training_muscle_group_clicked():
    result = db_sport.get_statistics('last_training_muscle_group')

    ui.w_tbl_statistics.clear()

    ui.w_tbl_statistics.setRowCount(len(result))
    ui.w_tbl_statistics.setColumnCount(2)
    ui.w_tbl_statistics.setHorizontalHeaderLabels([
        'Мышечная группа',
        'Количество прошедших дней',
    ])

    fill_table(result, ui.w_tbl_statistics)


def w_rb_last_training_muscle_clicked():
    result = db_sport.get_statistics('last_training_muscle')

    ui.w_tbl_statistics.clear()

    ui.w_tbl_statistics.setRowCount(len(result))
    ui.w_tbl_statistics.setColumnCount(2)
    ui.w_tbl_statistics.setHorizontalHeaderLabels([
        'Мышца',
        'Количество прошедших дней',
    ])

    fill_table(result, ui.w_tbl_statistics)


def w_rb_last_training_exercise_clicked():
    result = db_sport.get_statistics('last_training_exercise')

    ui.w_tbl_statistics.clear()

    ui.w_tbl_statistics.setRowCount(len(result))
    ui.w_tbl_statistics.setColumnCount(2)
    ui.w_tbl_statistics.setHorizontalHeaderLabels([
        'Упражнение',
        'Количество прошедших дней',
    ])

    fill_table(result, ui.w_tbl_statistics)


# Страница "Просмотр"
def form_data_workout(week_number, day_number):
    result = db_sport.get_data('workout', week_number, day_number)

    ui.w_tbl_data_workout.setRowCount(len(result))
    ui.w_tbl_data_workout.setColumnCount(27)
    ui.w_tbl_data_workout.setHorizontalHeaderLabels([
        'Неделя №',
        'День №',
        'Мезоцикл',
        'Микроцикл',
        'Мышечная группа',
        'Мышца',
        'Упражнение',
        'Сторона',
        'Раз 1 время отдыха (мин)',
        'Раз 1 вес (кг)',
        'Раз 1 КП (раз)',
        'Раз 2 время отдыха (мин)',
        'Раз 2 вес (кг)',
        'Раз 2 КП (раз)',
        'Предраб время отдыха (мин)',
        'Предраб вес (кг)',
        'Предраб КП (раз)',
        'Раб 1 время отдыха (мин)',
        'Раб 1 вес (кг)',
        'Раб 1 КП (раз)',
        'Раб 2 время отдыха (мин)',
        'Раб 2 вес (кг)',
        'Раб 2 КП (раз)',
        'КПШ',
        'Тренировочный объем',
        'Комментарий',
        'Дата',
    ])

    fill_table(result, ui.w_tbl_data_workout)


# Страница "Просмотр"
def w_tbl_data_workout_cellPressed():
    global connect_w_update_data_workout

    # Проверка того, был ли установлен connect с функцией изменения значения в ячейке до этого
    if not connect_w_update_data_workout:
        ui.w_tbl_data_workout.cellChanged.connect(w_update_data_workout)
        connect_w_update_data_workout = True

    # Проверка доступности изменения значения выбранной ячейки
    if ui.w_tbl_data_workout.currentColumn() in range(0, 7) or \
            ui.w_tbl_data_workout.currentColumn() in range(23, 25) or \
            ui.w_tbl_data_workout.currentColumn() == 26:
        ui.w_pb_hint_changing_data_workout.setVisible(False)
        ui.w_tbl_data_workout.setGeometry(20, 100, 871, 391)

        msg_box.warning(Sport,
                        'Изменение данных',
                        'Данные столбцы не подлежат изменению:\n\n'
                        '"Неделя №";\n'
                        '"День №";\n'
                        '"Мезоцикл";\n'
                        '"Микроцикл";\n'
                        '"Мышечная группа";\n'
                        '"Мышца";\n'
                        '"Упражнение";\n'
                        '"КПШ";\n'
                        '"Тренировочный объем";\n'
                        '"Дата".\n\n'
                        'Будьте внимательны!')
    else:
        global tbl_data_text_before_change

        # Запись значения в ячейке до изменения,
        # чтобы в дальнейшем при некорректном введенном значения выставить исходное значение
        current_row = ui.w_tbl_data_workout.currentRow()
        current_column = ui.w_tbl_data_workout.currentColumn()
        tbl_data_text_before_change = ui.w_tbl_data_workout.item(current_row, current_column).text()

        # Отображение подсказки по поводу допустимого значения в корректируемой ячейке
        # в зависимости от активного столбца
        match current_column:
            case 7:
                ui.w_tbl_data_workout.setGeometry(20, 100, 871, 351)
                ui.w_pb_hint_changing_data_workout.setVisible(True)

                exercise = Exercise()
                exercise.name = ui.w_tbl_data_workout.item(current_row, 6).text()

                if exercise.sides_quantity == 1:
                    ui.w_pb_hint_changing_data_workout.setText(f'Сторона у упражнения "{exercise.name}" может быть '
                                                               f'равной только "О" или "ОО".')
                elif exercise.sides_quantity == 2:
                    ui.w_pb_hint_changing_data_workout.setText(f'Сторона у упражнения "{exercise.name}" может быть '
                                                               f'равной только "Л", "ЛП", "П" или "ПЛ".')
                elif exercise.sides_quantity == 3:
                    ui.w_pb_hint_changing_data_workout.setText(f'Сторона у упражнения "{exercise.name}" может быть '
                                                               f'равной только "О", "ОО", "Л", "ЛП", "П" или "ПЛ".')
            case 8 | 9 | 11 | 12 | 14 | 15 | 17 | 18 | 20 | 21:
                ui.w_tbl_data_workout.setGeometry(20, 100, 871, 351)
                ui.w_pb_hint_changing_data_workout.setVisible(True)
                ui.w_pb_hint_changing_data_workout.setText('Время отдыха и вес могут быть только вещественным числом '
                                                           'больше или равным нулю. '
                                                           'Вещественные числа должны быть записаны через точку (".").')
            case 10 | 13 | 16 | 19 | 22:
                ui.w_tbl_data_workout.setGeometry(20, 100, 871, 351)
                ui.w_pb_hint_changing_data_workout.setVisible(True)
                ui.w_pb_hint_changing_data_workout.setText('Количество повторений может быть только целым числом '
                                                           'от 0 до 127.')
            case 25:
                ui.w_pb_hint_changing_data_workout.setVisible(False)
                ui.w_tbl_data_workout.setGeometry(20, 100, 871, 391)


def w_update_data_workout():
    current_row = ui.w_tbl_data_workout.currentRow()
    current_column = ui.w_tbl_data_workout.currentColumn()

    # Проверка того, что выбрана какая-либо ячейка
    if current_row != -1:
        cell_new_text = ui.w_tbl_data_workout.item(current_row, current_column).text()

        # Определение колонки, в которой происходят изменения
        match current_column:
            case 7:
                exercise = Exercise()
                exercise.name = ui.w_tbl_data_workout.item(current_row, 6).text()

                # Проверка количества сторон у упражнения
                if exercise.sides_quantity == 1:
                    # Проверка корректности введенного значения
                    if cell_new_text == 'О' or cell_new_text == 'ОО':
                        db_sport.update_data_workout(ui.w_tbl_data_workout.item(current_row, 6).text(),
                                                     str(tbl_data_text_before_change),
                                                     ui.w_tbl_data_workout.item(current_row, 26).text(),
                                                     current_column,
                                                     new_side_or_note=
                                                     ui.w_tbl_data_workout.item(current_row, current_column).text())
                    else:
                        msg_box_incorrect_value(f'Сторона у упражнения "{exercise.name}"\n'
                                                f'может быть равной только "О" или "ОО".')

                        ui.w_tbl_data_workout.item(current_row, current_column).setText(tbl_data_text_before_change)
                elif exercise.sides_quantity == 2:
                    # Проверка корректности введенного значения
                    if cell_new_text == 'Л' or cell_new_text == 'ЛП' or cell_new_text == 'П' or cell_new_text == 'ПЛ':
                        db_sport.update_data_workout(ui.w_tbl_data_workout.item(current_row, 6).text(),
                                                     str(tbl_data_text_before_change),
                                                     ui.w_tbl_data_workout.item(current_row, 26).text(),
                                                     current_column,
                                                     new_side_or_note=
                                                     ui.w_tbl_data_workout.item(current_row, current_column).text())
                    else:
                        msg_box_incorrect_value(f'Сторона у упражнения "{exercise.name}"\n'
                                                f'может быть равной только "Л", "ЛП", "П" или "ПЛ".')

                        ui.w_tbl_data_workout.item(current_row, current_column).setText(tbl_data_text_before_change)
                elif exercise.sides_quantity == 3:
                    # Проверка корректности введенного значения
                    if cell_new_text == 'О' or cell_new_text == 'ОО' or \
                            cell_new_text == 'Л' or cell_new_text == 'ЛП' or \
                            cell_new_text == 'П' or cell_new_text == 'ПЛ':
                        db_sport.update_data_workout(ui.w_tbl_data_workout.item(current_row, 6).text(),
                                                     str(tbl_data_text_before_change),
                                                     ui.w_tbl_data_workout.item(current_row, 26).text(),
                                                     current_column,
                                                     new_side_or_note=
                                                     ui.w_tbl_data_workout.item(current_row, current_column).text())
                    else:
                        msg_box_incorrect_value(f'Сторона у упражнения "{exercise.name}"\n'
                                                f'может быть равной только "О", "ОО", "Л", "ЛП", "П" или "ПЛ".')

                        ui.w_tbl_data_workout.item(current_row, current_column).setText(tbl_data_text_before_change)
            case 8 | 9 | 11 | 12 | 14 | 15 | 17 | 18 | 20 | 21:
                # Проверка корректности введенного значения
                try:
                    a = float(cell_new_text)
                    if a >= 0:
                        # Определение колонки, в которой происходят изменения, после успешной проверки на корректность
                        match current_column:
                            case 8 | 11 | 14 | 17 | 20:
                                db_sport.update_data_workout(ui.w_tbl_data_workout.item(current_row, 6).text(),
                                                             ui.w_tbl_data_workout.item(current_row, 7).text(),
                                                             ui.w_tbl_data_workout.item(current_row, 26).text(),
                                                             current_column,
                                                             new_time_rest_or_weight=
                                                             float(ui.w_tbl_data_workout.
                                                                   item(current_row, current_column).text()))
                            case 9 | 12 | 15 | 18 | 21:
                                exercise = Exercise()

                                db_sport.update_data_workout(ui.w_tbl_data_workout.item(current_row, 6).text(),
                                                             ui.w_tbl_data_workout.item(current_row, 7).text(),
                                                             ui.w_tbl_data_workout.item(current_row, 26).text(),
                                                             current_column,
                                                             new_time_rest_or_weight=
                                                             float(ui.w_tbl_data_workout.
                                                                   item(current_row, current_column).text()),
                                                             new_training_volume=
                                                             exercise.training_volume(
                                                                 int(ui.w_tbl_data_workout.item(current_row,
                                                                                                10).text()),
                                                                 float(
                                                                     ui.w_tbl_data_workout.item(current_row, 9).text()),
                                                                 int(ui.w_tbl_data_workout.item(current_row,
                                                                                                13).text()),
                                                                 float(ui.w_tbl_data_workout.item(current_row,
                                                                                                  12).text()),
                                                                 int(ui.w_tbl_data_workout.item(current_row,
                                                                                                16).text()),
                                                                 float(ui.w_tbl_data_workout.item(current_row,
                                                                                                  15).text()),
                                                                 int(ui.w_tbl_data_workout.item(current_row,
                                                                                                19).text()),
                                                                 float(ui.w_tbl_data_workout.item(current_row,
                                                                                                  18).text()),
                                                                 int(ui.w_tbl_data_workout.item(current_row,
                                                                                                22).text()),
                                                                 float(ui.w_tbl_data_workout.item(current_row,
                                                                                                  21).text())))

                                # Обновление информации в таблице с данными по тренировке,
                                # чтобы там отобразились обновленные значения тренировочного объема
                                ui.w_tbl_data_workout.clearContents()
                                form_data_workout(ui.w_cb_week_number.currentText(), ui.w_cb_day_number.currentText())
                    else:
                        msg_box_incorrect_value('Время отдыха и вес могут быть только вещественным числом\n'
                                                'больше или равным нулю.\n\n'
                                                'Вещественные числа должны быть записаны через точку (".").')

                        ui.w_tbl_data_workout.item(current_row, current_column).setText(tbl_data_text_before_change)
                except ValueError:
                    msg_box_incorrect_value('Время отдыха и вес могут быть только вещественным числом\n'
                                            'больше или равным нулю.\n\n'
                                            'Вещественные числа должны быть записаны через точку (".").')

                    ui.w_tbl_data_workout.item(current_row, current_column).setText(tbl_data_text_before_change)
            case 10 | 13 | 16 | 19 | 22:
                # Проверка корректности введенного значения
                if cell_new_text.isdigit():
                    if int(cell_new_text) < 128:
                        exercise = Exercise()

                        db_sport.update_data_workout(ui.w_tbl_data_workout.item(current_row, 6).text(),
                                                     ui.w_tbl_data_workout.item(current_row, 7).text(),
                                                     ui.w_tbl_data_workout.item(current_row, 26).text(),
                                                     current_column,
                                                     new_reps_quantity=
                                                     int(ui.w_tbl_data_workout.
                                                         item(current_row, current_column).text()),
                                                     new_qrl=
                                                     exercise.qrl(
                                                         int(ui.w_tbl_data_workout.item(current_row, 10).text()),
                                                         int(ui.w_tbl_data_workout.item(current_row, 13).text()),
                                                         int(ui.w_tbl_data_workout.item(current_row, 16).text()),
                                                         int(ui.w_tbl_data_workout.item(current_row, 19).text()),
                                                         int(ui.w_tbl_data_workout.item(current_row, 22).text())),
                                                     new_training_volume=
                                                     exercise.training_volume(
                                                         int(ui.w_tbl_data_workout.item(current_row, 10).text()),
                                                         float(ui.w_tbl_data_workout.item(current_row, 9).text()),
                                                         int(ui.w_tbl_data_workout.item(current_row, 13).text()),
                                                         float(ui.w_tbl_data_workout.item(current_row, 12).text()),
                                                         int(ui.w_tbl_data_workout.item(current_row, 16).text()),
                                                         float(ui.w_tbl_data_workout.item(current_row, 15).text()),
                                                         int(ui.w_tbl_data_workout.item(current_row, 19).text()),
                                                         float(ui.w_tbl_data_workout.item(current_row, 18).text()),
                                                         int(ui.w_tbl_data_workout.item(current_row, 22).text()),
                                                         float(ui.w_tbl_data_workout.item(current_row, 21).text())))

                        # Обновление информации в таблице с данными по тренировке,
                        # чтобы там отобразились обновленные значения КПШ и тренировочного объема
                        ui.w_tbl_data_workout.clearContents()
                        form_data_workout(ui.w_cb_week_number.currentText(), ui.w_cb_day_number.currentText())
                    else:
                        msg_box_incorrect_value('Количество повторений может быть\n'
                                                'только целым числом от 0 до 127.')

                        ui.w_tbl_data_workout.item(current_row, current_column).setText(tbl_data_text_before_change)
                else:
                    msg_box_incorrect_value('Количество повторений может быть\n'
                                            'только целым числом от 0 до 127.')

                    ui.w_tbl_data_workout.item(current_row, current_column).setText(tbl_data_text_before_change)
            case 25:
                # Проверка корректности введенного значения
                db_sport.update_data_workout(ui.w_tbl_data_workout.item(current_row, 6).text(),
                                             ui.w_tbl_data_workout.item(current_row, 7).text(),
                                             ui.w_tbl_data_workout.item(current_row, 26).text(),
                                             current_column,
                                             new_side_or_note=
                                             ui.w_tbl_data_workout.item(current_row, current_column).text())


# РАСТЯЖКА
# Страница "Создание". GroupBox "Описание"
def s_involved_muscle_name_changed():
    stretching.involved_muscle.name = ui.s_lstw_involved_muscle.currentItem().text()

    # Асаны
    stretching.asanas.clear()
    ui.s_lstw_asana.clear()

    stretching.asanas._form_dict('asanas', stretching.involved_muscle.name)
    for element in stretching.asanas:
        ui.s_lstw_asana.addItem(element.name)


def s_pb_clear_selection_clicked():
    # Определение того, выбрана ли какая-то задействованная мышца
    if ui.s_lstw_involved_muscle.currentRow() == -1:
        msg_box.critical(Sport,
                         'Очистка выбора',
                         'Данные не очищены, так как не выбран ни один\n'
                         'элемент в списке "Задействованная мышца".')
    else:
        # Задействованная мышца
        ui.s_lstw_involved_muscle.clearSelection()

        # Асана
        stretching.asanas.clear()
        ui.s_lstw_asana.clear()
        stretching.asanas._form_dict('asanas', 'Гибкость 1')
        for element in stretching.asanas:
            ui.s_lstw_asana.addItem(element.name)
        ui.s_lstw_asana.takeItem(ui.s_lstw_asana.count() - 1)

        stretching.asanas.clear()
        stretching.asanas._form_dict('asanas', 'Гибкость 2')
        for element in stretching.asanas:
            ui.s_lstw_asana.addItem(element.name)
        ui.s_lstw_asana.takeItem(ui.s_lstw_asana.count() - 1)

        stretching.asanas.clear()
        stretching.asanas._form_dict('asanas', 'Гибкость 3')
        for element in stretching.asanas:
            ui.s_lstw_asana.addItem(element.name)
        ui.s_lstw_asana.takeItem(ui.s_lstw_asana.count() - 1)


def s_add_asana_in_selected_asanas():
    """Добавление асаны в список 'Выбранные асаны'"""
    ui.s_lstw_asana.setGeometry(160, 170, 381, 111)
    ui.s_l_error_choose_asana.setVisible(False)

    added_asana = Asana()
    added_asana.name = ui.s_lstw_asana.currentItem().text()

    # Определение того, куда вставлять добавляемую асану, чтобы они шли согласно порядковым номерам
    if ui.s_lstw_selected_asanas.count() == 0:
        ui.s_lstw_selected_asanas.addItem(added_asana.name)
    else:
        for row in range(0, ui.s_lstw_selected_asanas.count()):
            selected_asana = Asana()
            selected_asana.name = ui.s_lstw_selected_asanas.item(row).text()

            if added_asana.sequence_number < selected_asana.sequence_number:
                ui.s_lstw_selected_asanas.insertItem(row, added_asana.name)
                break
            elif added_asana.sequence_number == selected_asana.sequence_number:
                msg_box.warning(Sport,
                                'Добавление асаны в список',
                                f'Асана "{added_asana.name}" уже есть\n'
                                'в списке "Выбранные асаны"!')
                break
            elif row == ui.s_lstw_selected_asanas.count() - 1:
                ui.s_lstw_selected_asanas.addItem(added_asana.name)


def s_side_changed():
    ui.s_l_error_choose_side.setVisible(False)


# Страница "Создание". Выбранные асаны
def s_delete_asana_from_selected_asanas():
    """Удаление асаны из списка 'Выбранные асаны'"""
    answer = msg_box.question(Sport,
                              'Удаление асаны из списка',
                              'Вы уверены, что хотите удалить асану\n'
                              f'{ui.s_lstw_selected_asanas.currentItem().text()} из списка "Выбранные асаны"?',
                              QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

    if answer == QtWidgets.QMessageBox.StandardButton.Yes:
        item = ui.s_lstw_selected_asanas.takeItem(ui.s_lstw_selected_asanas.currentRow())
        del item


# Страница "Создание". Кнопки
def s_insert_data_stretching():
    # Проверка наличия первой тренировки, чтобы было то, для чего формировать растяжку
    try:
        last_date = db_sport.get_last_date_training('workout')

        stretching.date = (last_date.year,
                           last_date.month,
                           last_date.day)
    except AttributeError:
        msg_box.warning(Sport,
                        'Сохранение данных',
                        'Данные не сохранены!\n\n'
                        'Для начала создайте тренировку, только\n'
                        'потом создайте для нее растяжку.')
    else:
        form_week_numbers()
        form_day_numbers(ui.s_sb_week_number.value())

        # Проверка того, была ли составлена уже растяжка для выбранного номера недели и номера дня
        if ui.s_sb_week_number.text() in stretching.week_numbers and \
                ui.s_sb_day_number.text() in stretching.day_numbers:
            msg_box.critical(Sport,
                             'Сохранение данных',
                             'Данные не сохранены, так как уже составлена растяжка\n'
                             f'на неделю №{stretching.week_number} и день №{stretching.day_number}!')

            # Сброс всех виджетов на странице "Создание" до изначальных настроек
            s_clear_data_on_page_creature()
        else:
            # Проверка заполненности полей перед сохранением данных
            if is_all_field_filled():
                # Определение выбранной стороны
                if ui.s_rb_left_side.isChecked():
                    side = 'Л'
                else:
                    side = 'П'

                asana = Asana()

                # Занесение данных в базу данных
                for i in range(0, ui.s_lstw_selected_asanas.count()):
                    asana.name = ui.s_lstw_selected_asanas.item(i).text()

                    db_sport.add_data_stretching(
                        stretching.week_number,
                        stretching.day_number,
                        int(i + 1),
                        ui.s_lstw_selected_asanas.item(i).text(),
                        'О' if asana.sides_quantity == 1 else side,
                        ui.s_sb_time_work.value(),
                        ui.s_sb_time_rest.value(),
                        '',
                        stretching.date
                    )

                # Информирование при успешном занесении данных
                msg_box_successful_saving()

                # Обновление информации на странице "Просмотр", чтобы там появились внесенные данные
                stretching.week_numbers.clear()
                ui.s_cb_week_number.clear()

                form_week_numbers()
                ui.s_cb_week_number.addItem('Все')
                ui.s_cb_week_number.addItems(stretching.week_numbers)

                ui.s_pb_hint_changing_data_stretching.setVisible(False)
                ui.s_tbl_data_stretching.setGeometry(20, 100, 871, 391)

                # Сброс всех виджетов на странице "Создание" до изначальных настроек
                s_clear_data_on_page_creature()

                # Сброс всех кнопок на странице "Статистика" на False, чтобы там не отображались старые данные
                radio_buttons = [ui.s_rb_asanas_on_the_sides, ui.s_rb_last_training_asana]

                for radio_button in radio_buttons:
                    radio_button.setAutoExclusive(False)
                    radio_button.setChecked(False)
                    radio_button.setAutoExclusive(True)

                # Сброс всех данных в таблице "Статистика", чтобы там не отображались старые данные
                ui.s_tbl_statistics.clearContents()
                ui.s_tbl_statistics.setRowCount(0)
                ui.s_tbl_statistics.setColumnCount(0)

                # Обновление информации в таблице "Расписание занятий"
                ui.home_tbl_training_schedule.clearContents()
                form_training_schedule()


def s_clear_data_on_page_creature():
    # Сброс всех виджетов на странице "Создание" до изначальных настроек
    # GroupBox "Этап"
    # Номер недели и номер дня
    form_week_numbers()
    set_value_sb_week_number(stretching.week_numbers, ui.s_sb_week_number)

    # GroupBox "Описание"
    # Задействованная мышца
    ui.s_lstw_involved_muscle.clearSelection()

    # Асана
    ui.s_lstw_asana.setGeometry(160, 170, 381, 111)
    ui.s_l_error_choose_asana.setVisible(False)

    stretching.asanas.clear()
    ui.s_lstw_asana.clear()
    stretching.asanas._form_dict('asanas', 'Гибкость 1')
    for element in stretching.asanas:
        ui.s_lstw_asana.addItem(element.name)
    ui.s_lstw_asana.takeItem(ui.s_lstw_asana.count() - 1)

    stretching.asanas.clear()
    stretching.asanas._form_dict('asanas', 'Гибкость 2')
    for element in stretching.asanas:
        ui.s_lstw_asana.addItem(element.name)
    ui.s_lstw_asana.takeItem(ui.s_lstw_asana.count() - 1)

    stretching.asanas.clear()
    stretching.asanas._form_dict('asanas', 'Гибкость 3')
    for element in stretching.asanas:
        ui.s_lstw_asana.addItem(element.name)
    ui.s_lstw_asana.takeItem(ui.s_lstw_asana.count() - 1)

    # Сторона
    ui.s_l_error_choose_side.setVisible(False)
    radio_buttons = [ui.s_rb_left_side, ui.s_rb_right_side]

    for radio_button in radio_buttons:
        radio_button.setAutoExclusive(False)
        radio_button.setChecked(False)
        radio_button.setAutoExclusive(True)

    # Время работы и время отдыха
    ui.s_sb_time_work.setValue(1)
    ui.s_sb_time_rest.setValue(1)

    # Выбранные асаны
    ui.s_lstw_selected_asanas.clear()


# Страница "Просмотр"
def form_data_stretching(week_number, day_number):
    result = db_sport.get_data('stretching', week_number, day_number)

    ui.s_tbl_data_stretching.setRowCount(len(result))
    ui.s_tbl_data_stretching.setColumnCount(9)
    ui.s_tbl_data_stretching.setHorizontalHeaderLabels([
        'Неделя №',
        'День №',
        '№ позы',
        'Асана',
        'Сторона',
        'Время работы (циклов вдох-выдох)',
        'Время отдыха (циклов вдох-выдох)',
        'Комментарий',
        'Дата',
    ])

    fill_table(result, ui.s_tbl_data_stretching)


def s_tbl_data_stretching_cellPressed():
    global connect_s_update_data_stretching

    # Проверка того, был ли установлен connect с функцией изменения значения в ячейке до этого
    if not connect_s_update_data_stretching:
        ui.s_tbl_data_stretching.cellChanged.connect(s_update_data_stretching)
        connect_s_update_data_stretching = True

    if ui.s_tbl_data_stretching.currentColumn() in range(0, 4) or ui.s_tbl_data_stretching.currentColumn() == 8:
        ui.s_pb_hint_changing_data_stretching.setVisible(False)
        ui.s_tbl_data_stretching.setGeometry(20, 100, 871, 391)

        msg_box.warning(Sport,
                        'Изменение данных',
                        'Данные столбцы не подлежат изменению:\n\n'
                        '"Неделя №";\n'
                        '"День №";\n'
                        '"№ позы";\n'
                        '"Асана";\n'
                        '"Дата".\n\n'
                        'Будьте внимательны!')
    else:
        global tbl_data_text_before_change

        # Запись значения в ячейке до изменения,
        # чтобы в дальнейшем при некорректном введенном значения выставить исходное значение
        current_row = ui.s_tbl_data_stretching.currentRow()
        current_column = ui.s_tbl_data_stretching.currentColumn()
        tbl_data_text_before_change = ui.s_tbl_data_stretching.item(current_row, current_column).text()

        # Отображение подсказки по поводу допустимого значения в корректируемой ячейке
        # в зависимости от активного столбца
        match current_column:
            case 4:
                ui.s_tbl_data_stretching.setGeometry(20, 100, 871, 351)
                ui.s_pb_hint_changing_data_stretching.setVisible(True)

                asana = Asana()
                asana.name = ui.s_tbl_data_stretching.item(current_row, 3).text()

                if asana.sides_quantity == 1:
                    ui.s_pb_hint_changing_data_stretching.setText(f'Сторона у асаны "{asana.name}" может быть равной '
                                                                  f'только "О".')
                elif asana.sides_quantity == 2:
                    ui.s_pb_hint_changing_data_stretching.setText(f'Сторона у асаны "{asana.name}" может быть равной '
                                                                  f'только "Л" или "П".')
            case 5 | 6:
                ui.s_tbl_data_stretching.setGeometry(20, 100, 871, 351)
                ui.s_pb_hint_changing_data_stretching.setVisible(True)
                ui.s_pb_hint_changing_data_stretching.setText('Время работы и время отдыха может быть только целым '
                                                              'числом от 0 до 127.')
            case 7:
                ui.s_pb_hint_changing_data_stretching.setVisible(False)
                ui.s_tbl_data_stretching.setGeometry(20, 100, 871, 391)


def s_update_data_stretching():
    current_row = ui.s_tbl_data_stretching.currentRow()
    current_column = ui.s_tbl_data_stretching.currentColumn()

    # Проверка того, что выбрана какая-либо ячейка
    if current_row != -1:
        cell_new_text = ui.s_tbl_data_stretching.item(current_row, current_column).text()

        # Определение колонки, в которой происходят изменения
        match current_column:
            case 4:
                asana = Asana()
                asana.name = ui.s_tbl_data_stretching.item(current_row, 3).text()

                # Проверка количества сторон у асаны
                if asana.sides_quantity == 1:
                    # Проверка корректности введенного значения
                    if cell_new_text == 'О':
                        db_sport.update_data_stretching(int(ui.s_tbl_data_stretching.item(current_row, 2).text()),
                                                        ui.s_tbl_data_stretching.item(current_row, 3).text(),
                                                        ui.s_tbl_data_stretching.item(current_row, 8).text(),
                                                        current_column,
                                                        ui.s_tbl_data_stretching.item(current_row,
                                                                                      current_column).text(),
                                                        0)
                    else:
                        msg_box_incorrect_value(f'Сторона у асаны "{asana.name}" может быть равной только "О".')

                        ui.s_tbl_data_stretching.item(current_row, current_column).setText(tbl_data_text_before_change)
                elif asana.sides_quantity == 2:
                    # Проверка корректности введенного значения
                    if cell_new_text == 'Л' or cell_new_text == 'П':
                        db_sport.update_data_stretching(int(ui.s_tbl_data_stretching.item(current_row, 2).text()),
                                                        ui.s_tbl_data_stretching.item(current_row, 3).text(),
                                                        ui.s_tbl_data_stretching.item(current_row, 8).text(),
                                                        current_column,
                                                        ui.s_tbl_data_stretching.item(current_row,
                                                                                      current_column).text(),
                                                        0)
                    else:
                        msg_box_incorrect_value(f'Сторона у асаны "{asana.name}" может быть равной только "Л" или "П".')

                        ui.s_tbl_data_stretching.item(current_row, current_column).setText(tbl_data_text_before_change)
            case 5 | 6:
                # Проверка корректности введенного значения
                if cell_new_text.isdigit() and not (len(cell_new_text) >= 2 and cell_new_text[0] == '0'):
                    if int(cell_new_text) < 128:
                        db_sport.update_data_stretching(int(ui.s_tbl_data_stretching.item(current_row, 2).text()),
                                                        ui.s_tbl_data_stretching.item(current_row, 3).text(),
                                                        ui.s_tbl_data_stretching.item(current_row, 8).text(),
                                                        current_column,
                                                        'Пусто',
                                                        int(ui.s_tbl_data_stretching.item(current_row,
                                                                                          current_column).text()))
                    else:
                        msg_box_incorrect_value('Время работы и время отдыха может быть\n'
                                                'только целым числом от 0 до 127.')

                        ui.s_tbl_data_stretching.item(current_row, current_column).setText(tbl_data_text_before_change)
                else:
                    msg_box_incorrect_value('Время работы и время отдыха может быть\n'
                                            'только целым числом от 0 до 127.')

                    ui.s_tbl_data_stretching.item(current_row, current_column).setText(tbl_data_text_before_change)
            case 7:
                db_sport.update_data_stretching(int(ui.s_tbl_data_stretching.item(current_row, 2).text()),
                                                ui.s_tbl_data_stretching.item(current_row, 3).text(),
                                                ui.s_tbl_data_stretching.item(current_row, 8).text(),
                                                current_column,
                                                ui.s_tbl_data_stretching.item(current_row, current_column).text(),
                                                0)


# Страница "Статистика". GroupBox "Критерий"
def s_rb_asanas_on_the_sides_clicked():
    result = db_sport.get_statistics('s_asanas_on_the_sides_quantity')

    ui.s_tbl_statistics.clear()

    ui.s_tbl_statistics.setRowCount(len(result))
    ui.s_tbl_statistics.setColumnCount(3)
    ui.s_tbl_statistics.setHorizontalHeaderLabels([
        'Асана',
        'Сторона',
        'Количество выполнений'
    ])

    fill_table(result, ui.s_tbl_statistics)


def s_rb_last_training_asana_clicked():
    result = db_sport.get_statistics('last_training_asana')

    ui.s_tbl_statistics.clear()

    ui.s_tbl_statistics.setRowCount(len(result))
    ui.s_tbl_statistics.setColumnCount(2)
    ui.s_tbl_statistics.setHorizontalHeaderLabels([
        'Асана',
        'Количество прошедших дней',
    ])

    fill_table(result, ui.s_tbl_statistics)


app = QtWidgets.QApplication(sys.argv)
Sport = QtWidgets.QMainWindow()
ui = Ui_Sport()
ui.setupUi(Sport)

# ОБЩЕЕ
# Создание необходимых экземпляров классов
db_sport = DatabaseSport()
msg_box = QtWidgets.QMessageBox()
tbl_data_text_before_change = None

# ГЛАВНАЯ
# Привязка событий с функциями
ui.pb_open_close_main_menu.clicked.connect(open_or_close_main_menu)
ui.pb_home.clicked.connect(page_home_activate)
ui.pb_yoga.clicked.connect(page_yoga_activate)
ui.pb_workout.clicked.connect(page_workout_activate)
ui.pb_stretching.clicked.connect(page_stretching_activate)
ui.pb_creature.clicked.connect(page_from_auxiliary_menu_activate)
ui.pb_viewing.clicked.connect(page_from_auxiliary_menu_activate)
ui.pb_statistic.clicked.connect(page_from_auxiliary_menu_activate)

# Заполнение виджетов значениями
form_training_schedule()

# ЙОГА
# Страница "Создание". GroupBox "Описание"
ui.y_l_error_choose_side.setVisible(False)
# Страница "Просмотр"
ui.y_pb_hint_changing_data_yoga.setVisible(False)
ui.y_tbl_data_yoga.setGeometry(20, 110, 871, 381)

# Создание необходимых экземпляров классов
last_page_yoga = None
yoga = Yoga()
minimum_date_yoga = QtCore.QDate()
connect_y_update_data_yoga = False

# Привязка событий с функциями
# Страница "Создание". GroupBox "Этап"
ui.y_sb_week_number.textChanged.connect(week_number_value_changed)
ui.y_sb_day_number.textChanged.connect(day_number_value_changed)
ui.y_cw_yoga.clicked.connect(date_changed)
# Страница "Создание". GroupBox "Описание"
ui.y_cb_complex.currentTextChanged.connect(y_complex_name_changed)
ui.y_cb_specialization.currentTextChanged.connect(y_specialization_name_changed)
ui.y_rb_left_side.clicked.connect(y_side_changed)
ui.y_rb_right_side.clicked.connect(y_side_changed)
# Страница "Создание". Кнопки
ui.y_pb_save.clicked.connect(y_insert_data_yoga)
ui.y_pb_clear.clicked.connect(y_clear_data_on_page_creature)
# Страница "Просмотр". GroupBox "Этап"
ui.y_cb_week_number.currentTextChanged.connect(cb_week_number_text_changed)
ui.y_cb_day_number.currentTextChanged.connect(cb_day_number_text_changed)
# Страница "Просмотр"
ui.y_tbl_data_yoga.cellPressed.connect(y_tbl_data_yoga_cellPressed)
# Страница "Статистика". Groupbox "Критерий"
ui.y_rb_complexes.clicked.connect(y_rb_complexes_clicked)
ui.y_rb_specializations.clicked.connect(y_rb_specializations_clicked)
ui.y_rb_asanas_on_the_sides.clicked.connect(y_rb_asanas_on_the_sides_clicked)
ui.y_rb_week_number.clicked.connect(y_rb_week_number_clicked)
ui.y_rb_day_number.clicked.connect(y_rb_day_number_clicked)
ui.y_rb_last_training_complex.clicked.connect(y_rb_last_training_complex_clicked)
ui.y_rb_last_training_specialization.clicked.connect(y_rb_last_training_specialization_clicked)

# Установка на время текущей страницы, чтобы не прописывать условие, когда происходит инициализация
ui.stackedWidget.setCurrentWidget(ui.y_page_creature)
# Заполнение виджетов значениями
# Страница "Создание". GroupBox "Этап"
# Номер недели и номер дня
form_week_numbers()
set_value_sb_week_number(yoga.week_numbers, ui.y_sb_week_number)
# Дата
form_minimum_date()
ui.y_cw_yoga.setMinimumDate(minimum_date_yoga)
ui.y_cw_yoga.setSelectedDate(ui.y_cw_yoga.minimumDate())
yoga.date = ui.y_cw_yoga.selectedDate().getDate()
# Страница "Создание". GroupBox "Описание"
# Комплекс, специализация и асаны
for element in yoga.complexes:
    ui.y_cb_complex.addItem(element.name)
# Страница "Просмотр". GroupBox "Этап"
# Номер недели и номер дня
ui.y_cb_week_number.addItem('Все')
ui.y_cb_week_number.addItems(yoga.week_numbers)
# Страница "Создание". GroupBox "Этап"

# ТРЕНИРОВКА
# Страница "Создание". GroupBox "Описание"
ui.w_l_error_choose_base_weight.setVisible(False)
# Страница "Просмотр"
ui.w_pb_hint_changing_data_workout.setVisible(False)
ui.w_tbl_data_workout.setGeometry(20, 100, 871, 391)

# Создание необходимых экземпляров классов
last_page_workout = None
workout = Workout()
minimum_date_workout = QtCore.QDate()
warm_up_1 = Approach()
warm_up_2 = Approach()
pre_worker = Approach()
worker_1 = Approach()
worker_2 = Approach()
connect_w_update_data_workout = False

warm_up_1.name = 'Разминка 1'
warm_up_2.name = 'Разминка 2'
pre_worker.name = 'Предрабочий'
worker_1.name = 'Рабочий 1'
worker_2.name = 'Рабочий 2'

# Привязка событий с функциями
# Страница "Создание". GroupBox "Этап"
ui.w_sb_week_number.textChanged.connect(week_number_value_changed)
ui.w_sb_day_number.textChanged.connect(day_number_value_changed)
ui.w_cb_mesocycle.currentTextChanged.connect(w_mesocycle_name_changed)
ui.w_cb_microcycle.currentTextChanged.connect(w_microcycle_name_changed)
ui.w_cw_workout.clicked.connect(date_changed)
# Страница "Создание". Кнопки
ui.w_pb_save.clicked.connect(w_insert_data_workout)
ui.w_pb_clear.clicked.connect(w_clear_data_on_page_creature)
# Страница "Создание". GroupBox "Описание"
ui.w_cb_muscle_group.currentTextChanged.connect(w_muscle_group_name_changed)
ui.w_cb_muscle.currentTextChanged.connect(w_muscle_name_changed)
ui.w_cb_exercise.currentTextChanged.connect(w_exercise_name_changed)
ui.w_cb_side.currentTextChanged.connect(w_side_changed)
ui.w_dsb_base_weight.textChanged.connect(w_base_weight_value_changed)
# Страница "Просмотр". GroupBox "Этап"
ui.w_cb_week_number.currentTextChanged.connect(cb_week_number_text_changed)
ui.w_cb_day_number.currentTextChanged.connect(cb_day_number_text_changed)
# Страница "Просмотр"
ui.w_tbl_data_workout.cellPressed.connect(w_tbl_data_workout_cellPressed)
# Страница "Статистика". Groupbox "Критерий"
ui.w_rb_muscle_groups.clicked.connect(w_rb_muscle_groups_clicked)
ui.w_rb_muscles.clicked.connect(w_rb_muscles_clicked)
ui.w_rb_exercises_on_the_sides.clicked.connect(w_rb_exercises_on_the_sides_clicked)
ui.w_rb_week_number.clicked.connect(w_rb_week_number_clicked)
ui.w_rb_day_number.clicked.connect(w_rb_day_number_clicked)
ui.w_rb_last_training_muscle_group.clicked.connect(w_rb_last_training_muscle_group_clicked)
ui.w_rb_last_training_muscle.clicked.connect(w_rb_last_training_muscle_clicked)
ui.w_rb_last_training_exercise.clicked.connect(w_rb_last_training_exercise_clicked)

# Установка на время текущей страницы, чтобы не прописывать условие, когда происходит инициализация
ui.stackedWidget.setCurrentWidget(ui.w_page_creature)
# Заполнение виджетов значениями
# Страница "Создание". GroupBox "Этап"
# Номер недели и номер дня
form_week_numbers()
set_value_sb_week_number(workout.week_numbers, ui.w_sb_week_number)
# Мезоцикл и микроцикл
for element in workout.mesocycles:
    ui.w_cb_mesocycle.addItem(element.name)
# Дата
form_minimum_date()
ui.w_cw_workout.setMinimumDate(minimum_date_workout)
ui.w_cw_workout.setSelectedDate(minimum_date_workout)
workout.date = ui.w_cw_workout.selectedDate().getDate()
# Страница "Создание". GroupBox "Описание"
# Мышечная группа, мышца, упражнение и сторона
for element in workout.muscle_groups:
    ui.w_cb_muscle_group.addItem(element.name)
# Страница "Просмотр". GroupBox "Этап"
# Номер недели и номер дня
ui.w_cb_week_number.addItem('Все')
ui.w_cb_week_number.addItems(workout.week_numbers)

# Специально самостоятельно вызываю этот метод, чтобы корректно выставлялись значения мезоцикла и микроцикла
day_number_value_changed()

# РАСТЯЖКА
# Страница "Создание". GroupBox "Описание"
ui.s_lstw_asana.setGeometry(160, 170, 381, 111)
ui.s_l_error_choose_asana.setVisible(False)
ui.s_l_error_choose_side.setVisible(False)
# Страница "Просмотр"
ui.s_pb_hint_changing_data_stretching.setVisible(False)
ui.s_tbl_data_stretching.setGeometry(20, 100, 871, 391)

# Создание необходимых экземпляров классов
last_page_stretching = None
stretching = Stretching()
connect_s_update_data_stretching = False

# Привязка событий с функциями
# Страница "Создание". GroupBox "Этап"
ui.s_sb_week_number.textChanged.connect(week_number_value_changed)
ui.s_sb_day_number.textChanged.connect(day_number_value_changed)
# Страница "Создание". GroupBox "Описание"
ui.s_lstw_involved_muscle.currentTextChanged.connect(s_involved_muscle_name_changed)
ui.s_pb_clear_selection.clicked.connect(s_pb_clear_selection_clicked)
ui.s_lstw_asana.doubleClicked.connect(s_add_asana_in_selected_asanas)
ui.s_rb_left_side.clicked.connect(s_side_changed)
ui.s_rb_right_side.clicked.connect(s_side_changed)
# Страница "Создание". Выбранные асаны
ui.s_lstw_selected_asanas.doubleClicked.connect(s_delete_asana_from_selected_asanas)
# Страница "Создание". Кнопки
ui.s_pb_save.clicked.connect(s_insert_data_stretching)
ui.s_pb_clear.clicked.connect(s_clear_data_on_page_creature)
# Страница "Просмотр". GroupBox "Этап"
ui.s_cb_week_number.currentTextChanged.connect(cb_week_number_text_changed)
ui.s_cb_day_number.currentTextChanged.connect(cb_day_number_text_changed)
# Страница "Просмотр"
ui.s_tbl_data_stretching.cellPressed.connect(s_tbl_data_stretching_cellPressed)
# Страница "Статистика". Groupbox "Критерий"
ui.s_rb_asanas_on_the_sides.clicked.connect(s_rb_asanas_on_the_sides_clicked)
ui.s_rb_last_training_asana.clicked.connect(s_rb_last_training_asana_clicked)

# Установка на время текущей страницы, чтобы не прописывать условие, когда происходит инициализация
ui.stackedWidget.setCurrentWidget(ui.s_page_creature)
# Заполнение виджетов значениями
# Страница "Создание". GroupBox "Этап"
# Номере недели и номер дня
ui.s_sb_week_number.setValue(ui.w_sb_week_number.value())
ui.s_sb_day_number.setValue(ui.w_sb_day_number.value())
# Страница "Создание". GroupBox "Описание"
# Задействованная мышца
for element in stretching.involved_muscles:
    ui.s_lstw_involved_muscle.addItem(element.name)
# Асана
stretching.asanas.clear()
stretching.asanas._form_dict('asanas', 'Гибкость 1')
for element in stretching.asanas:
    ui.s_lstw_asana.addItem(element.name)
ui.s_lstw_asana.takeItem(ui.s_lstw_asana.count() - 1)
stretching.asanas.clear()
stretching.asanas._form_dict('asanas', 'Гибкость 2')
for element in stretching.asanas:
    ui.s_lstw_asana.addItem(element.name)
ui.s_lstw_asana.takeItem(ui.s_lstw_asana.count() - 1)
stretching.asanas.clear()
stretching.asanas._form_dict('asanas', 'Гибкость 3')
for element in stretching.asanas:
    ui.s_lstw_asana.addItem(element.name)
ui.s_lstw_asana.takeItem(ui.s_lstw_asana.count() - 1)
# Страница "Просмотр". GroupBox "Этап"
# Номер недели и номер дня
form_week_numbers()
ui.s_cb_week_number.addItem('Все')
ui.s_cb_week_number.addItems(stretching.week_numbers)

# Установка страницы "Главная" активной при инициализации
page_home_activate()

Sport.show()
sys.exit(app.exec_())
