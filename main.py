from tkinter import *
from tkinter import ttk
import json
from currency import ruble
import chart
with open('arh.json', 'r') as file:
    value = json.load(file)

def create_window():
    global combobox, window
    window = Tk()     # создаем корневой объект - окно
    window.title("Добро пожаловать")     # устанавливаем заголовок окна

    window.geometry("800x600")
    window.minsize(200,150)   # минимальные размеры
    window.maxsize(1920,1280) # Максимальные размеры
    
    # контекстуальная надпись
    label = Label(text="Выберете курс 1 рубля по отношению к")
    label.pack()

    # выпадающий список
    languages = ["Доллар", "Тенге", "Евро", "Юань", "Шекель", "Йена", "Фунт", "Рупия"]
    label = ttk.Label()
    label.pack()
    combobox = ttk.Combobox(values=languages, state="readonly")
    combobox.pack()
    # Получение данных из выпадающего списка
    combobox.bind("<<ComboboxSelected>>", selected)    
    
    # доюавление данных
    add_button = ttk.Button(text="Добавить курс", command=create_currency)
    add_button.pack()

    label = Label(text='Выбраная валюта:')
    label.pack()    


# Получение данных из выпадающего списка
def selected(event):
    global selection
    selection = combobox.get()    

# добавление валюты
def create_currency():
    global value
    if selection == "Доллар" and value[0] == 0: 
        create_dollar()
        value[0] = 1
        with open('arh.json', 'w') as file:
            json.dump(value, file)
    elif selection == "Тенге" and value[1] == 0: 
        create_tenge()
        value[1] = 1
        with open('arh.json', 'w') as file:
            json.dump(value, file)
    elif selection == "Евро" and value[2] == 0: 
        create_euro()
        value[2] = 1
        with open('arh.json', 'w') as file:
            json.dump(value, file)
    elif selection == "Юань" and value[3] == 0: 
        create_yuan()
        value[3] = 1
        with open('arh.json', 'w') as file:
            json.dump(value, file)
    elif selection == "Шекель" and value[4] == 0: 
        create_shekel()
        value[4] = 1
        with open('arh.json', 'w') as file:
            json.dump(value, file)
    elif selection == "Йена" and value[5] == 0: 
        create_yen()
        value[5] = 1
        with open('arh.json', 'w') as file:
            json.dump(value, file)
    elif selection == "Фунт" and value[6] == 0: 
        create_pound()
        value[6] = 1
        with open('arh.json', 'w') as file:
            json.dump(value, file)
    elif selection == "Рупия" and value[7] == 0: 
        create_rupiah()
        value[7] = 1
        with open('arh.json', 'w') as file:
            json.dump(value, file)


def create_dollar():
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
    widget = Label(frame) 
    widget['text'] = f'1 доллар = {ruble[0]} рублей' 
    widget.pack()
    chart_button = ttk.Button(frame,text="График курса", command=chart.chart_dollar)
    clear_button = ttk.Button(frame,text="Очистить БД", command=clear_doll)
    delete_button = ttk.Button(frame,text="удалить", command=frame.destroy)
    chart_button.pack()
    delete_button.pack()
    clear_button.pack()
    frame.pack()

def create_tenge():
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
    widget = Label(frame)
    widget['text'] = f'1 рубль = {ruble[1]} тенге' 
    widget.pack()
    chart_button = ttk.Button(frame,text="График курса", command=chart.chart_tenge)
    clear_button = ttk.Button(frame,text="Очистить БД", command=clear_teng)
    delete_button = ttk.Button(frame,text="удалить", command=frame.destroy)
    chart_button.pack()
    delete_button.pack()
    clear_button.pack()
    frame.pack()

def create_euro():
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
    widget = Label(frame)
    widget['text'] = f'1 евро = {ruble[2]} рублей' 
    widget.pack()
    chart_button = ttk.Button(frame,text="График курса", command=chart.chart_euro)
    clear_button = ttk.Button(frame,text="Очистить БД", command=clear_eur)
    delete_button = ttk.Button(frame,text="удалить", command=frame.destroy)
    chart_button.pack()
    delete_button.pack()
    clear_button.pack()
    frame.pack()


def create_yuan():
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
    widget = Label(frame)
    widget['text'] = f'1 юань = {ruble[3]} рублей' 
    widget.pack()
    chart_button = ttk.Button(frame,text="График курса", command=chart.chart_yuan)
    clear_button = ttk.Button(frame,text="Очистить БД", command=clear_yua)
    delete_button = ttk.Button(frame,text="удалить", command=frame.destroy)
    chart_button.pack()
    delete_button.pack()
    clear_button.pack()
    frame.pack()

def create_shekel():
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
    widget = Label(frame)
    widget['text'] = f'1 шекель = {ruble[4]} рублей' 
    widget.pack()
    chart_button = ttk.Button(frame,text="График курса", command=chart.chart_shekel)
    clear_button = ttk.Button(frame,text="Очистить БД", command=clear_shek)
    delete_button = ttk.Button(frame,text="удалить", command=frame.destroy)
    chart_button.pack()
    delete_button.pack()
    clear_button.pack()
    frame.pack()

def create_yen():
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
    widget = Label(frame)
    widget['text'] = f'1 рубль = {ruble[5]} йена' 
    widget.pack()
    chart_button = ttk.Button(frame,text="График курса", command=chart.chart_yen)
    clear_button = ttk.Button(frame,text="Очистить БД", command=clear_ye)
    delete_button = ttk.Button(frame,text="удалить", command=frame.destroy)
    chart_button.pack()
    delete_button.pack()
    clear_button.pack()
    frame.pack()

def create_pound():
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
    widget = Label(frame)
    widget['text'] = f'1 фунт стерлингов = {ruble[6]} рублей' 
    widget.pack()
    chart_button = ttk.Button(frame,text="График курса", command=chart.chart_pound)
    clear_button = ttk.Button(frame,text="Очистить БД", command=clear_pou)
    delete_button = ttk.Button(frame,text="удалить", command=frame.destroy)
    chart_button.pack()
    delete_button.pack()
    clear_button.pack()
    frame.pack()

def create_rupiah():
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
    widget = Label(frame)
    widget['text'] = f'1 рупий = {ruble[7]} рублей' 
    widget.pack()
    chart_button = ttk.Button(frame,text="График курса", command=chart.chart_rupiah)
    clear_button = ttk.Button(frame,text="Очистить БД", command=clear_rup)
    delete_button = ttk.Button(frame,text="удалить", command=frame.destroy)
    chart_button.pack()
    delete_button.pack()
    clear_button.pack()
    frame.pack()


def clear_doll():
    global value
    value[0] = 0
    with open('arh.json', 'w') as file:
        json.dump(value, file)

def clear_teng():
    global value
    value[1] = 0
    with open('arh.json', 'w') as file:
        json.dump(value, file)


def clear_eur():
    global value
    value[2] = 0
    with open('arh.json', 'w') as file:
        json.dump(value, file)


def clear_yua():
    global value
    value[3] = 0
    with open('arh.json', 'w') as file:
        json.dump(value, file)


def clear_shek():
    global value
    value[4] = 0
    with open('arh.json', 'w') as file:
        json.dump(value, file)


def clear_ye():
    global value
    value[5] = 0
    with open('arh.json', 'w') as file:
        json.dump(value, file)


def clear_pou():
    global value
    value[6] = 0
    with open('arh.json', 'w') as file:
        json.dump(value, file)


def clear_rup():
    global value
    value[7] = 0
    with open('arh.json', 'w') as file:
        json.dump(value, file)



def save_currency():
    if value[0] == 1: create_dollar()
    if value[1] == 1: create_tenge()
    if value[2] == 1: create_euro()
    if value[3] == 1: create_yuan()
    if value[4] == 1: create_shekel()
    if value[5] == 1: create_yen()
    if value[6] == 1: create_pound()
    if value[7] == 1: create_rupiah()



create_window()
save_currency()

window.mainloop()