import customtkinter as ctk

# window
window = ctk.CTk()
window.title('customtkinter app')
window.geometry('900x300')

# widgets
label = ctk.CTkLabel(window,
                     text='a CTk label',
                     font=('times new roman', 20),
                     fg_color='#e7d1ff',
                     text_color='blue',
                     corner_radius=10,
                     )
label.pack()

def slider_event(value):
    print(value)

slider = customtkinter.CTkSlider(app, from_=0, to=100, command=slider_event)
window.mainloop()

