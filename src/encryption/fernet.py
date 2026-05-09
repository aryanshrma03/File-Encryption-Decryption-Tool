from cryptography.fernet import Fernet, InvalidToken
import base64
import hashlib
import os

from config.paths import ENCRYPT_FOLDER, DECRYPT_FOLDER


def generate_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)


def encrypt_file(file_path, password):
    key = generate_key(password)
    cipher = Fernet(key)

    with open(file_path, 'rb') as file:
        file_data = file.read()

    encrypted_data = cipher.encrypt(file_data)

    filename = os.path.basename(file_path)

    encrypted_file_path = os.path.join(
        ENCRYPT_FOLDER,
        filename + ".enc"
    )

    with open(encrypted_file_path, 'wb') as file:
        file.write(encrypted_data)

    return encrypted_file_path


def decrypt_file(file_path, password):
    key = generate_key(password)
    cipher = Fernet(key)

    try:
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()

        decrypted_data = cipher.decrypt(encrypted_data)

        filename = os.path.basename(file_path).replace(".enc", "")

        decrypted_file_path = os.path.join(
            DECRYPT_FOLDER,
            filename
        )

        with open(decrypted_file_path, 'wb') as file:
            file.write(decrypted_data)

        return decrypted_file_path

    except InvalidToken:
        raise Exception("Incorrect password! Decryption failed.")

    except Exception as e:
        raise Exception(f"Error during decryption: {str(e)}")