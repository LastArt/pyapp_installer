from utils import * 
from argparser import argparser_do
import sys
import subprocess
from tqdm import tqdm

  
def main():
    welcome_screen(type='full')
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
        argparser_do(sys.argv[1:])
        subprocess.run(["bash", "./python_appinstaller.sh"])
    else:
        #argparser_do()
        main()