import tkinter
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTkScrollableFrame

app = customtkinter.CTk()
app.geometry("600x400")
app.title("app")
app.resizable(width=True, height=True)

def button_callback():
    print("button pressed")

top=customtkinter.CTkFrame(master=app,
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

entry1 = customtkinter.CTkEntry(master=top,
                                placeholder_text='Type anything',
                                fg_color="#E5E4E2",
                                corner_radius= 0,
                                height=40)
entry1.pack(side="left", expand=True, fill="both", padx=10, pady=10)
button = customtkinter.CTkButton(master=top,image=img1,width=77, height=40,corner_radius=0, compound="left", fg_color='#4B9CD3', text_color='white', hover_color='#AFAFAF', text="", command=button_callback)
button.pack(side="left", padx=10, pady=10)


app.mainloop()