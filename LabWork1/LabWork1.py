import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def srez(string):
    str1 = string[1:]
    str2 = str1[::-1]
    str3 = str2[2:]
    str4 = str3[::-1]
    return str4


def calc_money(model, quantity, name):
    quant = db.c.execute('''SELECT comment FROM users WHERE Name=?''',
                         (name,))
    quantt = str(quant.fetchall()[0])
    vel = srez(quantt)
    quanttt = int(vel.replace("'", '')) + int(quantity)

    fam = db.c.execute('''SELECT Surname FROM users WHERE Name=?''',
                         (name,))
    fam = str(fam.fetchall()[0])
    fam = srez(fam).replace("'", '')
    
    ot = db.c.execute('''SELECT Surname FROM users WHERE Name=?''',
                         (name,))
    ot = str(ot.fetchall()[0])
    ot = srez(ot).replace("'", '')

    price = db2.c.execute('''SELECT price FROM products WHERE model=?''',
                         (model,))
    price = str(price.fetchall()[0])
    price = srez(price).replace("'", '')

    db.c.execute(f'''UPDATE users SET comment=? WHERE Name=?''',
                          (quanttt, name))
    db.conn.commit()
    test = db2.c.execute('''SELECT quantity FROM products WHERE model=?''',
                         (model,))
    testt = str(test.fetchall()[0])
    testtt = srez(testt)

    pop = int(testtt.replace("'", '')) - int(quantity) 
    if pop < 0:
        messagebox.showerror("Error", "Недостаточно товара на складе!")
    else:
        db2.c.execute('''UPDATE products SET quantity=? WHERE model=?''',
                          (pop, model))
        db2.conn.commit()

    db3.insert_data(fam, name, ot, model, quantity, price)

def credit_card(model, quantity, name):
    quant = db.c.execute('''SELECT comment FROM users WHERE Name=?''',
                         (name,))
    quantt = str(quant.fetchall()[0])
    vel = srez(quantt)
    quanttt = int(vel.replace("'", '')) + int(quantity)

    fam = db.c.execute('''SELECT Surname FROM users WHERE Name=?''',
                         (name,))
    fam = str(fam.fetchall()[0])
    fam = srez(fam).replace("'", '')
    
    ot = db.c.execute('''SELECT Surname FROM users WHERE Name=?''',
                         (name,))
    ot = str(ot.fetchall()[0])
    ot = srez(ot).replace("'", '')

    price = db2.c.execute('''SELECT price FROM products WHERE model=?''',
                         (model,))
    price = str(price.fetchall()[0])
    price = srez(price).replace("'", '')

    tek = db.c.execute('''SELECT now FROM users WHERE Name=?''',
                         (name,))
    tek = str(tek.fetchall()[0])
    tek = srez(tek).replace("'", '')
    total = int(tek) - (int(quantity) * int(price))
    db.c.execute(f'''UPDATE users SET now=? WHERE Name=?''',
                          (total, name))
    
    db.c.execute(f'''UPDATE users SET comment=? WHERE Name=?''',
                          (quanttt, name))
    db.conn.commit()
    test = db2.c.execute('''SELECT quantity FROM products WHERE model=?''',
                         (model,))
    testt = str(test.fetchall()[0])
    testtt = srez(testt)

    pop = int(testtt.replace("'", '')) - int(quantity) 
    if pop < 0:
        messagebox.showerror("Error", "Недостаточно товара на складе!")
    else:
        db2.c.execute('''UPDATE products SET quantity=? WHERE model=?''',
                          (pop, model))
        db2.conn.commit()

    db3.insert_data(fam, name, ot, model, quantity, price)

def credit_pay(model, quantity, name): 
    quant = db.c.execute('''SELECT comment FROM users WHERE Name=?''',
                         (name,))
    quantt = str(quant.fetchall()[0])
    vel = srez(quantt)
    quanttt = int(vel.replace("'", '')) + int(quantity)

    fam = db.c.execute('''SELECT Surname FROM users WHERE Name=?''',
                         (name,))
    fam = str(fam.fetchall()[0])
    fam = srez(fam).replace("'", '')
    
    ot = db.c.execute('''SELECT Surname FROM users WHERE Name=?''',
                         (name,))
    ot = str(ot.fetchall()[0])
    ot = srez(ot).replace("'", '')

    price = db2.c.execute('''SELECT price FROM products WHERE model=?''',
                         (model,))
    price = str(price.fetchall()[0])
    price = srez(price).replace("'", '')

    tek = db.c.execute('''SELECT now FROM users WHERE Name=?''',
                         (name,))
    tek = str(tek.fetchall()[0])
    tek = srez(tek).replace("'", '')
    total = int(tek) - (int(quantity) * int(price))
    plus_credit = 0
    if total <= 0:
        plus_credit = abs(total)
        total = 0 
  
    potolok = db.c.execute('''SELECT potolok FROM users WHERE Name=?''',
                         (name,))
    
    potolok = str(potolok.fetchall()[0])
    potolok = srez(potolok).replace("'", '')

    now_cost = db.c.execute('''SELECT now_cost FROM users WHERE Name=?''',
                         (name,))
    
    now_cost = str(now_cost.fetchall()[0])
    now_cost = srez(now_cost).replace("'", '')

    credit = db.c.execute('''SELECT credit FROM users WHERE Name=?''',
                         (name,))
    
    credit = str(credit.fetchall()[0])
    credit = srez(credit).replace("'", '')

    ost_credit = int(credit) + int(plus_credit)
    if ost_credit >= int(potolok) * 0.9:
        messagebox.showerror("Error", "Ваш кредитный лимит почти исчерпан!")
    else:
        db.c.execute(f'''UPDATE users SET credit=? WHERE Name=?''',
                          (ost_credit, name))
        db.c.execute(f'''UPDATE users SET now=? WHERE Name=?''',
                          (total, name))
    
        db.c.execute(f'''UPDATE users SET comment=? WHERE Name=?''',
                          (quanttt, name))
        db.conn.commit()
        test = db2.c.execute('''SELECT quantity FROM products WHERE model=?''',
                         (model,))
        testt = str(test.fetchall()[0])
        testtt = srez(testt)

        pop = int(testtt.replace("'", '')) - int(quantity) 
        if pop < 0:
            messagebox.showerror("Error", "Недостаточно товара на складе!")
        else:
            db2.c.execute('''UPDATE products SET quantity=? WHERE model=?''',
                          (pop, model))
            db2.conn.commit()

        db3.insert_data(fam, name, ot, model, quantity, price)

def barter_pay(model, tovar, name):

    fam = db.c.execute('''SELECT Surname FROM users WHERE Name=?''',
                         (name,))
    fam = str(fam.fetchall()[0])
    fam = srez(fam).replace("'", '')
    
    ot = db.c.execute('''SELECT Surname FROM users WHERE Name=?''',
                         (name,))
    ot = str(ot.fetchall()[0])
    ot = srez(ot).replace("'", '')

    price1 = db2.c.execute('''SELECT price FROM products WHERE model=?''',
                         (model,))
    price1 = str(price1.fetchall()[0])
    price1 = srez(price1).replace("'", '')

    price2 = db2.c.execute('''SELECT price FROM products WHERE model=?''',
                         (tovar,))
    price2 = str(price2.fetchall()[0])
    price2 = srez(price2).replace("'", '')

    if int(price1) == int(price2):
        quant1 = db2.c.execute('''SELECT quantity FROM products WHERE model=?''',
                         (model,))
        quant1 = str(quant1.fetchall()[0])
        quant1 = srez(quant1).replace("'", '')
        quant1 = int(quant1) - 1

        quant2 = db2.c.execute('''SELECT quantity FROM products WHERE model=?''',
                         (tovar,))
        quant2 = str(quant2.fetchall()[0])
        quant2 = srez(quant2).replace("'", '')
        quant2 = int(quant2) + 1
        
        if quant1 < 0:
            messagebox.showerror("Error", "Недостаточно товара на складе!")
        else:
            db2.c.execute('''UPDATE products SET quantity=? WHERE model=?''',
                          (quant1, model))
            db2.c.execute('''UPDATE products SET quantity=? WHERE model=?''',
                          (quant2, tovar))
            db2.conn.commit()

def netting_pay(model, quantity, name):
    price = db2.c.execute('''SELECT price FROM products WHERE model=?''',
                         (model,))
    price = str(price.fetchall()[0])
    price = srez(price).replace("'", '')

    tek = db.c.execute('''SELECT now_cost FROM users WHERE Name=?''',
                         (name,))
    tek = str(tek.fetchall()[0])
    tek = srez(tek).replace("'", '')

    credit = db.c.execute('''SELECT credit FROM users WHERE Name=?''',
                         (name,))
    
    credit = str(credit.fetchall()[0])
    credit = srez(credit).replace("'", '')

    potolok = db.c.execute('''SELECT potolok FROM users WHERE Name=?''',
                         (name,))
    
    potolok = str(potolok.fetchall()[0])
    potolok = srez(potolok).replace("'", '')

    total_credit = int(potolok) - int(credit)

    rasplata = int(quantity) * int(price) - total_credit
    if rasplata >= 0:
        rasplata -= total_credit
        db.c.execute('''UPDATE users SET credit=? WHERE Name=?''',
                          (potolok, name))
        total = int(tek) + rasplata
        db.c.execute('''UPDATE users SET now_cost=? WHERE Name=?''',
                          (total, name))
    else:
        rasplata = int(credit) + int(quantity) * int(price)
        db.c.execute('''UPDATE users SET credit=? WHERE Name=?''',
                          (rasplata, name))
    
    
    test = db2.c.execute('''SELECT quantity FROM products WHERE model=?''',
                         (model,))
    testt = str(test.fetchall()[0])
    testtt = srez(testt)
    pop = int(testtt.replace("'", '')) + int(quantity) 
    db2.c.execute('''UPDATE products SET quantity=? WHERE model=?''',
                          (pop, model))
    db2.conn.commit()
    db.conn.commit()
    


class Main(tk.Frame):
    def __init__(self, root, db):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        
        btn_open_dialog = tk.Button(toolbar, text='Добавить позицию', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)


        btn_edit_dialog = tk.Button(toolbar, text='Редактировать', bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.LEFT)

        
        btn_delete = tk.Button(toolbar, text='Удалить позицию', bg='#d7d8e0', bd=0, 
                               compound=tk.TOP, command=self.delete_records)
        btn_delete.pack(side=tk.LEFT)

        
        btn_search = tk.Button(toolbar, text='Поиск', bg='#d7d8e0', bd=0, 
                               compound=tk.TOP, command=self.open_search_dialog)
        btn_search.pack(side=tk.LEFT)

        
        btn_refresh = tk.Button(toolbar, text='Обновить', bg='#d7d8e0', bd=0, 
                                compound=tk.TOP, command=self.view_records)
        btn_refresh.pack(side=tk.LEFT)

        btn_create = tk.Button(toolbar, text='Открыть таблицу товаров', bg='#d7d8e0', bd=0, 
                                compound=tk.TOP, command=self.create_second)
        btn_create.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ID', 'Surname', 'Name', 'Secondname', 'total', 'now', 'potolok', 'now_cost', 'credit', 'comment'), height=15, show='headings')

        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('Surname', width=120, anchor=tk.CENTER)
        self.tree.column('Name', width=100, anchor=tk.CENTER)
        self.tree.column('Secondname', width=100, anchor=tk.CENTER)
        self.tree.column('total', width=80, anchor=tk.CENTER)
        self.tree.column('now', width=80, anchor=tk.CENTER)
        self.tree.column('potolok', width=80, anchor=tk.CENTER)
        self.tree.column('now_cost', width=80, anchor=tk.CENTER)
        self.tree.column('credit', width=80, anchor=tk.CENTER)
        self.tree.column('comment', width=80, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('Surname', text='Фамилия')
        self.tree.heading('Name', text='Имя')
        self.tree.heading('Secondname', text='Отчество')
        self.tree.heading('total', text='Общий счет')
        self.tree.heading('now', text='Текущий счет')
        self.tree.heading('potolok', text='Потолок кредита')
        self.tree.heading('now_cost', text='Текущий долг')
        self.tree.heading('credit', text='Остаток кредита')
        self.tree.heading('comment', text='Кол-во покупок')

        self.tree.pack(side=tk.LEFT)

        scroll = tk.Scrollbar(self, command=self.tree.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)

    def records(self, Surname, Name, Secondname, total, now, potolok, now_cost, credit, comment):
        self.db.insert_data(Surname, Name, Secondname, total, now, potolok, now_cost, credit, comment)
        self.view_records()
        names.append(Name)

    def update_record(self, Surname, Name, Secondname, total, now, potolok, now_cost, credit, comment):
        self.db.c.execute(f'''UPDATE {self.db.name} SET Surname=?, Name=?, Secondname=?, total=?, now=?, potolok=?, now_cost=?, credit=?, comment=? WHERE ID=?''',
                          (Surname, Name, Secondname, total, now, potolok, now_cost, credit, comment, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        self.db.c.execute(f'''SELECT * FROM {self.db.name}''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]
        self.tree.get_children()

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute(f'''DELETE FROM {self.db.name} WHERE id=?''', (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_records()

    def search_records(self, Name):
        Name = ('%' + "%" + Name + '%' + '%' + '%' + '%' + '%' + '%' + '%', )
        self.db.c.execute(f'''SELECT * FROM {self.db.name} WHERE Name LIKE ?''',  Name)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]
    def open_dialog(self):
        Child(self)

    def open_update_dialog(self):
        Update(self)

    def open_search_dialog(self):
        Search(self)
    def create_second(self):
        window = Products(db2, self)
        window.title('Товары')
        window.geometry('665x370+870+10')
        window.resizable(False, False)


class Child(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.init_child()
        self.view = master

    def init_child(self):
        self.title('Добавить пользователя')
        self.geometry('400x360+90+150')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Фамилия:')
        label_description.place(x=50, y=50)
        label_select = tk.Label(self, text='Имя:')
        label_select.place(x=50, y=80)
        label_sum = tk.Label(self, text='Отчество:')
        label_sum.place(x=50, y=110)
        label_description = tk.Label(self, text='Общий счет:')
        label_description.place(x=50, y=140)
        label_select = tk.Label(self, text='Текущий счет:')
        label_select.place(x=50, y=170)
        label_sum = tk.Label(self, text='Потолок кредита:')
        label_sum.place(x=50, y=200)
        label_description = tk.Label(self, text='Текущий долг:')
        label_description.place(x=50, y=230)
        label_select = tk.Label(self, text='Остаток кредита:')
        label_select.place(x=50, y=260)
        label_sum = tk.Label(self, text='Кол-во покупок:')
        label_sum.place(x=50, y=290)

        self.entry_fam = ttk.Entry(self)
        self.entry_fam.place(x=200, y=50)


        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=80)


        self.entry_ot = ttk.Entry(self)
        self.entry_ot.place(x=200, y=110)


        self.entry_score = ttk.Entry(self)
        self.entry_score.place(x=200, y=140)

        self.entry_now = ttk.Entry(self)
        self.entry_now.place(x=200, y=170)

        self.entry_pot = ttk.Entry(self)
        self.entry_pot.place(x=200, y=200)

        self.entry_tek = ttk.Entry(self)
        self.entry_tek.place(x=200, y=230)

        self.entry_ost = ttk.Entry(self)
        self.entry_ost.place(x=200, y=260)

        self.entry_com = ttk.Entry(self)
        self.entry_com.place(x=200, y=290)


        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=320)



        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=320)

        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_fam.get(),
                                                                       self.entry_name.get(),
                                                                       self.entry_ot.get(),
                                                                       self.entry_score.get(),
                                                                       self.entry_now.get(),
                                                                       self.entry_pot.get(),
                                                                       self.entry_tek.get(),
                                                                       self.entry_ost.get(),
                                                                       self.entry_com.get()) if len(self.entry_com.get()) != 0 and len(self.entry_fam.get()) != 0 and
            len(self.entry_name.get()) != 0 and len(self.entry_tek.get()) != 0 and 
            len(self.entry_ost.get()) != 0 and len(self.entry_score.get()) != 0 and
            len(self.entry_ot.get()) != 0 and len(self.entry_pot.get()) != 0 and
            len(self.entry_ost.get()) != 0 and 
            self.entry_now.get().isdigit() and self.entry_score.get().isdigit() and self.entry_pot.get().isdigit() and self.entry_tek.get().isdigit() and self.entry_ost.get().isdigit()
            else messagebox.showerror("Error", "Данные введены неверно!"))


        self.grab_set()
        self.focus_set()



class Update(Child):
    def __init__(self, master):
        super().__init__(master)
        self.init_edit()
        self.view = master

    def init_edit(self):
        self.title('Редактировать позицию')
        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=205, y=320)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_fam.get(),
                                                                       self.entry_name.get(),
                                                                       self.entry_ot.get(),
                                                                       self.entry_score.get(),
                                                                       self.entry_now.get(),
                                                                       self.entry_pot.get(),
                                                                       self.entry_tek.get(),
                                                                       self.entry_ost.get(),
                                                                       self.entry_com.get()) if len(self.entry_com.get()) != 0 and len(self.entry_fam.get()) != 0 and
            len(self.entry_name.get()) != 0 and len(self.entry_tek.get()) != 0 and 
            len(self.entry_ost.get()) != 0 and len(self.entry_score.get()) != 0 and
            len(self.entry_ot.get()) != 0 and len(self.entry_pot.get()) != 0 and
            len(self.entry_ost.get()) != 0 and 
            self.entry_now.get().isdigit() and self.entry_score.get().isdigit() and self.entry_pot.get().isdigit() and
            self.entry_tek.get().isdigit() and self.entry_ost.get().isdigit() and self.entry_com.get().isdigit()
            else messagebox.showerror("Error", "Данные введены неверно!"))

        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self, master):
        super().__init__()
        self.init_search()
        self.view = master

    def init_search(self):
        self.title('Поиск')
        self.geometry('300x100+90+150')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Поиск')
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Поиск')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')



class Products(tk.Toplevel):
    def __init__(self,db, master):
        super().__init__(master)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar1 = tk.Frame(bg='#d7d8e0', bd=2, master=self)
        toolbar1.pack(side=tk.TOP, fill=tk.X)

        
        btn_open_dialog = tk.Button(toolbar1, text='Добавить позицию', command=self.open_dialog1, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)


        btn_edit_dialog = tk.Button(toolbar1, text='Редактировать', bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.LEFT)

        
        btn_delete = tk.Button(toolbar1, text='Удалить позицию', bg='#d7d8e0', bd=0, 
                               compound=tk.TOP, command=self.delete_records)
        btn_delete.pack(side=tk.LEFT)

        
        btn_search = tk.Button(toolbar1, text='Поиск', bg='#d7d8e0', bd=0, 
                               compound=tk.TOP, command=self.open_search_dialog)
        btn_search.pack(side=tk.LEFT)

        
        btn_refresh = tk.Button(toolbar1, text='Обновить', bg='#d7d8e0', bd=0, 
                                compound=tk.TOP, command=self.view_records)
        btn_refresh.pack(side=tk.LEFT)

        btn_refresh = tk.Button(toolbar1, text='Заказать', bg='#d7d8e0', bd=0, 
                                compound=tk.TOP, command=self.open_order)
        btn_refresh.pack(side=tk.LEFT)

        btn_create = tk.Button(toolbar1, text='Открыть таблицу заказов', bg='#d7d8e0', bd=0, 
                                compound=tk.TOP, command=self.create_second)
        btn_create.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ID', 'brand', 'model', 'price', 'quantity', 'comment'), height=15, show='headings')

        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('brand', width=110, anchor=tk.CENTER)
        self.tree.column('model', width=100, anchor=tk.CENTER)
        self.tree.column('price', width=100, anchor=tk.CENTER)
        self.tree.column('quantity', width=100, anchor=tk.CENTER)
        self.tree.column('comment', width=200, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('brand', text='Бренд')
        self.tree.heading('model', text='Модель')
        self.tree.heading('price', text='Цена за 1 шт')
        self.tree.heading('quantity', text='Количество на складе')
        self.tree.heading('comment', text='Комментарий')

        self.tree.pack(side=tk.LEFT)

        scroll = tk.Scrollbar(self, command=self.tree.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)

    def records(self, brand, model, price, quantity, comment):
        self.db.insert_data(brand, model, price,quantity, comment)
        values.append(model)
        self.view_records()

    def update_record(self, brand, model, price, quantity, comment):
        self.db.c.execute(f'''UPDATE {self.db.name} SET brand=?,model=?, price=?, quantity=?, comment=? WHERE ID=?''',
                          (brand, model, price, quantity, comment, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        self.db.c.execute(f'''SELECT * FROM {self.db.name}''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute(f'''DELETE FROM {self.db.name} WHERE id=?''', (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_records()

    def search_records(self, model):
        model = ('%' + '%' + model + '%' + '%' + '%',)
        self.db.c.execute(f'''SELECT * FROM {self.db.name} WHERE model LIKE ?''', model)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def create_second(self):
        window = Orders(db3, self)
        window.title('Заказы')
        window.geometry('665x370+50+400')
        window.resizable(False, False)
        window.grab_set()
        window.focus_set()

    def open_dialog1(self):
        Child_Sec(self)

    def open_update_dialog(self):
        Update_Sec(self)

    def open_search_dialog(self):
        Search_Sec(self)
    
    def open_order(self):
        Order(self)


class Child_Sec(tk.Toplevel):
    def __init__(self,master):
        super().__init__(master)
        self.init_child()

    def init_child(self):
        self.title('Добавить товар')
        self.geometry('400x240+950+100')
        self.resizable(False, False)

        label_brand = tk.Label(self, text='Фирма:')
        label_brand.place(x=50, y=50)
        label_model = tk.Label(self, text='Модель:')
        label_model.place(x=50, y=80)
        label_sum = tk.Label(self, text='Цена за 1 шт:')
        label_sum.place(x=50, y=110)
        label_quantity = tk.Label(self, text='Количесто на складе:')
        label_quantity.place(x=50, y=140)
        label_comm = tk.Label(self, text='Комментарий:')
        label_comm.place(x=50, y=170)

        self.entry_brand = ttk.Entry(self)
        self.entry_brand.place(x=200, y=50)

        self.entry_model = ttk.Entry(self)
        self.entry_model.place(x=200, y=80)

        self.entry_sum = ttk.Entry(self)
        self.entry_sum.place(x=200, y=110)

        self.entry_quantity = ttk.Entry(self)
        self.entry_quantity.place(x=200, y=140)

        self.entry_comm = ttk.Entry(self)
        self.entry_comm.place(x=200, y=170)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=200)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=200)
        self.btn_ok.bind('<Button-1>', lambda event: self.master.records(self.entry_brand.get(),
                                                                       self.entry_model.get(),
                                                                       self.entry_sum.get(),
                                                                       self.entry_quantity.get(),
                                                                       self.entry_comm.get())  if len(self.entry_brand.get()) != 0 and len(self.entry_model.get()) != 0 and
            len(self.entry_sum.get()) != 0 and len(self.entry_quantity.get()) != 0 and 
            len(self.entry_comm.get()) != 0 and
            self.entry_sum.get().isdigit() and self.entry_quantity.get().isdigit() 
            else messagebox.showerror("Error", "Данные введены неверно!"))

        self.grab_set()
        self.focus_set()

class Update_Sec(Child_Sec):
    def __init__(self, master):
        super().__init__(master)
        self.init_edit()
        self.view = master

    def init_edit(self):
        self.title('Редактировать позицию')

        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=205, y=200)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_brand.get(),
                                                                       self.entry_model.get(),
                                                                       self.entry_sum.get(),
                                                                       self.entry_quantity.get(),
                                                                       self.entry_comm.get()) if len(self.entry_brand.get()) != 0 and len(self.entry_model.get()) != 0 and
            len(self.entry_sum.get()) != 0 and len(self.entry_quantity.get()) != 0 and 
            len(self.entry_comm.get()) != 0 and
            self.entry_sum.get().isdigit() and self.entry_quantity.get().isdigit() 
            else messagebox.showerror("Error", "Данные введены неверно!"))
        self.btn_ok.destroy()

class Search_Sec(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.init_search()
        self.view = master

    def init_search(self):
        self.title('Поиск')
        self.geometry('300x100+950+100')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Поиск')
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Поиск')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

class Order(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.init_order()
        self.view = master

    def init_order(self):
        self.title('Заказ')
        self.geometry('200x120+900+450')
        self.resizable(False, False)

        
        choise = ['money', 'credit card', 'credit', 'barter', 'netting']
        self.combobox = ttk.Combobox(self, values=choise)
        self.combobox.current(0)
        self.combobox.place(x = 30, y = 40)

        btn_order = ttk.Button(master = self, text='Далее')
        btn_order.place(x=30, y=80)
        btn_order.bind('<Button-1>', lambda event: self.checkcmbo())
    def checkcmbo(self):
        if self.combobox.get() == 'money':
            money = Calculation_money(self)
            money.btn_ok.bind('<Button-1>', lambda event: calc_money(money.combobox1.get(), money.entry_quant.get(),  money.combobox2.get()))

        elif self.combobox.get() == "credit card":
            card = Calculation_money(self)
            card.btn_ok.bind('<Button-1>', lambda event: credit_card(card.combobox1.get(), card.entry_quant.get(),  card.combobox2.get()))

        elif self.combobox.get() == "credit":
            credit = Calculation_money(self)
            credit.btn_ok.bind('<Button-1>', lambda event: credit_pay(credit.combobox1.get(), credit.entry_quant.get(),  credit.combobox2.get()))

        elif self.combobox.get() == "barter":
            barter = Calculation_barter(self)
            barter.btn_ok.bind('<Button-1>', lambda event: barter_pay(barter.combobox1.get(), barter.combobox.get(),  barter.combobox2.get()))

        elif self.combobox.get() == "netting":
            netting = Calculation_money(self)
            netting.btn_ok.bind('<Button-1>', lambda event: netting_pay(netting.combobox1.get(), netting.entry_quant.get(),  netting.combobox2.get()))

        
class Calculation(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.init_calc()

    def init_calc(self):
        self.title('Добавить товар')
        self.geometry('400x220+1100+450')
        self.resizable(False, False)

        label_model = tk.Label(self, text='Товар:')
        label_model.place(x=100, y=50)
        
        label_quant = tk.Label(self, text='Пользователь:')
        label_quant.place(x=100, y=110)

        self.combobox1 = ttk.Combobox(self, values=values)
        self.combobox1.current(0)
        self.combobox1.place(x = 200, y = 50)

        

        self.combobox2 = ttk.Combobox(self, values=names)
        self.combobox2.current(0)
        self.combobox2.place(x = 200, y = 110)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=180)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=180) 



class Calculation_money(Calculation):
    def __init__(self, master):
        super().__init__(master)
        self.init_money()
        self.view = master
    def init_money(self):
        label_quant = tk.Label(self, text='Количество:')
        label_quant.place(x=100, y=80)
        self.entry_quant = ttk.Entry(self)
        self.entry_quant.place(x=200, y=80)

class Calculation_barter(Calculation):
    def __init__(self, master):
        super().__init__(master)
        self.init_money()
        self.view = master
    def init_money(self):
        label_quant = tk.Label(self, text='Ваш товар:')
        label_quant.place(x=100, y=80)
        self.combobox = ttk.Combobox(self, values=values)
        self.combobox.current(0)
        self.combobox.place(x = 200, y = 80)



class Orders(tk.Toplevel):
    def __init__(self,db, master):
        super().__init__(master)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar1 = tk.Frame(bg='#d7d8e0', bd=2, master=self)
        toolbar1.pack(side=tk.TOP, fill=tk.X)

        
        btn_search = tk.Button(toolbar1, text='Поиск', bg='#d7d8e0', bd=0, 
                               compound=tk.TOP, command=self.open_search_dialog)
        btn_search.pack(side=tk.LEFT)

        
        btn_refresh = tk.Button(toolbar1, text='Обновить', bg='#d7d8e0', bd=0, 
                                compound=tk.TOP, command=self.view_records)
        btn_refresh.pack(side=tk.LEFT)

        btn_delete = tk.Button(toolbar1, text='Удалить позицию', bg='#d7d8e0', bd=0, 
                               compound=tk.TOP, command=self.delete_records)
        btn_delete.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ID', 'Surname', 'Name', 'Secondname',  'model', 'quantity', 'price'), height=15, show='headings')

        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('Surname', width=130, anchor=tk.CENTER)
        self.tree.column('Name', width=100, anchor=tk.CENTER)
        self.tree.column('Secondname', width=130, anchor=tk.CENTER)
        self.tree.column('model', width=90, anchor=tk.CENTER)
        self.tree.column('quantity', width=80, anchor=tk.CENTER)
        self.tree.column('price', width=80, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('Surname', text='Фамилия')
        self.tree.heading('Name', text='Имя')
        self.tree.heading('Secondname', text='Отчество')
        self.tree.heading('model', text='Модель')
        self.tree.heading('quantity', text='Количество')
        self.tree.heading('price', text='Цена')

        self.tree.pack(side=tk.LEFT)

        scroll = tk.Scrollbar(self, command=self.tree.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)

    def view_records(self):
        self.db.c.execute(f'''SELECT * FROM {self.db.name}''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]


    def search_records(self, Name):
        Name = ('%' + '%' + Name + '%' + '%' + '%',)
        self.db.c.execute(f'''SELECT * FROM {self.db.name} WHERE Name LIKE ?''', Name)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute(f'''DELETE FROM {self.db.name} WHERE id=?''', (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_records()

    def open_search_dialog(self):
        Search_Orders(self)


class Search_Orders(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.init_search()
        self.view = master

    def init_search(self):
        self.title('Поиск')
        self.geometry('300x100+300+500')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Поиск')
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Поиск')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')



class DB_users():
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect(f'{self.name}.db')
        self.c = self.conn.cursor()
        self.c.execute(
            f'''CREATE TABLE IF NOT EXISTS {self.name} (id integer primary key, Surname text, Name text,
              Secondname text, total int, now int, potolok int, now_cost int, credit int, comment text )''')
        self.conn.commit()

    def insert_data(self, Surname, Name, Secondname, total, now, potolok, now_cost, credit, comment):
        self.c.execute(f'''INSERT INTO {self.name}(Surname, Name, Secondname, total, now, potolok, now_cost, credit, comment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (Surname, Name, Secondname, total, now, potolok, now_cost, credit, comment))
        self.conn.commit()

class DB_products():
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect(f'{self.name}.db')
        self.c = self.conn.cursor()
        self.c.execute(
            f'''CREATE TABLE IF NOT EXISTS {self.name} (id integer primary key, brand text, model text, price int, quantity int, comment text)''')
        self.conn.commit()

    def insert_data(self,brand, model, price, quantity, comment):
        self.c.execute(f'''INSERT INTO {self.name}(brand, model, price, quantity, comment) VALUES (?, ?, ?, ?, ?)''',
                       (brand, model, price, quantity, comment))
        self.conn.commit()

class DB_orders():
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect(f'{self.name}.db')
        self.c = self.conn.cursor()
        self.c.execute(
            f'''CREATE TABLE IF NOT EXISTS {self.name} (id integer primary key, Surname text, Name text,
              Secondname text, model text, quantity int, price int)''')
        self.conn.commit()

    def insert_data(self, Surname, Name, Secondname,  model, quantity, price):
        self.c.execute(f'''INSERT INTO {self.name}(Surname, Name, Secondname, model, quantity, price) VALUES (?, ?, ?, ?, ?, ?)''',
                       (Surname, Name, Secondname,  model, quantity, price))
        self.conn.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB_users('users')
    db2 = DB_products('products')
    db3 = DB_orders('orders')
    app = Main(root,db)
    app.pack()
    values = list(db2.c.execute('''SELECT model FROM products'''))
    names = list(db.c.execute('''SELECT Name FROM users'''))
    root.title("Пользователи")
    root.geometry("865x370+10+10")
    root.resizable(False, False)
    root.mainloop()
