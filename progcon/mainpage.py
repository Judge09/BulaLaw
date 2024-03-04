import customtkinter
from PIL import ImageTk, Image

app = customtkinter.CTk()
app.geometry("600x400")
app.title("app")
app.resizable(width=True, height=True)

def button_callback():
    print("button pressed")

img1 = customtkinter.CTkImage(Image.open("search2.png").resize((40, 40)))

frame = customtkinter.CTkFrame(app)
frame.pack(fill="both", padx=10, pady=10)

# Create and place a search entry widget
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
