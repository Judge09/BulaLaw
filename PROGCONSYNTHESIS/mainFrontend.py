import tkinter
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTkScrollableFrame

# Importing functions from the process code
def load_legal_terms(file_path):
    legal_terms = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split('|')
                    if len(parts) == 3:  # Ensure we have three parts
                        term, definition, location = parts
                        legal_terms[term] = {"definition": definition, "location": location}
                    else:
                        print(f"Error parsing line: {line}")
    except FileNotFoundError:
        print("File not found.")
    return legal_terms


def search(legal_terms, keyword):
    keyword = keyword.lower()
    results = []

    for term, data in legal_terms.items():
        term_lower = term.lower()
        definition_lower = data["definition"].lower()

        if keyword in term_lower or keyword in definition_lower:
            results.append((term, data["definition"], data["location"]))

    return results

# Tkinter application
app = customtkinter.CTk()
app.geometry("600x400")
app.title("app")
app.resizable(width=True, height=True)

def button_callback():
    keyword = entry1.get()  # Get the keyword from the entry field
    search_results = search(legal_terms, keyword)  # Perform search
    if search_results:
        print("\nSearch results:")
        for result in search_results:
            print(f"\nTerm: {result[0]}\nDefinition: {result[1]}\nLocation: {result[2]}\n")
    else:
        print("\nNo matching terms found.")

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

# Load legal terms
file_path = "legal_terms2.txt"  # Replace with the actual path to your text file
legal_terms = load_legal_terms(file_path)

app.mainloop()
