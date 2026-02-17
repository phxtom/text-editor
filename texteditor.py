import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Text Editor")
    
text=tk.Text(root)
text.grid()

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
