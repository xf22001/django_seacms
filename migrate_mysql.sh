#!/bin/bash

#================================================================
#   
#   
#   文件名称：migrate_mysql.sh
#   创 建 者：肖飞
#   创建日期：2020年09月07日 星期一 15时02分50秒
#   修改日期：2020年09月07日 星期一 16时25分41秒
#   描    述：
#
#================================================================
function main() {
	echo "修改配置,连接mysql..."
	read -n 1
	vi seacms/settings.py
	python manage.py inspectdb > models.py
	mv models.py app/

	echo "修改模型中的错误..."
	read -n 1
	vi app/models.py

	python manage.py dumpdata app > seacms.json

	sed -i 's/    managed = False/    managed = True/g' app/models.py
	echo "修改配置,连接sqlite3..."
	read -n 1
	vi seacms/settings.py
	python manage.py makemigrations
	python manage.py migrate
	python manage.py loaddata seacms.json
}

main $@
