from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# Assuming the private key is in a file named 'private_key.pem'
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,  # Replace with your password if the key is encrypted
        backend=default_backend()
    )

# Now the private_key variable holds the private key object
