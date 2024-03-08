import psycopg2
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

hostname = 'localhost'
username = 'postgres'
password = '1234'
database = 'Laba7'

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        
        btn_open_dialog = tk.Button(toolbar, text='Добавить позицию', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)

        
        btn_delete = tk.Button(toolbar, text='Удалить позицию', bg='#d7d8e0', bd=0, 
                               compound=tk.TOP, command=self.delete_records)
        btn_delete.pack(side=tk.LEFT)


        self.tree = ttk.Treeview(self, columns=('id', 'name', 'code', 'number', 'place', 'code_inside'), height=15, show='headings')

        self.tree.column('id', width=30, anchor=tk.CENTER)
        self.tree.column('name', width=120, anchor=tk.CENTER)        
        self.tree.column('code', width=190, anchor=tk.CENTER)
        self.tree.column('number', width=190, anchor=tk.CENTER)
        self.tree.column('place', width=150, anchor=tk.CENTER)
        self.tree.column('code_inside', width=150, anchor=tk.CENTER)

        self.tree.heading('id', text='ID')
        self.tree.heading('name', text='Наименование')
        self.tree.heading('code', text='Код Подразделения')
        self.tree.heading('number', text='Порядковый Номер')
        self.tree.heading('place', text='Место Хранения')
        self.tree.heading('code_inside', text='Код Внутреннего Учета')

        self.tree.pack(side=tk.LEFT)

        scroll = tk.Scrollbar(self, command=self.tree.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)

    def records(self, id, name, code, number, place):
        try:
            cursor = conn.cursor()
            code_inside = int(code) + int(number)
            cursor.execute('''INSERT INTO ОсновныеСредства (ID, Наименование, КодПодразделения, ПорядковыйНомер, МестоХранения, КодВнутреннегоУчета) VALUES (%s, %s, %s, %s, %s, %s)''',
                            (id, name, code, number, place, code_inside))
            conn.commit()
            print("Запись успешно добавлена")
        except (Exception, psycopg2.Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if conn:
                cursor.close()
        self.view_records()

    def view_records(self):
        try:
            cursor = conn.cursor()
            cursor.execute(f'''SELECT * FROM ОсновныеСредства''')
            [self.tree.delete(i) for i in self.tree.get_children()]
            [self.tree.insert('', 'end', values=row) for row in cursor.fetchall()]
            self.tree.get_children()
        except (Exception, psycopg2.Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if conn:
                cursor.close()

    def delete_records(self):
        for selection_item in self.tree.selection():
            try:
                cursor = conn.cursor()
                cursor.execute('''DELETE FROM ОсновныеСредства WHERE ID=%s''', (self.tree.set(selection_item, '#1'),))
            except (Exception, psycopg2.Error) as error:
                print("Ошибка при работе с PostgreSQL", error)
            finally:
                if conn:
                    cursor.close()
        conn.commit()
        self.view_records()

    def open_dialog(self):
        Child(self)

class Child(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.init_child()
        self.view = master

    def init_child(self):
        self.title('Добавить пользователя')
        self.geometry('400x360+90+150')
        self.resizable(False, False)

        label_id = tk.Label(self, text='ID:')
        label_id.place(x=50, y=50)
        label_description = tk.Label(self, text='Наименование:')
        label_description.place(x=50, y=80)
        label_select = tk.Label(self, text='Код подразделения:')
        label_select.place(x=50, y=110)
        label_sum = tk.Label(self, text='Порядковый номер:')
        label_sum.place(x=50, y=140)
        label_description = tk.Label(self, text='Место хранения:')
        label_description.place(x=50, y=170)


        self.entry_id = ttk.Entry(self)
        self.entry_id.place(x=200, y=50)

        self.entry_fam = ttk.Entry(self)
        self.entry_fam.place(x=200, y=80)


        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=110)


        self.entry_ot = ttk.Entry(self)
        self.entry_ot.place(x=200, y=140)


        self.entry_score = ttk.Entry(self)
        self.entry_score.place(x=200, y=170)



        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=320)



        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=320)

        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_id.get(),
                                                                        self.entry_fam.get(),
                                                                       self.entry_name.get(),
                                                                       self.entry_ot.get(),
                                                                       self.entry_score.get(),
                                                                        ) if len(self.entry_fam.get()) != 0 and 
                                                                        len(self.entry_id.get()) != 0 and
            len(self.entry_name.get()) != 0 and len(self.entry_score.get()) != 0 and
            len(self.entry_ot.get()) != 0 and 
            self.entry_name.get().isdigit() and self.entry_ot.get().isdigit() and self.entry_id.get().isdigit()
            else messagebox.showerror("Error", "Данные введены неверно!"))


        self.grab_set()
        self.focus_set()

try:
    conn = psycopg2.connect(
        host=hostname,
        user=username,
        password=password,
        database=database
    )

    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS ОсновныеСредства 
                (ID INT PRIMARY KEY,
                Наименование VARCHAR(255),
                КодПодразделения VARCHAR(255),
                ПорядковыйНомер INT,
                МестоХранения VARCHAR(255),
                КодВнутреннегоУчета VARCHAR(255))
                ''')
    if __name__ == '__main__':
        root = tk.Tk()
        app = Main(root)
        app.pack()
        root.title("Пользователи")
        root.geometry("865x370+10+10")
        root.resizable(False, False)
        root.mainloop()
except psycopg2.Error as error:
    print('Ошибка при подключении к базе данных:', error)
finally:
    cur.close()
    conn.close()
    print('Соединение закрыто')
