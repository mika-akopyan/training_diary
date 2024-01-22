import os


def ui_to_py():
    """Конвертирует все файлы с расширением 'ui' в 'py'"""
    path = os.getcwd()

    os.chdir(path)

    for item in os.scandir(path):
        if item.is_file():
            if item.name[len(item.name)-3:] == '.ui':
                os.system(f'pyuic5 {item.name} -o {item.name[0:-3]}.py')


def qrc_to_py():
    """Конвертирует все файлы с расширением 'qrc' в 'py'"""
    path = os.getcwd()

    os.chdir(path)

    for item in os.scandir(path):
        if item.is_file():
            if item.name[len(item.name)-4:] == '.qrc':
                os.system(f'pyrcc5 {item.name} -o {item.name[0:-4]}_rc.py')


qrc_to_py()
ui_to_py()
