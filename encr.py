import base64
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

def encrypt_file(file_path, password):
    # Generate a random salt
    salt = get_random_bytes(8)

    # Use PBKDF2 to derive a key and IV from the password and salt
    key_iv = PBKDF2(password, salt, dkLen=48, count=10000)
    key = key_iv[:32]
    iv = key_iv[32:]

    # Create a cipher object and encrypt the file
    cipher = AES.new(key, AES.MODE_CFB, iv)
    with open(file_path, 'rb') as f:
        plaintext = f.read()
    ciphertext = cipher.encrypt(plaintext)

    # Write the salt, ciphertext, and HMAC to the output file
    with open(file_path + '.encrypted', 'wb') as f:
        f.write(salt)
        f.write(ciphertext)
        f.write(hmac(key, ciphertext, sha256))

# Use the function to encrypt a file
encrypt_file('/path/to/file.txt', 'password')

