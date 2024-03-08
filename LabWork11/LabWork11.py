import math
import tkinter as tk

def f1(x):
    try:
        if x:
            return math.sqrt(float(x))
        else:
            return ''
    except ValueError:
        print('Нельзя брать отрицательное значение')

def f2(x):
    try:
        if x:
            return 1/float(x)
        else:
            return ''
    except ZeroDivisionError:
        print('Нельзя делить на 0')

def f3(x):
    try:
        if x == '':
            x = 0
        return math.exp(float(x))
        
    except Exception:
        pass

def f123(x):
    return f1(f2(f3(x)))
def f132(x):
    return f1(f3(f2(x)))
def f213(x):
    return f2(f1(f3(x)))
def f231(x):
    return f2(f3(f1(x)))
def f312(x):
    return f3(f1(f2(x)))
def f321(x):
    return f3(f2(f1(x)))

def button_clicked1(label, entry):
    x = entry.get()
    entry.delete(0, tk.END)
    label.config(text = f123(x))
def button_clicked2(label, entry):
    x = entry.get()
    entry.delete(0, tk.END)
    label.config(text = f132(x))
def button_clicked3(label, entry):
    x = entry.get()
    entry.delete(0, tk.END)
    label.config(text = f213(x))
def button_clicked4(label, entry):
    x = entry.get()
    entry.delete(0, tk.END)
    label.config(text = f231(x))
def button_clicked5(label, entry):
    x = entry.get()
    entry.delete(0, tk.END)
    label.config(text = f312(x))
def button_clicked6(label, entry):
    x = entry.get()
    entry.delete(0, tk.END)
    label.config(text = f321(x))

def main():
    root = tk.Tk()

    label1 = tk.Label(root, text="Список функций: 1)sqrt(x) 2)1/x 3)e^x")
    label1.pack()

    root.geometry('650x100+450+350')

    text_entry = tk.Entry(root)
    text_entry.pack()

    label = tk.Label(root, text="Ответ: ")
    label.pack()

    button_frame = tk.Frame(root)
    button_frame.pack()

    button1 = tk.Button(button_frame, text=f"F1(F2(F3(x)))", command=lambda: button_clicked1(label, text_entry))
    button1.pack(side=tk.LEFT)
    button2 = tk.Button(button_frame, text=f"F1(F3(F2(x)))", command=lambda: button_clicked2(label, text_entry))
    button2.pack(side=tk.LEFT)
    button3 = tk.Button(button_frame, text=f"F2(F1(F3(x)))", command=lambda: button_clicked3(label, text_entry))
    button3.pack(side=tk.LEFT)
    button4 = tk.Button(button_frame, text=f"F2(F3(F1(x)))", command=lambda: button_clicked4(label, text_entry))
    button4.pack(side=tk.LEFT)
    button5 = tk.Button(button_frame, text=f"F3(F1(F2(x)))", command=lambda: button_clicked5(label, text_entry))
    button5.pack(side=tk.LEFT)
    button6 = tk.Button(button_frame, text=f"F3(F2(F1(x)))", command=lambda: button_clicked6(label, text_entry))
    button6.pack(side=tk.LEFT)

    root.mainloop()

if __name__ == '__main__':
    main()
