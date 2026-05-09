# 🔐 Secure File Encryption & Decryption Tool

A modern cybersecurity-based desktop application developed using Python and CustomTkinter that allows users to securely encrypt and decrypt files using password-based protection.

---

# 📌 Project Overview

The Secure File Encryption & Decryption Tool is designed to protect sensitive files from unauthorized access using encryption techniques. The application provides a simple and modern graphical user interface where users can:

- Select files
- Encrypt files securely
- Decrypt encrypted files
- Use password-based protection
- Store encrypted/decrypted files in organized folders

This project demonstrates practical cybersecurity concepts such as encryption, password security, secure file handling, and modular software architecture.

---

# 🚀 Features

- 🔒 File Encryption
- 🔓 File Decryption
- 🔑 Password-Based Security
- 👁 Show/Hide Password
- 📁 Organized File Storage
- ⚠ Incorrect Password Detection
- 🌙 Modern Dark-Themed UI
- 🧩 Modular Project Structure
- 💻 Offline Working

---

# 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| CustomTkinter | Modern GUI |
| Cryptography | Encryption & Decryption |
| VS Code | Development Environment |
| Hashlib | Password Hashing |

---

# 📂 Project Structure

```plaintext
Final_Semester_Project/
│
├── data/
│   ├── encrypt/
│   └── decrypt/
│
├── src/
│   │
│   ├── app/
│   │   └── gui.py
│   │
│   ├── encryption/
│   │   └── fernet.py
│   │
│   ├── components/
│   │   ├── header.py
│   │   ├── footer.py
│   │   ├── buttons.py
│   │   └── password.py
│   │
│   ├── config/
│   │   ├── paths.py
│   │   └── theme.py
│   │
│   └── main.py
│
├── requirements.txt
└── README.md