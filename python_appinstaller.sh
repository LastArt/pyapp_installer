#!/bin/bash

# Переменные для хранения аргументов
DIRECTORY=""
APPNAME=""
MAINFILE=""
GITUSERNAME=""
REPO_TYPE=""
TOKEN=""

# Проверяем наличие данных в переменных
if [ -z "$DIRECTORY" ] || [ -z "$APPNAME" ] || [ -z "$GITUSERNAME" ] || [ -z "$REPO_TYPE" ]; then
    echo "Ошибка: не все данные заполнены."
    exit 1
fi

# Проверяем существование каталога, если он не существует, создаем
if [ ! -d "$DIRECTORY" ]; then
    mkdir -p "$DIRECTORY"
fi

# Переходим в созданный нами каталог
cd "$DIRECTORY" || exit

# Устанавливаем Git
apt update
apt install -y git

# Устанавливаем Python 3 и инструмент для создания виртуального окружения
apt install -y python3 python3-venv

# Создаем виртуальное окружение
python3 -m venv venv

# Активируем виртуальное окружение
source venv/bin/activate

# Устанавливаем pip и обновляем его
pip install --upgrade pip

# Устанавливаем PyInstaller
pip install pyinstaller

# Клонируем репозиторий с программой в зависимости от типа (public или private)
if [ -z "$REPO_TYPE" ]; then
    REPO_TYPE="public"
fi

if [ "$REPO_TYPE" = "private" ]; then
    git clone https://$GITUSERNAME:$TOKEN@github.com/$GITUSERNAME/$APPNAME.git
else
    git clone https://github.com/$GITUSERNAME/$APPNAME.git
    exit 1
fi

# Переходим в папку клонированного репозитория
cd $APPNAME || exit

# Устанавливаем зависимости из requirements.txt, который лежит в папке клонированного репозитория
pip install -r requirements.txt

# Компилируем Python-программу в исполняемый файл 
pyinstaller --onefile $MAINFILE.py

# Создаем systemd-файл службы при необходимости с флагами (если не нужны, то просто ExecStart=$DIRECTORY/yourproject/dist/your_programm)
tee /etc/systemd/system/$MAINFILE.service > /dev/null <<EOT
[Unit]
Description=Controller Service
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=$DIRECTORY/$APPNAME
ExecStart=$DIRECTORY/$APPNAME/dist/$MAINFILE
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
EOT

# Перезагружаем демон systemd, чтобы отразить изменения
systemctl daemon-reload

# Включаем и запускаем службу
systemctl enable $MAINFILE
systemctl start $MAINFILE