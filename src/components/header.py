import customtkinter as ctk

def create_header(root):
    title = ctk.CTkLabel(
        root,
        text="🔐 File Encryption & Decryption Tool",
        font=("Segoe UI", 30, "bold"),
        text_color="#ffffff"
    )
    title.pack(pady=(30, 5))

    subtitle = ctk.CTkLabel(
        root,
        text="Secure Your Files With Advanced Encryption",
        font=("Segoe UI", 14),
        text_color="#888888"
    )
    subtitle.pack(pady=(0, 20))