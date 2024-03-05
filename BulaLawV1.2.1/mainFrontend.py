import tkinter
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTkScrollableFrame

customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

class LawDictionary:
    def __init__(self, file_path): 
        self.legal_terms = self.load_legal_terms(file_path)
    
    def load_legal_terms(self, file_path):
        legal_terms = {}
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    term, definition, location = line.strip().split('|')
                    legal_terms[term] = {"definition": definition, "location": location}
                        
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        return legal_terms

    def search(self, keyword):
        keyword = keyword.lower()
        results = [] #if may nagmatch. diyan mastore

        for term, data in self.legal_terms.items():
            term_lower = term.lower()
            definition_lower = data["definition"].lower()

            if keyword in term_lower or keyword in definition_lower:
                # Highlight the keyword in the term and definition
                highlighted_term = term_lower.replace(keyword, f"\033[1;31m{keyword}\033[0m")
                highlighted_definition = definition_lower.replace(keyword, f"\033[1;31m{keyword}\033[0m")

                results.append((highlighted_term, data["definition"], data["location"]))

        return results

if __name__ == "__main__":

    file_path = "legal_terms.txt"   #Replace with the actual path to your text file
    law_dict = LawDictionary(file_path)

    while True:

        if userInput.lower() == 'exit':
            break

        search_results = law_dict.search(userInput)

        if search_results:
            print("\nSearch results:")

            for result in search_results:
                print(f"\nTerm: {result[0]}\nDefinition: {result[1]}\nLocation: {result[2]}\n")
        else:
            print("\nNo matching terms found.")


#======================================================================================================
    

app = customtkinter.CTk()  # creating custom tkinter window
app.geometry("600x440")
app.title('Login')

def button_callback():
    print("button pressed")
def button_function():
    app.destroy()  # destroy current window and creating new one

img1 = ImageTk.PhotoImage(Image.open("pattern.png"))
l1 = customtkinter.CTkLabel(master=app,
                            image=img1
                            )
l1.pack()

# creating custom frame
frame = customtkinter.CTkFrame(master=l1,
                               width=320,
                               height=360,
                               corner_radius=15
                               )

frame.place(relx=0.5,
            rely=0.5,
            anchor=tkinter.CENTER
            )

l2 = customtkinter.CTkLabel(master=frame,
                            text="Log into your Account",
                            font=('Century Gothic', 20)
                            )
l2.place(x=50, y=45)

entry1 = customtkinter.CTkEntry(master=frame,
                                width=220,
                                placeholder_text='Username',
                                )
entry1.place(x=50, y=110)

entry2 = customtkinter.CTkEntry(master=frame,
                                width=220,
                                placeholder_text='Password',
                                show="*"
                                )
entry2.place(x=50, y=165)

l3 = customtkinter.CTkLabel(master=frame,
                            text="Forget password?",
                            font=('Century Gothic', 12)
                            )
l3.place(x=155, y=195)

# Create custom button
button1 = customtkinter.CTkButton(master=frame,
                                  width=220,
                                  text="Login",
                                  command=button_function,
                                  corner_radius=6
                                  )
button1.place(x=50, y=240)

img2 = customtkinter.CTkImage(Image.open("Google__G__Logo.svg.webp").resize((20, 20)))
img3 = customtkinter.CTkImage(Image.open("124010.png").resize((20, 20)))

button2 = customtkinter.CTkButton(master=frame,
                                  image=img2,
                                  text="Google",
                                  width=100,
                                  height=20,
                                  compound="left",
                                  fg_color='white',
                                  text_color='black',
                                  hover_color='#AFAFAF'
                                  )
button2.place(x=50, y=290)

button3 = customtkinter.CTkButton(master=frame,
                                  image=img3,
                                  text="Facebook",
                                  width=100,
                                  height=20,
                                  compound="left",
                                  fg_color='white',
                                  text_color='black',
                                  hover_color='#AFAFAF'
                                  )
button3.place(x=170, y=290)

app.mainloop()

app = customtkinter.CTk()
app.geometry("600x400")
app.title("app")
app.resizable(width=True, height=True)

def button_callback():
    print("button pressed")

img1 = customtkinter.CTkImage(Image.open("search2.png").resize((40, 40)))

frame = customtkinter.CTkFrame(app)
frame.pack(fill="both",
           padx=10,
           pady=10
           )

# Create and place a search entry widget
entry = customtkinter.CTkEntry(frame,
                                placeholder_text='Type anything',
                                fg_color="#E5E4E2",
                                corner_radius= 0,
                                height=40
                               )

def retrieve_input():      
    global userInput
    userInput = entry.get()

entry.pack(side="left",
           expand=True,
           fill="both"
           )

# Create and place a search button
search_button = customtkinter.CTkButton(frame,
                                        image=img1,
                                        width=50,
                                        height=50,
                                        corner_radius=0,
                                        compound="left",
                                        fg_color='#4B9CD3',
                                        text_color='white',
                                        hover_color='#AFAFAF',
                                        text="",
                                        command=retrieve_input
                                        )
search_button.pack(side="left", padx=(0, 10))

app.mainloop()

app = customtkinter.CTk()
app.geometry("600x400")
app.title("app")
app.resizable(width=True, height=True)

top=customtkinter.CTkFrame(master=app,
                           fg_color="#D3D3D3"
                           )
top.pack(side="top",
         fill="both",
         expand=False
         )

bot = CTkScrollableFrame(master=app, fg_color="#E5E4E2")
bot.pack(side="bottom",
         fill="both",
         expand=True
         )

img1 = customtkinter.CTkImage(Image.open("search2.png").resize((40, 40)))

entry1 = customtkinter.CTkEntry(master=top,
                                placeholder_text='Type anything',
                                fg_color="#E5E4E2",
                                corner_radius=0,
                                height=40
                                )
entry1.pack(side="left",
            expand=True,
            fill="both",
            padx=10,
            pady=10
            )

button = customtkinter.CTkButton(master=top,
                                 image=img1,
                                 width=50,
                                 height=50,
                                 corner_radius=0,
                                 compound="left",
                                 fg_color='#4B9CD3',
                                 text_color='black',
                                 hover_color='#AFAFAF',
                                 text="",
                                 command=button_function
                                 )
button.pack(side="left",
            padx=10,
            pady=10
            )

app.mainloop()