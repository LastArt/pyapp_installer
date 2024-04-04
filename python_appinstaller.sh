#!/bin/bash

# Цвета
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

# Переменные для хранения аргументов
DIRECTORY="/ack"
APPNAME="Time-Inspector"
MAINFILE="timeInspector"
GITUSERNAME="LastArt"
REPO_TYPE="public"
TOKEN=""

# Проверка наличия sudo прав и запрос пароля, если необходимо
if [ "$EUID" -ne 0 ]; then
    sudo "$0" "$@"
    exit $?
fi

# Проверяем наличие данных в переменных
if [ -z "$DIRECTORY" ] || [ -z "$APPNAME" ] || [ -z "$MAINFILE" ] || [ -z "$GITUSERNAME" ] || [ -z "$REPO_TYPE" ]; then
    echo -e "${RED}Ошибка: не все данные заполнены.${NC}"
    exit 1
fi

# Выводим сообщение о начале установки
echo -e "${GREEN}Начало установки.${NC}"

# Проверяем существует ли уже каталог
if [ -d "$DIRECTORY/$APPNAME" ]; then
    echo -e "${YELLOW}Удаление существующего каталога${NC}"
    if [ "$(ls -A $DIRECTORY/$APPNAME)" ]; then
        rm -rf "$DIRECTORY/$APPNAME"
    else
        echo -e "${GREEN}Каталог $DIRECTORY/$APPNAME уже пуст.${NC}"
    fi
fi

# Создаем каталог, если он не существует
if [ ! -d "$DIRECTORY" ]; then
    echo -e "${GREEN}Создание каталога $DIRECTORY.${NC}"
    mkdir -p "$DIRECTORY"
fi

# Переходим в целевую директорию
cd "$DIRECTORY/" || exit

# Устанавливаем Git и Python
echo -e "${GREEN}Установка Git и Python.${NC}"
apt update
apt install -y git python3 python3-venv

# Создаем виртуальное окружение и активируем его
echo -e "${GREEN}Создание и активация виртуального окружения.${NC}"
python3 -m venv venv
source venv/bin/activate

# Обновляем pip
echo -e "${GREEN}Обновление pip.${NC}"
pip install --upgrade pip

# Клонируем репозиторий с программой
echo -e "${GREEN}Клонирование репозитория.${NC}"
if [ "$REPO_TYPE" = "private" ]; then
    git clone "https://$GITUSERNAME:$TOKEN@github.com/$GITUSERNAME/$APPNAME.git"
else
    git clone "https://github.com/$GITUSERNAME/$APPNAME.git"
fi

# Переходим в папку клонированного репозитория
cd "$APPNAME/" || exit

# Устанавливаем разрешение для записи в log.txt
chmod 777 log.txt

# Устанавливаем зависимости из requirements.txt
echo -e "${GREEN}Установка зависимостей из requirements.txt.${NC}"
pip install -r requirements.txt

# Создаем systemd-файл службы
echo -e "${GREEN}Создание файла службы systemd.${NC}"
cat << EOF > "/etc/systemd/system/$MAINFILE.service"
[Unit]
Description=Controller Service
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=$DIRECTORY/$APPNAME
ExecStart=$DIRECTORY/$APPNAME/python3 $MAINFILE.py
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
EOF

# Перезагружаем демон systemd
echo -e "${GREEN}Перезагрузка демона systemd.${NC}"
systemctl daemon-reload

# Выводим сообщение о завершении установки
echo -e "${GREEN}Установка завершена.${NC}"

# Включаем и запускаем службу
echo -e "${GREEN}Включение и запуск службы.${NC}"
systemctl enable "$MAINFILE"
systemctl start "$MAINFILE"



