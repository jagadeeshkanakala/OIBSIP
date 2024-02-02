import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip  # For clipboard integration

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.length_label = ttk.Label(self.frame, text="Password Length:")
        self.length_label.grid(row=0, column=0, sticky=tk.W, pady=5)

        self.length_entry = ttk.Entry(self.frame)
        self.length_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)

        self.lowercase_var = tk.BooleanVar()
        self.lowercase_check = ttk.Checkbutton(self.frame, text="Include Lowercase Letters", variable=self.lowercase_var)
        self.lowercase_check.grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=5)

        self.uppercase_var = tk.BooleanVar()
        self.uppercase_check = ttk.Checkbutton(self.frame, text="Include Uppercase Letters", variable=self.uppercase_var)
        self.uppercase_check.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=5)

        self.numbers_var = tk.BooleanVar()
        self.numbers_check = ttk.Checkbutton(self.frame, text="Include Numbers", variable=self.numbers_var)
        self.numbers_check.grid(row=3, column=0, columnspan=2, sticky=tk.W, pady=5)

        self.symbols_var = tk.BooleanVar()
        self.symbols_check = ttk.Checkbutton(self.frame, text="Include Symbols", variable=self.symbols_var)
        self.symbols_check.grid(row=4, column=0, columnspan=2, sticky=tk.W, pady=5)

        self.generate_button = ttk.Button(self.frame, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(self.frame, text="")
        self.result_label.grid(row=6, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
        except ValueError:
            self.result_label.config(text="Error: Invalid input. Please enter a valid number for password length.")
            return

        if length <= 0:
            self.result_label.config(text="Error: Password length must be greater than 0.")
            return

        character_set = ""
        if self.lowercase_var.get():
            character_set += string.ascii_lowercase
        if self.uppercase_var.get():
            character_set += string.ascii_uppercase
        if self.numbers_var.get():
            character_set += string.digits
        if self.symbols_var.get():
            character_set += string.punctuation

        if not character_set:
            self.result_label.config(text="Error: At least one character set must be selected.")
            return

        generated_password = ''.join(random.choice(character_set) for _ in range(length))
        self.result_label.config(text=f"Generated Password: {generated_password}")

        # Copy the generated password to the clipboard
        pyperclip.copy(generated_password)


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
