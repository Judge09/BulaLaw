# importing tkinter, tk and ttk (mas modern ttk pero tk may mga options na wala sa ttk like bg sa button)
import tkinter as tk
from tkinter import ttk, font  # (imports diff fonts)

# window
window = tk.Tk()
window.title('styling')
window.geometry('900x300')

# print(font.families()) prints font families

# widgets
# label
label = ttk.Label(window,
                  text='A label\n bagong bitch ',  # \n break line
                  background="red",
                  foreground="yellow",
                  font=("times new roman", 20),
                  justify="center"  # right, left
                  )

label.pack()  # layout methods

# style for ze button
style = ttk.Style()
# style.theme_use('alt') ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
# print(style.theme_names())

style.configure('new.TButton',
                background='purple',
                foreground='yellow',
                font=('times new roman', 20))
style.map('new.TButton',
          foreground=[('pressed', 'red'), ('disabled', 'yellow')],
          background=[('pressed', 'yellow'), ('active', 'green')])

style.configure('new.TFrame',
                background="purple")
# button
button = ttk.Button(window,
                    text='A button',
                    style='new.TButton'
                    )  # button no have label styling mithod
button.pack()

frame = ttk.Frame(window,
                  height=200,
                  width=400,
                  style='new.TFrame'
                  )  # frame no have label styling mithod
frame.pack()
# run
window.mainloop()
