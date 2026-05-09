import customtkinter as ctk

def create_action_buttons(parent, encrypt_command, decrypt_command):
    frame = ctk.CTkFrame(
        parent,
        fg_color="transparent"
    )
    frame.pack(pady=30)

    encrypt_button = ctk.CTkButton(
        frame,
        text="Encrypt",
        command=encrypt_command,
        width=180,
        height=50,
        font=("Segoe UI", 16, "bold"),
        fg_color="green",
        hover_color="#00aa00",
        corner_radius=12
    )
    encrypt_button.grid(row=0, column=0, padx=15)

    decrypt_button = ctk.CTkButton(
        frame,
        text="Decrypt",
        command=decrypt_command,
        width=180,
        height=50,
        font=("Segoe UI", 16, "bold"),
        fg_color="blue",
        hover_color="#2222ff",
        corner_radius=12
    )
    decrypt_button.grid(row=0, column=1, padx=15)

    return frame