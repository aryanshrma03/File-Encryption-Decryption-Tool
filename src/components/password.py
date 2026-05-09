def toggle_password(entry, variable):
    if variable.get():
        entry.configure(show="")
    else:
        entry.configure(show="*")