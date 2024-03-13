from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, a):
        self.a = a
        self.a.title("Password Generator")
        self.a.geometry("400x400")

        self.password_var = StringVar()
        self.password_var.set("")

        self.length_label = ttk.Label(a, text="Password Length*:")
        self.length_label.grid(row=0, column=0, padx=15, pady=5, sticky="w")

        self.length_entry = ttk.Entry(a)
        self.length_entry.grid(row=0, column=1, pady=5)

        self.complexity_label = ttk.Label(a, text="Complexity Level*:")
        self.complexity_label.grid(row=1, column=0, padx=15, pady=5, sticky="w")

        self.complexity_var = StringVar()
        self.complexity_var.set("Medium")

        self.complexity_dropdown = ttk.Combobox(a, textvariable=self.complexity_var, values=["Low", "Medium", "Hard"])
        self.complexity_dropdown.grid(row=1, column=1, pady=5)

        self.uppercase_var = IntVar()
        self.uppercase_checkbox = ttk.Checkbutton(a, text="Include Uppercase", variable=self.uppercase_var)
        self.uppercase_checkbox.grid(row=2, column=0, padx=15, pady=5, sticky="w")

        self.lowercase_var = IntVar()
        self.lowercase_checkbox = ttk.Checkbutton(a, text="Include Lowercase", variable=self.lowercase_var)
        self.lowercase_checkbox.grid(row=3, column=0, padx=15, pady=5, sticky="w")

        self.numbers_var = IntVar()
        self.numbers_checkbox = ttk.Checkbutton(a, text="Include Numbers", variable=self.numbers_var)
        self.numbers_checkbox.grid(row=4, column=0, padx=15, pady=5, sticky="w")

        self.special_var = IntVar()
        self.special_checkbox = ttk.Checkbutton(a, text="Include Special Characters", variable=self.special_var, command=self.show_special_input)
        self.special_checkbox.grid(row=5, column=0, padx=15, pady=5, sticky="w")

        self.special_label = ttk.Label(a, text="Number of Special Characters*:")
        self.special_label.grid(row=6, column=0, padx=15, pady=5, sticky="w")
        self.special_label.grid_remove()

        self.special_entry = ttk.Entry(a)
        self.special_entry.grid(row=6, column=1, pady=5)
        self.special_entry.grid_remove()

        self.generate_button = ttk.Button(a, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.copy_button = ttk.Button(a, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=8, column=0, columnspan=2)

        self.password_label = ttk.Label(a, textvariable=self.password_var)
        self.password_label.grid(row=9, column=0, columnspan=2, pady=10)

    def show_special_input(self):
        if self.special_var.get():
            self.special_label.grid()
            self.special_entry.grid()
        else:
            self.special_label.grid_remove()
            self.special_entry.grid_remove()

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid Password Length ")
            return

        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0.")
            return

        special_count = 0
        if self.special_var.get():
            try:
                special_count = int(self.special_entry.get())
                if special_count < 1:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Error", "Invalid input for number of special characters.")
                return

            if special_count > length:
                messagebox.showerror("Error", "Number of special characters cannot exceed the password length.")
                return

        charset1 = ""
        charset2 = ""
        complexity = self.complexity_var.get()
        if self.uppercase_var.get():
            charset1 += string.ascii_uppercase
        if self.lowercase_var.get():
            charset1 += string.ascii_lowercase
        if self.numbers_var.get():
            charset1 += string.digits
        if self.special_var.get():
            if complexity == "Low":
                charset2 += "!@#$%^&*()-_=+"
            elif complexity == "Medium":
                charset2 += "!@#$%^&*()_+=-[]{}|;:,.<>?/~"
            elif complexity == "Hard":
                charset2 += "!@#$%^&*()_+=-[]{}|\:;\"'<>,.?/~`"
            else:
                messagebox.showerror("Error", "Invalid complexity level.")
                return

        if not (charset1 or (charset2 and special_count>0)):
            messagebox.showerror("Error", "Please select at least one character type.")
            return
        
        p = ""
        p += ''.join(random.choice(charset1) for _ in range(length - special_count))
        p += ''.join(random.choice(charset2) for _ in range(special_count))
        password =  ''.join(random.sample(p,len(p)))

        self.password_var.set(password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard.")
        else:
            messagebox.showerror("Error", "No password generated yet.")


def main():
    root = Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
