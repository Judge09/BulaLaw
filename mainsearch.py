import tkinter
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTkScrollableFrame
import webbrowser

app = customtkinter.CTk()
app.geometry("600x400")
app.title("app")
app.resizable(width=True, height=True)

def callback(url):
    webbrowser.open_new(url)

def button_callback():
    print("button pressed")


top = customtkinter.CTkFrame(master=app,
                             fg_color="#D3D3D3")
top.pack(side="top",
         fill="both",
         expand=False)

bot = CTkScrollableFrame(master=app,
                         fg_color="#E5E4E2")
bot.pack(side="bottom",
         fill="both",
         expand=True)

img1 = customtkinter.CTkImage(Image.open("search2.png"))

entry = customtkinter.CTkEntry(top,
                               placeholder_text='Type anything',
                               fg_color="#E5E4E2",
                               corner_radius=0,
                               height=40)

entry.pack(side="left", expand=True, fill="both")

# Create and place a search button
search_button = customtkinter.CTkButton(top, image=img1, width=50, height=50, corner_radius=0, compound="left",
                                        fg_color='#4B9CD3', text_color='white', hover_color='#AFAFAF', text="",
                                        command=button_callback)
search_button.pack(side="left", padx=(0, 10))

#ehto ung looloop na frame
frames = customtkinter.CTkFrame(master=bot,
                             fg_color="#D3D3D3")
frames.pack(fill="both", expand=False)

link1 = customtkinter.CTkLabel(frames, text="Hyperlink", text_color="#4B9CD3", cursor="hand2", font=("", 20))
link1.pack(anchor="w")
link1.bind("<Button-1>", lambda e: callback("https://www.youtube.com/"))

label1 = customtkinter.CTkLabel(frames, text="Label 1", text_color="black")
label1.pack(anchor="w")
label2 = customtkinter.CTkLabel(frames, text="Label 2", text_color="black")
label2.pack(anchor="w")

app.mainloop()
