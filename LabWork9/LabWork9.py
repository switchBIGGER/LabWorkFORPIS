import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def main():
    try:
        conn = sqlite3.connect('transport.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Автомобили
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Марка_автомобиля TEXT,
                        Гос_номер_автомобиля TEXT,
                        Год_выпуска INTEGER,
                        Норма_расхода_литров_на_1_км REAL)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Водители
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Сотрудник INTEGER,
                        Автомобиль INTEGER,
                        FOREIGN KEY (Сотрудник) REFERENCES Сотрудники(ID),
                        FOREIGN KEY (Автомобиль) REFERENCES Автомобили(ID))''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Путевые_листы
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Водитель INTEGER,
                        Автомобиль INTEGER,
                        Время_выезда DATETIME,
                        Время_заезда DATETIME,
                        Начальный_километраж REAL,
                        Конечный_километраж REAL,
                        Пробег REAL,
                        Расход_топлива REAL,
                        FOREIGN KEY (Водитель) REFERENCES Водители(ID),
                        FOREIGN KEY (Автомобиль) REFERENCES Автомобили(ID))''')


        cursor.execute('''INSERT INTO Автомобили (Марка_автомобиля, Гос_номер_автомобиля, Год_выпуска, Норма_расхода_литров_на_1_км)
                        VALUES ('Марка1', 'Гос_номер1', 2010, 10.5)''')
        cursor.execute('''INSERT INTO Автомобили (Марка_автомобиля, Гос_номер_автомобиля, Год_выпуска, Норма_расхода_литров_на_1_км)
                        VALUES ('Марка2', 'Гос_номер2', 2015, 8.2)''')
        cursor.execute('''INSERT INTO Автомобили (Марка_автомобиля, Гос_номер_автомобиля, Год_выпуска, Норма_расхода_литров_на_1_км)
                        VALUES ('Марка3', 'Гос_номер3', 2014, 7)''')


        cursor.execute('''INSERT INTO Водители (Сотрудник, Автомобиль)
                        VALUES (1, 1)''')
        cursor.execute('''INSERT INTO Водители (Сотрудник, Автомобиль)
                        VALUES (2, 1)''')
        cursor.execute('''INSERT INTO Водители (Сотрудник, Автомобиль)
                        VALUES (3, 2)''')
        cursor.execute('''INSERT INTO Водители (Сотрудник, Автомобиль)
                        VALUES (3, 3)''')

        cursor.execute('''INSERT INTO Путевые_листы (Водитель, Автомобиль, Время_выезда, Время_заезда, Начальный_километраж, Конечный_километраж)
                        VALUES (1, 1, '2023-05-17 08:00:00', '2023-05-17 16:00:00', 900, 1200)''')
        cursor.execute('''INSERT INTO Путевые_листы (Водитель, Автомобиль, Время_выезда, Время_заезда, Начальный_километраж, Конечный_километраж)
                        VALUES (2, 1, '2023-05-18 09:00:00', '2023-05-18 17:00:00', 1400, 1500)''')
        cursor.execute('''INSERT INTO Путевые_листы (Водитель, Автомобиль, Время_выезда, Время_заезда, Начальный_километраж, Конечный_километраж)
                        VALUES (3, 2, '2023-05-17 10:00:00', '2023-05-17 18:00:00', 1000, 2200)''')
        cursor.execute('''INSERT INTO Путевые_листы (Водитель, Автомобиль, Время_выезда, Время_заезда, Начальный_километраж, Конечный_километраж)
                        VALUES (3, 3, '2023-05-17 10:00:00', '2023-05-17 18:00:00', 2000, 2200)''')

        df = pd.read_sql_query("SELECT Путевые_листы.*, Автомобили.Норма_расхода_литров_на_1_км FROM Путевые_листы INNER JOIN Автомобили ON Путевые_листы.Автомобиль = Автомобили.ID", conn)

        df = df.assign(Пробег=df['Конечный_километраж'] - df['Начальный_километраж'])

        df = df.assign(Расход_топлива=df['Пробег'] * df['Норма_расхода_литров_на_1_км'])


        # Группировка данных по водителям
        avg_mileage_by_driver = df.groupby('Водитель')['Пробег'].sum()

        # Группировка данных по автомобилям
        avg_fuel_consumption_by_car = df.groupby('Автомобиль')['Расход_топлива'].sum()

        print(df)

        plt.bar(avg_mileage_by_driver.index, avg_mileage_by_driver.values)
        plt.axhline(y=avg_mileage_by_driver.mean(), color='red', linestyle='--')
        plt.xlabel('Водитель')
        plt.ylabel('Пробег')
        plt.title('Средний пробег по водителям')
        plt.show()

        plt.bar(avg_fuel_consumption_by_car.index, avg_fuel_consumption_by_car.values)
        plt.axhline(y=avg_fuel_consumption_by_car.mean(), color='red', linestyle='--')
        plt.xlabel('Автомобиль')
        plt.ylabel('Расход топлива')
        plt.title('Средний расход топлива по автомобилям')
        plt.show()

    except sqlite3.Error as error:
        print(f'Возникла ошибка: {error}')
    finally:
        if conn:
            conn.close()
            print("Соединение с sqlite3 закрыто")

if __name__ == '__main__':
    main()