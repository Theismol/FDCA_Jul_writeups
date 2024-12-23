from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

def reverse_s_transformation(s):
    char_array = list(s)
    for index in range(0, len(char_array) - 1, 2):
        char_array[index], char_array[index + 1] = char_array[index + 1], char_array[index]
    return ''.join(char_array)

def decrypt_aes_cbc(encrypted_base64, key, iv):
    encrypted_bytes = base64.b64decode(encrypted_base64)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_bytes = decryptor.update(encrypted_bytes) + decryptor.finalize()

    decrypted_text = decrypted_bytes.decode('utf-8')
    return decrypted_text


kG = 'aS6BpWo8WyKFzwRzntKjW+nuD4+IeeZbMM2OmQcsTf2fgWoE81bOah1hmiPTLOzP'
key = b'valhallahpakkergodegaver'  
iv = bytes([0] * 16)  


reversed_kG = reverse_s_transformation(kG)


print(decrypt_aes_cbc(reversed_kG, key, iv))

