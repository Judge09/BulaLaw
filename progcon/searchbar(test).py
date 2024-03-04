import tkinter as tk

def search():
    query = entry.get()
    # Perform search or any other action with the query
    print("Searching for:", query)

# Create the main window
root = tk.Tk()
root.title("Search Bar Example")

# Create a frame to hold the search entry and button
frame = tk.Frame(root)
frame.pack(fill=tk.X, padx=10, pady=10)

# Create and place a search entry widget
entry = tk.Entry(frame, width=30)
entry.pack(side=tk.LEFT, fill=tk.X)

# Create and place a search button
search_button = tk.Button(frame, text="Search", command=search)
search_button.pack(side=tk.LEFT, padx=(0, 10))

# Disable geometry propagation for the frame
frame.pack_propagate(True)

# Run the Tkinter event loop
root.mainloop()