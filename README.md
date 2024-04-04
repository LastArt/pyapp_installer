![Logo](https://i.imgur.com/h6FyoA5.png) 
# pyapp_installer
### Автоматизация развёртывания Python-приложений
pyapp_installer представляет собой **bash скрипт** для быстрого развёртывания простых программ, написанных на Python, вместе с их окружением и зависимостями. Этот инструмент идеально подходит, когда необходимо развернуть одно и то же приложение на множестве серверов, а Docker-ом пользоваться не хочется.


## 📖 Как это работает

Процесс работы с **pyapp_installer** прост и интуитивен. Прежде всего, вам нужно настроить файл в соответствии с вашим проектом. Затем вы можете запускать этот файл на каждом устройстве, где планируете использовать ваш сервис. 
Загрузка файла на сервер может осуществляться любым удобным для вас способом. После запуска скрипт автоматически выполнит все рутинные процедуры, необходимые для установки и развёртывания вашего сервиса.

### Подготовка

Прежде чем приступить к работе, выполните следующие шаги:

1. Скачайте файл скрипта с GitHub
```bash
  git clone https://github.com/LastArt/pyapp_installer.git
```
2. Пройдите первичную настройку по шагам или запустите программу с флагами (см. 🚩 Флаги)

3. Сохраните исполняемый файл на флеш носителе или диске. 

4. Теперь при необходимости развернуть приложение на Вашем рабочем сервере, просто перенесите файл удобным способом и запустите .

## 📀 Установка

Установка Вашего проекта при помощи файла может быть 2-мя способами:
#### Перенос исполнительного файла с сервера на сервер удобным способой (метод подходит при отсутствие интернет соединения)

1. Скачайте файл скрипта с GitHub чтобы подготовить его к переносу на рабочие сервера
```bash
  git clone https://github.com/LastArt/pyapp_installer.git
```
2. Пройдите первичную настройку по шагам

3. Сохраните исполняемый файл на флеш носителе. 

4. Теперь при необходимости можно развернуть приложение на Вашем рабочем сервере, просто запустив его с внешнего носителя.

#### На каждом рабочем сервере где предполагается развернуть программу, скачивается программа c github (метод подходит при наличие интернет соединения)

1. Находясь на сервере на котором предполагается развернуть Ваше приложение, скачайте файл скрипта с GitHub
```bash
  git clone https://github.com/LastArt/pyapp_installer.git
```
2. Запустите программу с использованием флагов (см. 🚩 Флаги)


## 🚩 Флаги

Используемые в скрипте флаги

| Флаги                    | Описание                                                            |
| :--------------------    | :-------------------------------------------------------------      |
| `-d` `--dir`             | Директория для разворачивания Вашего приложения                     |
| `-a` `--app`             | Название вашего проекта в github                                    |
| `-f` `--file`            | Имя главного файла Вашей программы без .py                          |
| `-u` `--user`            | Имя пользователя github                                             |
| `-p` `--private`         | Определяет тип репозитория как **private**                          |
| `-k` `--key`             | Персональный токен ползователя github если указан флаг -p --private |

*-k --key необходимо вводить, только если Вы указали тип репозитория  **private**
как получить персональный токен можно почитать [вот тут](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

### Пример использования:
#### 1️⃣ Если Ваша программа находиться в приватном репозитории (тип репозитория private)
```bash
./pyappinstaller -d '/usr/me/myfolder' -a 'my_project' -f 'main' -u 'MyGithubUserName' -p  -k 'your_token'
```
#### 2️⃣ Если Ваша программа находиться в публичном репозитории (тип репозитория public)
```bash
./pyappinstaller -d '/usr/me/myfolder' -a 'my_project' -f 'main' -u 'MyGithubUserName' 
```
