import argparse
from utils import * 


def argparser_do():
    parser = argparse.ArgumentParser(description="Time Inspector 1.0 Учет рабочего времени\n"
                                                "с использованием api TimeControl, "
                                                "Все права защищены (с) 2024 \n"
                                                "Манукян Артур <it_doctor82@mail.ru>")

    parser.epilog = ("Пример:\n"
                    "tminspector -d '156400' -o 'Название объекта'")

    parser.add_argument('-h', '--help', action='help', help='показать помощи и выйти')
    parser.add_argument('-v', '--version', action='version', version=version_with_name, help='показать версию программы и выйти')
    parser.add_argument('-d', '--dir', help='Директория для разворачивания Вашего приложения')
    parser.add_argument('-a', '--app', help='Название вашего проекта в github')
    parser.add_argument('-f', '--file', help='Имя главного файла Вашей программы без .py')
    parser.add_argument('-u', '--user', help=' Имя пользователя github')
    parser.add_argument('-p', '--private', action='store_true', help='Определяет тип репозитория как private')
    parser.add_argument('-t', '--token', help='Персональный токен ползователя github если указан флаг -p --private')

    args = parser.parse_args()
    print("Полученные аргументы:", args)

    if args.dir:
        update_shell_script_line("DIRECTORY", args.dir)
    if args.app:
        update_shell_script_line("APPNAME", args.app)
    if args.file:
        update_shell_script_line("MAINFILE", args.file)
    if args.user:
        update_shell_script_line("GITUSERNAME", args.user)
    if args.private:
        update_shell_script_line("REPO_TYPE", "private")
    if args.token:
        update_shell_script_line("TOKEN", args.token)