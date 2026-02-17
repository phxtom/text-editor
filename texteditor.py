import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app=ctk.CTk()
app.geometry("900x600")
app.title=("Scratchpad")

text=ctk.CTkTextbox(app, font=("JetBrains Mono", 14))
text.pack(fill="both", expand=True, padx=20, pady=20)

def saveas():
    global text

    t = text.get("1.0", "end-1c")
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file:
        with open(file, "w") as f:
            f.write(t)
            f.close()

button=tk.Button(root, text="Save As", command=saveas)
button.grid()

root.mainloop()
