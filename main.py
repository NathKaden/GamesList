from tkinter import *
from tkinter import ttk

window = Tk()
window.title("GameList")
window.geometry('700x480')
#window.iconbitmap("./assets/icon.png")
window.config(background="#333333")

# Label that act as a "Title" something like an H1
lbl = Label(window, text="haap", font=("Arial Bold", 20))

lbl.grid(column=0, row=0)


# creation d'une barre de menu
menu_bar = Menu(window)
# Creer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Fichier",menu=file_menu)
file_menu.add_command(label="Nouveau",command="")
file_menu.add_command(label="Quitter",command=window.quit)

#configurer notre fenetre pour alouter cette menu bar
window.config (menu=menu_bar)
#afficher la fenetre
window.mainloop()