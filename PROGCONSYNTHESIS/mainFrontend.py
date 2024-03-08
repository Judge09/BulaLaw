import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
from customtkinter import CTkScrollableFrame
import geocoder

# Function to fetch user's location based on IP geolocation
def get_user_location():
    try:
        g = geocoder.ip('me')
        return g.city
    except Exception as e:
        print("Error fetching user's location:", e)
        return ""

# Importing functions from the process code
def load_legal_terms(file_path):
    legal_terms = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split('|')
                    if len(parts) == 4:  # Ensure we have four parts
                        name, description, location, link = parts
                        legal_terms[name] = {"description": description, "location": location, "link": link}
                    else:
                        print(f"Error parsing line: {line}")
    except FileNotFoundError:
        print("File not found.")
    return legal_terms


def search(legal_terms, keyword, user_location):
    keyword = keyword.lower()
    results = []

    for name, data in legal_terms.items():
        name_lower = name.lower()
        description_lower = data["description"].lower()
        location_lower = data["location"].lower()

        if keyword in name_lower or keyword in description_lower:
            if "philippine" in location_lower or user_location.lower() in location_lower:
                results.append((name, data["description"], data["location"], data["link"]))

    return results


# Tkinter application
app = customtkinter.CTk()
app.geometry("1000x500")
app.title("app")
app.resizable(width=True, height=True)

def button_callback():
    keyword = entry1.get()  # Get the keyword from the entry field
    user_location = get_user_location()  # Get user's current location
    search_results = search(legal_terms, keyword, user_location)  # Perform search
    result_text.delete('1.0', tk.END)  # Clear previous results
    if search_results:
        num_results_label.config(text=f"{len(search_results)} results found")
        
        # Display user's location
        user_location_label.config(text=f"Your location: {user_location}")
        
        for result in search_results:
            result_text.insert(tk.END, f"Name: {result[0]}\nDescription: {result[1]}\nLocation: {result[2]}\n")
            website_button = tk.Button(result_frame, text="Visit Website", command=lambda link=result[3]: open_website(link))
            result_text.window_create(tk.END, window=website_button)
            result_text.insert(tk.END, "\n\n")
    else:
        num_results_label.config(text="No matching terms found")
        user_location_label.config(text="")

def open_website(link):
    import webbrowser
    webbrowser.open(link)

# Frame to hold search entry and button
search_frame = customtkinter.CTkFrame(master=app, fg_color="#D3D3D3")
search_frame.pack(side="top", fill="x", padx=10, pady=10)

img1 = customtkinter.CTkImage(Image.open("search2.png"))
entry1 = customtkinter.CTkEntry(master=search_frame, placeholder_text='Type anything', fg_color="#E5E4E2", corner_radius= 0, height=40, text_color = "black")
entry1.pack(side="left", expand=True, fill="both", padx=10, pady=10)
button = customtkinter.CTkButton(master=search_frame, image=img1, width=77, height=40, corner_radius=0, compound="left", fg_color='#4B9CD3', text_color='white', hover_color='#AFAFAF', text="", command=button_callback)
button.pack(side="left", padx=10, pady=10)

# Frame to hold user's location
user_location_frame = customtkinter.CTkFrame(master=app, fg_color="#E5E4E2")
user_location_frame.pack(side="top", fill="x", padx=10, pady=(0, 5))

# Label to display user's location
user_location_label = tk.Label(user_location_frame, text="", fg="black")
user_location_label.pack(anchor=tk.W)

# Frame to hold search results
result_frame = customtkinter.CTkFrame(master=app, fg_color="#E5E4E2")
result_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10)

# Label to display number of results
num_results_label = tk.Label(result_frame, text="", fg="black")
num_results_label.pack(anchor=tk.W, padx=10, pady=5)

# Text widget to display search results
result_text = tk.Text(master=result_frame, wrap=tk.WORD, bg="#E5E4E2")
result_text.pack(fill="both", expand=True, padx=10, pady=10)

# Load legal terms
file_path = "legal_terms2.txt"  
legal_terms = load_legal_terms(file_path)

app.mainloop()
