from colorama import Fore
import sys


name = '''
                                                  _                 _             _   _               
  _ __    _   _    __ _   _ __    _ __           (_)  _ __    ___  | |_    __ _  | | | |   ___   _ __ 
 | '_ \  | | | |  / _` | | '_ \  | '_ \          | | | '_ \  / __| | __|  / _` | | | | |  / _ \ | '__|
 | |_) | | |_| | | (_| | | |_) | | |_) |    _    | | | | | | \__ \ | |_  | (_| | | | | | |  __/ | |   
 | .__/   \__, |  \__,_| | .__/  | .__/    (_)   |_| |_| |_| |___/  \__|  \__,_| |_| |_|  \___| |_|   
 |_|      |___/          |_|     |_|                                                                  
'''           

descr = '''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+         Добро пожаловать в программу "pyapp installer". Ответьте на несколько вопросов,         +
+                      чтобы настроить скрипт для дальнейшей работы                               +
+                                 Для выхода нажмите Ctrl + C                                     +
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

options = '''
[1] - Выполнить настройку
[2] - Запустить скрипт
[3] - Выйти из программы
'''

version_with_name = "pyapp-installer ver. 0.1"

def welcome_screen(type: str):
    """
    Функция отображения экрана приветствия.

    Parameters:
        type (str): Тип экрана приветствия. Может быть 'full' или 'simple'.
    
    Returns:
        None
    """
    if type == "full":
        print(Fore.BLUE + name + Fore.RESET)
        print(Fore.MAGENTA + "", descr + Fore.RESET)
    elif type == "simple":
        print(Fore.BLUE + name + Fore.RESET)



def update_shell_script_line(varname: str, arg: str):
    updated = False
    filename = "python_appinstaller.sh"
    with open(filename, "r+") as file:
        lines = file.readlines()
        file.seek(0)  # Вернуться в начало файла для записи
        for i, line in enumerate(lines):
            if varname in line:
                if varname == "DIRECTORY":
                    lines[i] = f'DIRECTORY="{arg}"\n'
                elif varname == "APPNAME":
                    lines[i] = f'APPNAME="{arg}"\n'
                elif varname == "MAINFILE":
                    lines[i] = f'MAINFILE="{arg}"\n'
                elif varname == "GITUSERNAME":
                    lines[i] = f'GITUSERNAME="{arg}"\n'
                elif varname == "REPO_TYPE":
                    lines[i] = f'REPO_TYPE="{arg}"\n'
                elif varname == "TOKEN":
                    lines[i] = f'TOKEN="{arg}"\n'
                updated = True
                break
        
        if not updated and varname == "REPO_TYPE":
            if private:
                lines.append(f'REPO_TYPE="private"\n')
            else:
                lines.append(f'REPO_TYPE="public"\n')
            updated = True

        file.writelines(lines)
        file.truncate()  # Обрезать файл до текущей позиции курсора
    if updated:
        print(f"Данные успешно обновлены в файле {filename}.")
    else:
        print(f"Не удалось найти строку с переменной {varname} для обновления.")

    

def update_shell_script(data_dict: dict, repo_type: str):
    """
    Обновляет указанный shell-скрипт данными введенными пользователем.

    Args:
    repo_type (str): Тип репозитория ('public' или 'private').
    username (str): Имя пользователя GitHub.
    token (str): Персональный токен GitHub.
    directory (str): Путь к каталогу.

    Returns:
    None
    """

    # Читаем содержимое файла
    with open("python_appinstaller.sh", "r") as file:
        lines = file.readlines()

    # Ищем строки, которые нужно заменить
    for i, line in enumerate(lines):
        if line.startswith("DIRECTORY"):
            lines[i] = f'DIRECTORY="{data_dict['directory']}"\n'
        elif line.startswith("APPNAME"):
            lines[i] = f'APPNAME="{data_dict['appname']}"\n'
        elif line.startswith("USERNAME"):
            lines[i] = f'USERNAME="{data_dict['gitusername']}"\n'
        elif line.startswith("REPO_TYPE"):
            lines[i] = f'REPO_TYPE="{data_dict['repo_type']}"\n'
        if repo_type == "1":
            if line.startswith("TOKEN"):
                lines[i] = f'TOKEN="{data_dict['token']}"\n'
            
    # Записываем обновленные строки обратно в файл
    with open("python_appinstaller.sh", "w") as file:
        file.writelines(lines)
    print("Данные успешно обновлены в файле данные.sh.")


def setup_script():
    data_dict ={}
    data_dict["directory"] = input("Укажите директорию куда будет распакован проект\n ---> ")
    data_dict["appname"] = input("Укажите название проекта [Где смотреть: https: //github.com/UserName/Название_вашего_проекта.git]\n ---> ")
    data_dict["gitusername"] = input("Укажите имя пользователя на github [Где смотреть: https: //github.com/ВАШЕ_ИМЯ_ПОЛЬЗОВАТЕЛЯ/ВАШ_ПРОЕКТ.git]\n ---> ")
    repo_type = input("Укажите тип репозитория в котором находиться проект\n1 - Private (Приватный)\n2 - Public (Публичный)\n ---> ")
    if repo_type == "1":
            data_dict["repo_type"] = "private"
            data_dict["token"] = input(f"Введите персональный токен на github\n[Как получить: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens]\n ---> ")
    else:
        data_dict["repo_type"] = "public"
    print("\n\n" + Fore.GREEN + "Проверим наши настройки:" +"\n\n" + Fore.RESET)
    print("Директория для распаковки: " + Fore.YELLOW + data_dict["directory"] + Fore.RESET)
    print("Название проекта: " + Fore.YELLOW + data_dict["appname"] + Fore.RESET)
    print("Имя пользователя на github: " + Fore.YELLOW + data_dict["gitusername"] + Fore.RESET)
    print("Тип репозитория: " + Fore.YELLOW + data_dict["repo_type"] + Fore.RESET)
    if repo_type == "1":
        print("Ваш персональный токен на github: " + Fore.YELLOW + data_dict["token"] + Fore.RESET)
    check = input("\n\n" + Fore.GREEN + "Введенные Вами данные верны?" + Fore.RESET +  "\n\n(1) - Да, сохраняем!\n(2) - Нет, переделываем!\n(3) - Выйти без сохранения\n" + Fore.GREEN +  "---> " + Fore.RESET)
    if check == "1":
       update_shell_script(data_dict=data_dict, repo_type=repo_type)
       return True
    elif check == "2":
        setup_script()
    else:
        return True