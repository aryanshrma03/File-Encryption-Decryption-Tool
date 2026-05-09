import customtkinter as ctk
from tkinter import filedialog, messagebox

from encryption.fernet import encrypt_file, decrypt_file

from config.theme import load_theme
from components.header import create_header
from components.footer import create_footer
from components.buttons import create_action_buttons
from components.password import toggle_password


load_theme()


class FileEncrypter:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("File Encryption Tool")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.file_path = ""

        # Header
        create_header(self.root)

        # Select File Button
        self.select_button = ctk.CTkButton(
            self.root,
            text="Select File",
            command=self.select_file,
            width=220,
            height=50,
            font=("Segoe UI", 16, "bold"),
            corner_radius=12
        )
        self.select_button.pack(pady=15)

        # Selected File Label
        self.selected_file_label = ctk.CTkLabel(
            self.root,
            text="No file selected",
            wraplength=500,
            text_color="#66b3ff",
            font=("Segoe UI", 13)
        )
        self.selected_file_label.pack(pady=10)

        # Password Label
        self.password_label = ctk.CTkLabel(
            self.root,
            text="Enter Password",
            font=("Segoe UI", 18)
        )
        self.password_label.pack(pady=10)

        # Password Entry
        self.password_entry = ctk.CTkEntry(
            self.root,
            width=420,
            height=45,
            show="*",
            font=("Segoe UI", 15),
            corner_radius=12,
            placeholder_text="Enter secure password..."
        )
        self.password_entry.pack(pady=10)

        # Show Password Checkbox
        self.show_password_var = ctk.BooleanVar()

        self.show_password_checkbox = ctk.CTkCheckBox(
            self.root,
            text="Show Password",
            variable=self.show_password_var,
            command=self.toggle_password_ui,
            font=("Segoe UI", 13)
        )
        self.show_password_checkbox.pack(pady=5)

        # Buttons
        create_action_buttons(
            self.root,
            self.encrypt,
            self.decrypt
        )

        # Footer
        create_footer(self.root)

    # Toggle Password
    def toggle_password_ui(self):
        toggle_password(
            self.password_entry,
            self.show_password_var
        )

    # Select File
    def select_file(self):
        self.file_path = filedialog.askopenfilename()

        if self.file_path:
            self.selected_file_label.configure(
                text=f"Selected File:\n{self.file_path}"
            )

            messagebox.showinfo(
                "Selected File",
                "File Selected Successfully!"
            )

    # Encrypt
    def encrypt(self):
        password = self.password_entry.get()

        if not self.file_path:
            messagebox.showerror(
                "Error",
                "Please select a file first."
            )
            return

        if not password:
            messagebox.showerror(
                "Error",
                "Please enter a password."
            )
            return

        try:
            encrypted_file = encrypt_file(
                self.file_path,
                password
            )

            messagebox.showinfo(
                "Success",
                f"File Encrypted Successfully!\n\nSaved at:\n{encrypted_file}"
            )

        except Exception as e:
            messagebox.showerror(
                "Encryption Error",
                str(e)
            )

    # Decrypt
    def decrypt(self):
        password = self.password_entry.get()

        if not self.file_path:
            messagebox.showerror(
                "Error",
                "Please select a file first."
            )
            return

        if not password:
            messagebox.showerror(
                "Error",
                "Please enter a password."
            )
            return

        try:
            decrypted_file = decrypt_file(
                self.file_path,
                password
            )

            messagebox.showinfo(
                "Success",
                f"File Decrypted Successfully!\n\nSaved at:\n{decrypted_file}"
            )

        except Exception as e:
            messagebox.showerror(
                "Decryption Error",
                str(e)
            )

    def run(self):
        self.root.mainloop()