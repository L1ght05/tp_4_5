import tkinter as tk
from tkinter import messagebox, filedialog

root = tk.Tk()
root.title("Widget Practice")
root.geometry("400x400")
root.config(bg="white")

def change_theme(theme):
    colors = {
        "Light": "white",
        "Dark": "#2e2e2e",
        "Blue": "#d0e4f7"
    }
    root.config(bg=colors.get(theme, "white"))

def save_file():
    messagebox.showinfo("Success", "File saved successfully!")

def save_as_file():
    filedialog.asksaveasfilename(title="Save As")

def show_about():
    about_window = tk.Toplevel(root)
    about_window.title("About")
    about_window.geometry("300x180")
    about_window.resizable(False, False)
    about_window.transient(root)
    about_window.grab_set()
    
    tk.Label(about_window, text="Widget Practice App", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(about_window, text="Version: 3.1.0", font=("Arial", 10)).pack()
    tk.Label(about_window, text="Developed by: Oumari yassin abderrahmane", font=("Arial", 10)).pack(pady=5)
    tk.Label(about_window, text="Built with Python & Tkinter", font=("Arial", 9)).pack()
    tk.Button(about_window, text="Close", command=about_window.destroy).pack(pady=15)

def show_contact():
    messagebox.showinfo("Contact Us", "Email: yassinoumari8@.com")

menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=lambda: print("New file"))
file_menu.add_command(label="Open", command=lambda: print("Open file"))
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)

preferences_menu = tk.Menu(file_menu, tearoff=0)
theme_menu = tk.Menu(preferences_menu, tearoff=0)
theme_menu.add_command(label="Light", command=lambda: change_theme("Light"))
theme_menu.add_command(label="Dark", command=lambda: change_theme("Dark"))
theme_menu.add_command(label="Blue", command=lambda: change_theme("Blue"))
preferences_menu.add_cascade(label="Color Theme", menu=theme_menu)
file_menu.add_cascade(label="Preferences", menu=preferences_menu)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Copy", command=lambda: print("Copy"))
edit_menu.add_command(label="Paste", command=lambda: print("Paste"))
menubar.add_cascade(label="Edit", menu=edit_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
help_menu.add_command(label="Contact", command=show_contact)
menubar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menubar)

label = tk.Label(root, text="Choose your preferences", font=("Arial", 14))
label.pack(pady=10)

vr1 = tk.BooleanVar()
vr2 = tk.BooleanVar()
cb1 = tk.Checkbutton(root, text="Enable notifications", variable=vr1)
cb2 = tk.Checkbutton(root, text="Dark mode", variable=vr2)
cb1.pack()
cb2.pack()

mode = tk.StringVar(value="Light")
tk.Label(root, text="Theme").pack()
tk.Radiobutton(root, text="Light", variable=mode, value="Light").pack()
tk.Radiobutton(root, text="Dark", variable=mode, value="Dark").pack()

lb = tk.Listbox(root, height=4)
for item in ["Python", "Java", "C++", "JavaScript"]:
    lb.insert(tk.END, item)
lb.pack(pady=5)

scale = tk.Scale(root, from_=0, to=100, orient="horizontal", label="Volume")
scale.pack(pady=10)

def show_values():
    print("Notifications:", vr1.get())
    print("Dark mode:", vr2.get())
    print("Theme:", mode.get())
    print("Language:", lb.get(tk.ACTIVE))
    print("Volume:", scale.get())

tk.Button(root, text="Show Values", command=show_values).pack(pady=10)

root.mainloop()