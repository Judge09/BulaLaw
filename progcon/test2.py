# importing tkinter, tk and ttk (mas modern ttk pero tk may mga options na wala sa ttk like bg sa button)
import tkinter as tk
from tkinter import ttk, font  # (imports diff fonts)

# window
window = tk.Tk()
window.title('styling')
window.geometry('900x300')

# widgets
# label
ttk.Label(window, background='red').pack(expand=True, fill='both')
ttk.Label(window, background='purple').pack(expand=True, fill='both')
ttk.Label(window, background='#687696').pack(expand=True, fill='both')

# run
window.mainloop()
