import hashlib
import base64
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# Load RSA public key from file
with open('public_key.pem', 'rb') as f:
    public_key = f.read()

# Load RSA private key from file
with open('private_key.pem', 'rb') as f:
    private_key = f.read()

# Hashing using SHA256
def sha256_hash(message):
    hash_object = hashlib.sha256(message.encode())
    return hash_object.hexdigest()

# Encryption using RSA Algorithm
def rsa_encrypt(message, public_key):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

# Decryption using RSA Algorithm
def rsa_decrypt(encrypted_message, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()

# Example Use Case
message = "Fauzan Syawalino"
hashed_message = sha256_hash(message)
encrypted_message = rsa_encrypt(hashed_message, public_key)

# Convert ciphertext into String and Heksadesimal
encrypted_message_string = base64.b64encode(encrypted_message).decode()
encrypted_message_hexadecimal = encrypted_message.hex()

decrypted_message = rsa_decrypt(encrypted_message, private_key)

print("\nOriginal message:", message)
print("\nHashed message:", hashed_message)
print("\nEncrypted message (String):", encrypted_message_string)
print("\nEncrypted message (Hexadecimal):", encrypted_message_hexadecimal)
print("\nDecrypted message:", decrypted_message)