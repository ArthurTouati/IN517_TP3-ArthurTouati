import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def aes_gcm_encrypt(key: bytes, plaintext: bytes, associated_data: bytes = b""):
    """
    Encrypt with AES-GCM.
    key: 16, 24, or 32 bytes (AES-128/192/256)
    returns (nonce, ciphertext)
    """
    aesgcm = AESGCM(key)
    nonce = os.urandom(12) # 96-bit nonce
    ciphertext = aesgcm.encrypt(nonce, plaintext, associated_data)
    return nonce, ciphertext
def aes_gcm_decrypt(key: bytes, nonce: bytes, ciphertext: bytes,associated_data: bytes = b""):
    """
    Decrypt with AES-GCM.
    Raises an exception if authentication fails.
    """
    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, associated_data)
    return plaintext
# Example usage
if __name__ == "__main__":
    key = AESGCM.generate_key(bit_length=256) # 32-byte key
    plaintext = b"Symmetric cryptography example"
    aad = b"header or metadata"
    nonce, ciphertext = aes_gcm_encrypt(key, plaintext, aad)
    print("Ciphertext (hex):", ciphertext.hex())
    recovered = aes_gcm_decrypt(key, nonce, ciphertext, aad)
    print("Recovered:", recovered.decode())