import customtkinter as ctk

def create_footer(root):
    footer = ctk.CTkLabel(
        root,
        text="Developed by Aryan Sharma",
        font=("Segoe UI", 12, "bold"),
        text_color="#666666"
    )

    footer.pack(side="bottom", pady=18)