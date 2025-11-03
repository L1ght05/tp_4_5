import tkinter as tk
from tkinter import messagebox, filedialog

# --- Main Window ---
root = tk.Tk()
root.title("Widget Practice")
root.geometry("400x450")

# --- Default Background ---
root.config(bg="lightgray")

# --- Label ---
label = tk.Label(root, text="Choose your preferences:", font=("Arial", 14), bg="lightgray")
label.pack(pady=10)

# --- Checkbuttons ---
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
cb1 = tk.Checkbutton(root, text="Enable notifications", variable=var1, bg="lightgray")
cb2 = tk.Checkbutton(root, text="Dark mode", variable=var2, bg="lightgray")
cb1.pack()
cb2.pack()

# --- Radiobuttons ---
mode = tk.StringVar(value="Light")
tk.Label(root, text="Theme:", bg="lightgray").pack()
tk.Radiobutton(root, text="Light", variable=mode, value="Light", bg="lightgray").pack()
tk.Radiobutton(root, text="Dark", variable=mode, value="Dark", bg="lightgray").pack()

# --- Listbox ---
lb = tk.Listbox(root, height=4)
for item in ["Python", "Java", "C++", "JavaScript"]:
    lb.insert(tk.END, item)
lb.pack(pady=5)

# --- Scale ---
scale = tk.Scale(root, from_=0, to=100, orient="horizontal", label="Volume", bg="lightgray")
scale.pack(pady=10)

# --- Button ---
def show_values():
    print("Notifications:", var1.get())
    print("Dark mode:", var2.get())
    print("Theme:", mode.get())
    print("Language:", lb.get(tk.ACTIVE))
    print("Volume:", scale.get())

tk.Button(root, text="Show Values", command=show_values).pack(pady=10)

# ======================================================
# 1️⃣  FILE MENU: Add Save, Save As, and proper structure
# ======================================================

def save_file():
    messagebox.showinfo("Save", "File saved successfully!")

def save_as_file():
    filename = filedialog.asksaveasfilename(title="Save As", defaultextension=".txt",
                                            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filename:
        messagebox.showinfo("Save As", f"File saved as:\n{filename}")

# ======================================================
# 2️⃣  DYNAMIC SUBMENU: Change Theme Dynamically
# ======================================================

def set_theme(color):
    themes = {
        "Light": "lightgray",
        "Dark": "#2b2b2b",
        "Blue": "#87CEFA"
    }
    root.config(bg=themes[color])
    label.config(bg=themes[color])
    cb1.config(bg=themes[color])
    cb2.config(bg=themes[color])
    for widget in root.pack_slaves():
        if isinstance(widget, tk.Radiobutton) or isinstance(widget, tk.Scale) or isinstance(widget, tk.Label):
            widget.config(bg=themes[color])

# ======================================================
# 3️⃣  HELP MENU: About and Contact
# ======================================================

def show_about():
    about_win = tk.Toplevel(root)
    about_win.title("About")
    about_win.geometry("300x200")
    about_win.config(bg="white")

    tk.Label(about_win, text="Widget Practice App", font=("Arial", 14, "bold"), bg="white").pack(pady=10)
    tk.Label(about_win, text="Developer: Yassine", bg="white").pack()
    tk.Label(about_win, text="Version: 1.0", bg="white").pack()
    tk.Button(about_win, text="Close", command=about_win.destroy).pack(pady=20)

def show_contact():
    messagebox.showinfo("Contact", "Email: developer@example.com")

# ======================================================
# 4️⃣  SETTINGS WINDOW (Bonus)
# ======================================================

def open_settings():
    settings_win = tk.Toplevel(root)
    settings_win.title("Settings")
    settings_win.geometry("300x250")
    settings_win.config(bg="white")

    tk.Label(settings_win, text="Settings", font=("Arial", 14, "bold"), bg="white").pack(pady=10)

    # Checkbox
    notif_var = tk.BooleanVar(value=var1.get())
    tk.Checkbutton(settings_win, text="Enable notifications", variable=notif_var, bg="white").pack(pady=5)

    # Theme selection
    tk.Label(settings_win, text="Select Theme:", bg="white").pack()
    theme_var = tk.StringVar(value="Light")
    for theme in ["Light", "Dark", "Blue"]:
        tk.Radiobutton(settings_win, text=theme, variable=theme_var, value=theme, bg="white").pack(anchor="w")

    # Save Button
    def apply_settings():
        var1.set(notif_var.get())
        set_theme(theme_var.get())
        messagebox.showinfo("Settings", "Settings saved and theme updated!")

    tk.Button(settings_win, text="Save Changes", command=apply_settings).pack(pady=15)

# ======================================================
# --- MENU BAR CREATION ---
# ======================================================

menubar = tk.Menu(root)

# --- FILE MENU ---
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=lambda: print("New File"))
file_menu.add_command(label="Open", command=lambda: print("Open File"))

# --- SUBMENU: Preferences ---
preferences_menu = tk.Menu(file_menu, tearoff=0)

# Dynamic Theme Submenu
theme_menu = tk.Menu(preferences_menu, tearoff=0)
theme_menu.add_command(label="Light", command=lambda: set_theme("Light"))
theme_menu.add_command(label="Dark", command=lambda: set_theme("Dark"))
theme_menu.add_command(label="Blue", command=lambda: set_theme("Blue"))
preferences_menu.add_cascade(label="Themes", menu=theme_menu)

# Settings Window
preferences_menu.add_command(label="Settings", command=open_settings)
file_menu.add_cascade(label="Preferences", menu=preferences_menu)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=file_menu)

# --- ADD SAVE AND SAVE AS DIRECTLY UNDER FILE (not inside submenu) ---
menubar.add_command(label="Save", command=save_file)
menubar.add_command(label="Save As", command=save_as_file)

# --- EDIT MENU ---
edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Copy", command=lambda: print("Copy"))
edit_menu.add_command(label="Paste", command=lambda: print("Paste"))
menubar.add_cascade(label="Edit", menu=edit_menu)

# --- HELP MENU ---
help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
help_menu.add_command(label="Contact", command=show_contact)
menubar.add_cascade(label="Help", menu=help_menu)

# --- CONFIGURE MENUBAR ---
root.config(menu=menubar)

# --- MAIN LOOP ---

root.mainloop()