import sqlite3 as sl

con = sl.connect("gb.db")  # соединяемся с БД , если ее нету, то создаем такую БД
cur = con.cursor()


def create_table():
    # создаем пустую таблицу users со столбцами id, name, age если ее не было в БД
    cur.execute(
        """CREATE TABLE IF NOT EXISTS phonebook (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        surname TEXT,
        phone_number TEXT
    )"""
    )
    con.commit()  # сохраняем изменения


def show_data():
    cur.execute("select * from phonebook")
    output(cur)


def output(cur):
    for row in cur.fetchall():
        print(row)


def add_entry(name, surname, phone_number):
    cur.execute(
        f"select * from phonebook where name = '{name}'AND surname = '{surname}'AND phone_number = '{phone_number}'"
    )
    if not cur.fetchall():
        cur.execute(
            f"INSERT INTO phonebook (name, surname, phone_number) VALUES ('{name}', '{surname}', '{phone_number}')"
        )
        con.commit()


def remove_entry_by_name(name):
    cur.execute(f"delete from phonebook where name = '{name}'")


def remove_entry_by_surname(surname):
    cur.execute(f"delete from phonebook where surname = '{surname}'")


def remove_entry_by_phone_number(phone_number):
    cur.execute(f"delete from phonebook where phone_number = '{phone_number}'")


def search_by_name(name):
    cur.execute(f"select * from phonebook where name = '{name}'")
    output(cur)


def search_by_surname(surname):
    cur.execute(f"select * from phonebook where surname = '{surname}'")
    output(cur)


def search_by_phone_number(phone_number):
    cur.execute(f"select * from phonebook where phone_number = '{phone_number}'")
    output(cur)


create_table()

while True:
    command = input("Введите команду: ")

    if command == "/end":
        break

    if command == "/search_by_name":
        name = input("Введите имя: ")
        search_by_name(name)

    if command == "/search_by_surname":
        surname = input("Введите фамилию: ")
        search_by_name(surname)

    if command == "/search_by_phone_number":
        phone_number = input("Введите номер телефона: ")
        search_by_name(phone_number)

    if command == "/remove_entry_by_name":
        name = input("Введите номер имя: ")
        remove_entry_by_name(name)

    if command == "/remove_entry_by_surname":
        surname = input("Введите номер фамилию: ")
        remove_entry_by_surname(surname)

    if command == "/remove_entry_by_phone_number":
        phone_number = input("Введите номер телефона: ")
        remove_entry_by_phone_number(phone_number)

    if command == "/add_entry":
        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        phone_number = input("Введите номер телефона: ")
        add_entry(name, surname, phone_number)

    if command == "/show_data":
        show_data()