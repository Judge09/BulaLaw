import tkinter
from customtkinter import *
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # creating cutstom tkinter window
app.geometry("600x440")
app.title('search')
app.grid_columnconfigure((0), weight=1)

frame1 = CTkScrollableFrame(master=app, fg_color="#8D6F3A", border_color="#FFCC70", border_width=2,
                           orientation="vertical", scrollbar_button_color="#FFCC70")
frame1.pack(expand=True)

# creating custom frame
def search():
    query = entry1.get()
    # Perform search or any other action with the query
    print("Searching for:", query)

# Create and place a search entry widget
entry1 = CTkEntry(app, width=30)
entry1.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Create and place a search button
search_button = CTkButton(app, text="Search", command=search)
search_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Configure column weights to make them resizable
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=0)  # Change weight if you want to give more space to the button

# Run the Tkinter event loop
app.mainloop()