import psycopg2
from psycopg2 import Error
from psycopg2 import OperationalError 

def create_connection(db_name, db_user, db_password,db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def log_in():
    primary = int(input('Вы здесь в первый раз?\nЕсли да (гость), нажмите 1, в противном случае нажмите 2: '))
    if (primary == 1):
        con = create_connection('Laba4', 'postgres', '1234', "127.0.0.1", "5432")
    elif(primary == 2):
        user_name = input("Введите login: ")

        user_password = input("Введите пароль: ")
        con = create_connection("Laba4", user_name, user_password, "127.0.0.1", "5432")
    return con

def update_table(connection, directory_id, price):
    try:
        cursor = connection.cursor()
        print("Таблица до обновления записи")
        sql_select_query = """select * from directory """
        cursor.execute(sql_select_query, (directory_id,))
        record = cursor.fetchone()
        print(record)

        # Обновление отдельной записи
        sql_update_query = """Update directory set Имя = %s where directory_id = %s"""
        cursor.execute(sql_update_query, (price, directory_id))
        connection.commit()
        count = cursor.rowcount
        print(count, "Запись успешно обновлена")

        print("Таблица после обновления записи")
        sql_select_query = """select * from directory """
        cursor.execute(sql_select_query, (directory_id,))
        record = cursor.fetchone()
        print(record)        

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


def delete_data(connection, directory_id):
    try:
        cursor = connection.cursor()
        # Удаление записи
        sql_delete_query = """Delete from directory where directory_id = %s"""
        cursor.execute(sql_delete_query, (directory_id,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Запись успешно удалена")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


def insert_data(connection, record_to_insert):
    try:
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO directory (directory_id, Фамилия, Имя, Отчество, Должность, Адрес, Телефон)
                                           VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        print ("Запись успешно добавлена ​​в таблицу directory")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

def select_data(connection):
    try:
        cursor = connection.cursor()
        sql_select_query = """select * from directory"""
        cursor.execute(sql_select_query)
        record = cursor.fetchone()
        print(record)

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


connection = log_in()
if connection:
    print("Что вы хотите сделать с таблицей?\n1)Просмотр таблицы\n2)Добавление записи\n3)Удаление записи\n4)Обновление одной записи: ")
    number = int(input())
    if(number == 1):
        select_data(connection)
    elif(number == 2):
        print("Введите 7 значений для столбцов, начиная с номера строки: ")
        my_list = []
        for i in range(7):
            elem = input()
            my_list.append(elem)
        insert_data(connection, my_list)
    elif(number == 3):
        deleted = int(input("Введите номер строки, кото12рую хотите удалить: "))
        delete_data(connection, deleted)
    elif(number == 4):
        updated = input("Введите строку, которую надо обновить: ")
        print("Введите 7 значений для столбцов, начиная с номера строки: ")
        elem = input("Введите имя: ")
        update_table(connection, updated, elem)