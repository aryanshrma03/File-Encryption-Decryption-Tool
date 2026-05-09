import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

ENCRYPT_FOLDER = os.path.join(
    BASE_DIR,
    "data",
    "encrypt"
)

DECRYPT_FOLDER = os.path.join(
    BASE_DIR,
    "data",
    "decrypt"
)

os.makedirs(ENCRYPT_FOLDER, exist_ok=True)
os.makedirs(DECRYPT_FOLDER, exist_ok=True)