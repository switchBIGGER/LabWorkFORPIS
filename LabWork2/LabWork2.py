import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from random import randint
import matplotlib.pyplot as plt



class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.values = [randint(0,500) for i in range(1000)]
        self.appended = []
        self.cond = []

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        
        btn_open_dialog = tk.Button(toolbar, text='Values', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)

        
        btn_open_cond = tk.Button(toolbar, text='Cond', command=self.open_conditions, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP)
        btn_open_cond.pack(side=tk.LEFT)

        btn_graph = tk.Button(toolbar,text='Graph', command=self.plot_graph, bg='#d7d8e0', bd=0, compound=tk.TOP )
        btn_graph.pack(side=tk.LEFT)

        btn_graph = tk.Button(toolbar,text='Update', command=self.update, bg='#d7d8e0', bd=0, compound=tk.TOP )
        btn_graph.pack(side=tk.LEFT)

        btn_histogram = tk.Button(toolbar, text='Histogram', command=self.plot_histogram, bg='#d7d8e0', bd=0, compound=tk.TOP)
        btn_histogram.pack(side=tk.LEFT)    


        self.tree = ttk.Treeview(self, columns=('ID', 'N1'), height=15, show='headings')

        self.tree.column('ID', width=50, anchor=tk.CENTER)
        self.tree.column('N1', width=120, anchor=tk.CENTER)


        self.tree.heading('ID', text='ID')
        self.tree.heading('N1', text='N1')
  

        self.tree.pack(side=tk.LEFT)

        scroll = tk.Scrollbar(self, command=self.tree.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)
    
    def withdraw_values(self, quantity):
        if self.tree.get_children():
            self.tree.delete(*self.tree.get_children())
        if len(self.appended):  
            for i in range(int(quantity)):
                if abs(self.values[i + len(self.appended)]) > abs(self.appended[i]) * 1.2:
                    value = self.values[i + len(self.appended)]
                    self.tree.insert('', 'end', values=(i+1, value))
                    self.appended.append(value)
                    messagebox.showinfo(title="Информация", message="Значение увеличилось на 20%!")
                else:
                    value = self.values[i + len(self.appended)]
                    self.tree.insert('', 'end', values=(i+1, value))
                    self.appended.append(value)
                    
        else:
            for i in range(int(quantity)):
                value = self.values[i + len(self.appended)]
                self.tree.insert('', 'end', values=(i+1, value))
                self.appended.append(value)

    def plot_graph(self):
        values = []
        for value in self.tree.get_children():
            tem = self.tree.item(value)
            values.append(tem['values'][1])
        plt.plot(values)
        plt.xlabel('Item')
        plt.ylabel('Value')
        plt.title('Treeview Data')
        plt.show()

    def do_cond(self,upper = 0, lower = 0, multiple = 0):
        upper, lower, multiple = float(upper), float(lower), float(multiple)
        if upper != 0 and lower == 0 and multiple == 0:
            self.cond.clear()
            for value in self.tree.get_children():
                tem = self.tree.item(value)
                if upper < float(tem['values'][1]):
                    self.cond.append(tem['values'][1])
            if self.tree.get_children():
                self.tree.delete(*self.tree.get_children())  
            for i in range(len(self.cond)):
                self.tree.insert('', 'end', values=(i+1, self.cond[i]))
        elif lower != 0 and upper == 0 and multiple == 0:
            self.cond.clear()
            for value in self.tree.get_children():
                tem = self.tree.item(value)
                if lower > float(tem['values'][1]):
                    self.cond.append(tem['values'][1])
            if self.tree.get_children():
                self.tree.delete(*self.tree.get_children())  
            for i in range(len(self.cond)):
                self.tree.insert('', 'end', values=(i+1,self.cond[i]))
        elif lower == 0 and upper == 0 and multiple != 0:
            self.cond.clear()
            for value in self.tree.get_children():
                tem = self.tree.item(value)
                if float(tem['values'][1]) % multiple == 0:
                    self.cond.append(tem['values'][1])
            if self.tree.get_children():
                self.tree.delete(*self.tree.get_children())  
            for i in range(len(self.cond)):
                self.tree.insert('', 'end', values=(i+1, self.cond[i]))      
    def plot_histogram(self):
        plt.hist(self.values, bins=10, alpha=0.5, label='values')

        plt.hist(self.cond, bins=10, alpha=0.5, label='cond_values')

        plt.xlabel('Значение')
        plt.ylabel('Частота')
        plt.legend()

        plt.show()
    def update(self):
        if self.tree.get_children():
            self.tree.delete(*self.tree.get_children())  
        for i in range(len(self.appended)):
            self.tree.insert('', 'end', values=(i+1, self.appended[i]))    

    def open_dialog(self):
        Child(self)
    
    def open_conditions(self):
        Cond(self)



class Child(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.init_child()
        self.view = master

    def init_child(self):
        self.title('Quuantity')
        self.geometry('200x130+90+150')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Enter values quantity:')
        label_description.place(x=10, y=50)


        self.entry_X = ttk.Entry(self, width=10)
        self.entry_X.place(x=130, y=50)


        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(x=300, y=320)



        self.btn_ok = ttk.Button(self, text='Withdraw')
        self.btn_ok.place(x=120, y=80)

        self.btn_ok.bind('<Button-1>', lambda event: self.master.withdraw_values(self.entry_X.get()) if len(self.entry_X.get()) != 0 and self.entry_X.get().isdigit()
                         else messagebox.showerror("Error", "Данные введены неверно!") and self.view.withdraw_values(0))


        self.grab_set()
        self.focus_set()

class Cond(tk.Toplevel):
    def __init__(self,master):
        super().__init__(master)
        self.init_cond()
        self.view = master

    def init_cond(self):
        self.title('Выберите условие отбора')
        self.geometry('200x120+500+350')
        self.resizable(False, False)

        
        choise = ['Больше', 'Меньше', 'Кратно']
        self.combobox = ttk.Combobox(self, values=choise)
        self.combobox.current(0)
        self.combobox.place(x = 30, y = 40)

        btn_order = ttk.Button(master = self, text='Enter')
        btn_order.place(x=30, y=80)
        btn_order.bind('<Button-1>', lambda event: self.checkcmbo())
    def checkcmbo(self):
        if self.combobox.get() == 'Меньше':
            low = Lower(self)
            low.btn_ok.bind('<Button-1>', lambda event: self.view.do_cond(lower = low.entry_low.get()) if low.entry_low.get() != 0 and low.entry_low.get().isdigit()
                         else messagebox.showerror("Error", "Данные введены неверно!"))

        elif self.combobox.get() == "Больше":
            up = Upper(self)
            up.btn_ok.bind('<Button-1>', lambda event: self.view.do_cond(upper = up.entry_up.get()) if up.entry_up.get() != 0 and up.entry_up.get().isdigit()
                         else messagebox.showerror("Error", "Данные введены неверно!"))

        elif self.combobox.get() == "Кратно":
            mult = Multiple(self)
            mult.btn_ok.bind('<Button-1>', lambda event: self.view.do_cond(multiple = mult.entry_mult.get()) if  mult.entry_mult.get() != 0 and  mult.entry_mult.get().isdigit()
                         else messagebox.showerror("Error", "Данные введены неверно!"))
        self.grab_set()
        self.focus_set()


class Lower(tk.Toplevel):
    def __init__(self,master):
        super().__init__(master)
        self.init_low()

    def init_low(self):
        self.title("Условие отбора")
        self.geometry('200x120+700+350')
        self.resizable(False,False)

        label_low = tk.Label(self, text='Меньше чем:')
        label_low.place(x=10, y=50)

        self.entry_low = ttk.Entry(self, width=10)
        self.entry_low.place(x=100, y=50)
        self.btn_ok = ttk.Button(self, text='Enter')
        self.btn_ok.place(x=100, y=80) 

class Upper(tk.Toplevel):
    def __init__(self,master):
        super().__init__(master)
        self.init_low()

    def init_low(self):
        self.title("Условие отбора")
        self.geometry('200x120+700+350')
        self.resizable(False,False)

        label_up = tk.Label(self, text='Больше чем:')
        label_up.place(x=10, y=50)

        self.entry_up = ttk.Entry(self, width=10)
        self.entry_up.place(x=100, y=50)
        self.btn_ok = ttk.Button(self, text='Enter')
        self.btn_ok.place(x=100, y=80) 

class Multiple(tk.Toplevel):
    def __init__(self,master):
        super().__init__(master)
        self.init_low()

    def init_low(self):
        self.title("Условие отбора")
        self.geometry('200x120+700+350')
        self.resizable(False,False)

        label_mult = tk.Label(self, text='Кратно:')
        label_mult.place(x=10, y=50)

        self.entry_mult = ttk.Entry(self, width=10)
        self.entry_mult.place(x=100, y=50)
        self.btn_ok = ttk.Button(self, text='Enter')
        self.btn_ok.place(x=100, y=80) 


def main():
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Лабораторная №2")
    root.geometry("240x370+300+100")
    root.resizable(False, False)
    root.mainloop()




if __name__ == "__main__":
    main()