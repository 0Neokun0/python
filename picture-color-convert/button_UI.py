import tkinter as tk
base = tk.Tk()

def push() :
    print('Push')

button = tk.Button(base,text='Push', command=push).pack()
base.mainloop()