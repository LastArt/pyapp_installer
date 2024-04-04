from utils import * 
from argparser import argparser_do
import sys
import subprocess
from tqdm import tqdm

  
def main():
    welcome_screen()
    print(Fore.GREEN + options + Fore.RESET)
    input_result = input("Ожидание ввода ---> ")
    if input_result == "1":
        res = setup_script()
        if res:
            main()
    elif input_result == "2":
        subprocess.run(["bash", "./python_appinstaller.sh"])
    elif input_result == "3":
        print("До скорых встреч!")
        sys.exit()


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        welcome_screen(type="simple")
        # Запускаем скрипт .sh с помощью tqdm для отображения прогресс-бара
        with tqdm(total=100, desc='Выполнение скрипта .sh', unit='%') as pbar:
            subprocess.run(["bash", "./python_appinstaller.sh"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            pbar.update(100)
    else:
        argparser_do()
        main()