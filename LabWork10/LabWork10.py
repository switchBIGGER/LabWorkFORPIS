import sqlite3
import pandas as pd


def create_sample_database(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Склад (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Товар TEXT,
            Количество INTEGER,
            Цена_товара REAL
        )
    ''')

    cursor.executemany('''
        INSERT INTO Склад (Товар, Количество, Цена_товара) VALUES (?, ?, ?)
    ''', [
        ('Утюг', 134, 4996.0),
        ('Пылесос', 56, 24569.0),
        ('Нож-кредитка', 798, 120.0)
    ])

    conn.commit()
    conn.close()

def main():
    db_file = "Warehouse.db"
    create_sample_database(db_file)

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    product = input("Введите товар: ")

    query = f'SELECT * FROM Склад WHERE Товар = ?'
    cursor.execute(query, (product,))
    rows = cursor.fetchall()

    if rows:
        df = pd.DataFrame(rows, columns=['ID', 'Товар', 'Количество', 'Цена_товара'])

        print(df)

     
        col_sum1 = df['Количество'].sum()
        col_sum2 = df['Цена_товара'].sum()
        print(f'Количество: {col_sum1}')
        print(f'Цена: {col_sum2}')
    else:
        print("Такого товара в базе данных нет")

    conn.close()

if __name__ == '__main__':
    main()