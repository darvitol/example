import sqlite3 as sql

# Подключение к БД
connection = sql.connect('test.sqlite')

# Создание курсора
q = connection.cursor()

# Текст запроса
# q.execute('''CREATE TABLE user (id int auto_increment primary key, name varchar, password varchar )''')

# Выполнение запроса
# connection.commit()

user_name = input("Введите Ваше имя: ")
user_password = input("Введите пароль: ")

print("Список пользователей:\n")
q.execute("INSERT INTO user (name, password) VALUES ('%s', '%s')" % (user_name, user_password))
connection.commit()

q.execute("SELECT * FROM user")
row = q.fetchone()

while row is not None:
    print("Name: ", row[1], "| Password", row[2])
    row = q.fetchone()

# Отключение БД
q.close()
connection.close()
