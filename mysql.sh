sudo /etc/init.d/mysql start

mysql -uroot -e "CREATE DATABASE qa"
mysql -uroot -e "CREATE USER 'django'@'localhost' IDENTIFIED BY 'ask'"
mysql -uroot -e "GRANT ALL ON qa.* TO 'django'@'localhost'"

# python ask/manage.py validate
# python ask/manage.py sql qa

python ask/manage.py syncdb
