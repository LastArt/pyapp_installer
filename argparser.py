import argparse
from utils import * 


def argparser_do(argv=None):
    parser = argparse.ArgumentParser(description="pyappinstaller 0.1 Программа для быстрого развертывания\n"
                                                "сервисов на серверах.\n "
                                                "Все права защищены (с) 2024 \n"
                                                "Манукян Артур <e-mail>")

    parser.epilog = ("Пример:\n"
                    "pyappinstaller -d '/usr/me/myfolder' -a 'my_project' -f 'main' -u 'MyGithubUserName' -p  -k 'your_token'")
    
    parser.add_argument('-v', '--version', action='version', version=version_with_name, help='показать версию программы и выйти')
    parser.add_argument('-d', '--dir', help='Директория для разворачивания Вашего приложения')
    parser.add_argument('-a', '--app', help='Название вашего проекта в github')
    parser.add_argument('-f', '--file', help='Имя главного файла Вашей программы без .py')
    parser.add_argument('-u', '--user', help=' Имя пользователя github')
    parser.add_argument('-p', '--private', action='store_true', help='Определяет тип репозитория как private')
    parser.add_argument('-t', '--token', help='Персональный токен ползователя github если указан флаг -p --private')

    args = parser.parse_args(argv)

    if args.dir is not None:
        update_shell_script_line("DIRECTORY", args.dir)
    if args.app is not None:
        update_shell_script_line("APPNAME", args.app)
    if args.file is not None:
        update_shell_script_line("MAINFILE", args.file)
    if args.user is not None:
        update_shell_script_line("GITUSERNAME", args.user)
    if args.private:
        update_shell_script_line("REPO_TYPE", args.private) #'private'
    if args.token is not None:
        update_shell_script_line("TOKEN", args.token)

    if hasattr(args, 'help'):  # Проверяем, был ли передан аргумент -h/--help
        if args.help:  # Если аргумент -h/--help передан, выводим помощь и завершаем программу
            parser.print_help()
            exit()