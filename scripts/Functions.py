import random
from tkinter import *
from tkinter import messagebox


# ---------------------------------------------Ініціалізації елементів-------------------------------------------------#
# Оголошуємо list1 як глобальну змінну
list1 = ["You", "can", "change", "this", "strings", ":)"]

text_str = ""  # Ініціалізуємо глобальну змінну



# --------------------------------------------Функція виставлення курсору----------------------------------------------#
def set_cursor(listbox, index):
    listbox.selection_clear(0, END)  # Спочатку скасовуємо виділення всіх елементів
    listbox.selection_set(index)  # Встановлюємо курсор на елементі з вказаним індексом
    listbox.activate(index)  # Активуємо елемент з вказаним індексом




# --------------------------------------------Функція видалення рядку--------------------------------------------------#
def deleteSTR(listbox):
    listbox.delete(listbox.curselection())
    update_Read_List(listbox)






# ------------------------------------------Функції запису і читання даних---------------------------------------------#
def update_Write_List(listbox):
    listbox.delete(0, END)  # Видаляємо всі елементи

    for i in list1:
        listbox.insert(END, i)  # Додаємо елементи у віджет


def update_Read_List(listbox):

    list1 = []

    num_elements = listbox.size()

    for i in range(num_elements):
        list1.append(listbox.get(i))






# ---------------------------------------------Функції обробки натискання "Open"---------------------------------------#
def Open(separatorTree, B_open, listbox):
    enterer = Text(separatorTree, height=5, width=15)

    # Отримуємо індекс вибраного елемента у списку Listbox
    selection_index = listbox.curselection()

    # Перевіряємо, чи вибрано якийсь елемент
    if selection_index:
        # Отримуємо значення індексу з кортежу та виводимо відповідний елемент зі списку list1
        enterer.insert(END, list1[selection_index[0]])
        enterer.grid(row=0, column=0, columnspan=3, sticky='nsew')  # Показуємо віджет

        B_open.config(
            text="Close",
            command=lambda: open_ok(enterer, B_open, separatorTree, listbox, selection_index[0])
        )
    else:
        # Якщо немає вибраного елемента, виводимо повідомлення про помилку
        messagebox.showerror("Error", "Please select an item to edit")

def open_ok(enterer, B_add, separatorTree, listbox, pos):
    global text_str

    selection_index = listbox.curselection()

    text_str = enterer.get("1.0", "end").strip()  # Використовуємо strip(), щоб видалити символи нового рядка
    listbox.insert(END, text_str)

    # Змінюємо елемент у list1 за позицією pos
    list1[pos] = text_str

    # Оновлюємо listbox з новими значеннями
    update_Write_List(listbox)

    B_add.config(
        command=lambda: Open(separatorTree, B_add, listbox),
        text="Open"
    )

    # Оновлюємо listbox після оновлення значення у list1
    update_Read_List(listbox)

    enterer.destroy()





# ----------------------------------------------Функції обробки натискання "Add"---------------------------------------#
def AddSTR(separatorTree, B_add, listbox):
    enterer = Text(separatorTree, height=5, width=15)
    enterer.grid(row=0, column=0, columnspan=3, sticky='nsew')

    B_add.config(
        text="OK, add",
        command=lambda: event_ok(enterer, B_add, separatorTree, listbox)
    )

def event_ok(enterer, B_add, separatorTree, listbox):
    global text_str
    text_str = enterer.get("1.0", "end")
    listbox.insert(END, text_str)

    B_add.config(
        command=lambda: AddSTR(separatorTree, B_add, listbox),
        text="Add"
    )

    update_Read_List(listbox)
    enterer.destroy()





# ----------------------------------------------Функції обробки натискання "RANDOM"------------------------------------#
def randSTR(separatorTree, B_open, listbox):

    nums = len(list1)
    random_number = random.randint(0, nums)


    enterer = Text(separatorTree, height=5, width=15)

    # Отримуємо індекс вибраного елемента у списку Listbox
    selection_index = listbox.curselection()

    # Отримуємо значення індексу з кортежу та виводимо відповідний елемент зі списку list1
    enterer.insert(END, list1[random_number-1])
    enterer.grid(row=0, column=0, columnspan=3, sticky='nsew')  # Показуємо віджет Text для редагування

    B_open.config(
        text="Close",
        command=lambda: rand_ok(enterer, B_open, separatorTree, listbox, random_number-1)
    )


def rand_ok(enterer, B_add, separatorTree, listbox, pos):
    global text_str

    selection_index = listbox.curselection()

    text_str = enterer.get("1.0", "end").strip()  # Використовуємо strip(), щоб видалити символи нового рядка
    listbox.insert(END, text_str)

    # Змінюємо елемент у list1 за позицією pos
    list1[pos] = text_str

    # Оновлюємо listbox з новими значеннями
    update_Write_List(listbox)

    B_add.config(
        command=lambda: randSTR(separatorTree, B_add, listbox),
        text="RANDOM"
    )

    # Оновлюємо listbox після оновлення значення у list1
    update_Read_List(listbox)

    set_cursor(listbox,pos)
    enterer.destroy()

