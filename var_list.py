import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry('500x300')


backpack = ['knife', 'sword', 'gun', 'Health potion']

var = tk.Variable(value=backpack)

listbox = tk.Listbox(root, listvariable=var, height=6)
listbox.pack(expand=True, fill=tk.BOTH)

def something():
    value = listbox.get(listbox.curselection())
    if value == 'knife':
        root1 = tk.Tk()
        root.geometry('500x300')
        label1 = tk.Label(root1, bg='black', fg='white', text ='this is how we set commands for a list')
        label1.pack(expand = True, fill = BOTH)
        root1.mainloop()
    
    if value == 'gun':
        root1 = tk.Tk()
        root.geometry('500x300')
        label1 = tk.Label(root1, bg='black', fg='white', text ='you take your gun and shoot the monster')
        label1.pack(expand = True, fill = BOTH)
        root.destroy()
        

def click(event):
    value = listbox.get(listbox.curselection())
    if value == 'knife':
        root1 = tk.Tk()
        root.geometry('500x300')
        label1 = tk.Label(root1, bg='black', fg='white', text ='this is how we bind keys to buttons in tkinter')
        label1.pack(expand = True, fill = BOTH)
        root.destroy()


button = tk.Button(root, text='fetch', width=15,height=2, command=something)
button.pack()
button1 = tk.Button(root, text = 'button')
button1.bind('<Return>', click)
button1.pack()

root.mainloop()