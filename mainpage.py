import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
app.title("app")
app.attributes('-topmost', True)
app.resizable(True, True)

def button_callback():
    app.destroy()

img1 = customtkinter.CTkImage(Image.open("search2.png").resize((40, 40)))

frame = customtkinter.CTkFrame(app)
frame.pack(fill="both", padx=10, pady=10)

# Create and place a search entry widget
img2 = customtkinter.CTkImage(Image.open("BULALAW.png"),size=(1441,316))
label=customtkinter.CTkLabel(frame, image=img2, text="")
label.pack()
entry = customtkinter.CTkEntry(frame,
                                placeholder_text='Type anything',
                                fg_color="#E5E4E2",
                                corner_radius= 0,
                                height=40)

entry.pack(side="left",expand=True, fill="both")

# Create and place a search button
search_button = customtkinter.CTkButton(frame, image=img1,width=50, height=50,corner_radius=0, compound="left", fg_color='#4B9CD3', text_color='white', hover_color='#AFAFAF', text="", command=button_callback)
search_button.pack(side="left", padx=(0, 10))

app.mainloop()
