from Functions import *

max_columns = 3

if __name__ == '__main__':
    root = Tk()
    root.title("Random Strings :)")
    root.geometry("300x300")

    #заборона міняти розиіри менше ніж 300 на 300
    root.minsize(300, 300)
    root.resizable(width=True, height=True)


    # ---------------------------------------Ініціалізації елементів---------------------------------------------------#

    B_add = Button(root, text="Add string")
    B_del = Button(root, text="Dell string")
    B_open = Button(root, text="Open")
    B_rand = Button(root, text="RANDOM")

    separator = Frame(root, height=2, bd=1, relief=SUNKEN)
    separatorTree = Frame(root, height=40, bd=1, relief=SUNKEN)

    listbox = Listbox(separatorTree, height=5, width=15, selectmode=EXTENDED)  # створюємо віджет – список




    # -----------------------------------------Розташування по сітці---------------------------------------------------#

    B_add.grid(row=3, column=1, sticky='ew', padx=5, pady=5)
    B_open.grid(row=3, column=2, sticky='ew', padx=5, pady=5)
    B_del.grid(row=3, column=3, sticky='ew', padx=5, pady=5)



    B_rand.grid(row=1, column=1, columnspan=max_columns, sticky='sew', padx=5, pady=5)

    separator.grid(row=2, column=1, columnspan=max_columns, sticky='ew', padx=5, pady=5)
    separatorTree.grid(row=0, column=1, columnspan=max_columns, sticky='nsew', padx=10, pady=10)

    listbox.grid(row=0, column=0, columnspan=max_columns, sticky='nsew')  # Встановлюємо columnspan на 2




    # ------------------------------------------Налаштування конфігів--------------------------------------------------#

    B_add.config(
        activebackground='#f4C639',
        background='#79FFA4',
        bd=2,
        relief=GROOVE,
        command=lambda: AddSTR(separatorTree, B_add, listbox)

    )

    B_del.config(
        activebackground='#f4C639',
        background='#FF4F29',
        bd=2,
        relief=GROOVE,
        command=lambda: deleteSTR(listbox)

    )

    B_rand.config(
        activebackground='#f4C639',
        background='#B1C9FF',
        bd=2,
        relief=GROOVE,
        command=lambda: randSTR(separatorTree, B_rand, listbox)

    )

    B_open.config(
        activebackground='#f4C639',
        background='#FECC7A',
        bd=2,
        relief=GROOVE,
        command=lambda: Open(separatorTree, B_open, listbox)

    )


    separatorTree.config(
        background='#EAFFD4'
    )

    listbox.config(
        background='#EAFFD4'
    )

    listbox.config(
        selectbackground='#BDFEFF',
        selectforeground='#000000'
    )



    # -----------------------------Гнучкість колонок для рівномірного розподілу ширини---------------------------------#

    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)

    separatorTree.columnconfigure(1, weight=1)


    root.rowconfigure(0, weight=1)  # separatorTree
    root.rowconfigure(1, weight=0)  # b3
    root.rowconfigure(2, weight=0)  # separator
    root.rowconfigure(3, weight=0)  # b1, b2

    separatorTree.rowconfigure(0, weight=1) #listbox






    # -----------------------------Логічна частина програми---------------------------------#

    update_Write_List(listbox)


    root.mainloop()
    # -------------------------------------------Кінець функції--------------------------------------------------------#