def xor_encrypt(plaintext_bytes: bytes, key_bytes: bytes) -> bytes:
    """
    Chiffre les données en utilisant l'opération XOR avec une clé.
    
    Args:
        plaintext_bytes: Les octets du texte en clair à chiffrer
        key_bytes: La clé de chiffrement (sera répétée si nécessaire)
    
    Returns:
        Les octets chiffrés (ciphertext)
    """
    ciphertext = []  # Liste vide pour stocker les octets chiffrés
    key_length = len(key_bytes)
    
    # Parcourir chaque octet du texte en clair
    for i in range(len(plaintext_bytes)):
        k = key_bytes[i % key_length]  # Clé cyclique (MOD key_length)
        c = plaintext_bytes[i] ^ k     # Opération XOR
        ciphertext.append(c)           # Ajouter à la liste
    
    return bytes(ciphertext)


def xor_decrypt(ciphertext_bytes: bytes, key_bytes: bytes) -> bytes:
    """
    Déchiffre les données en utilisant l'opération XOR avec une clé.
    
    Note: Le déchiffrement XOR est identique au chiffrement (propriété XOR).
    
    Args:
        ciphertext_bytes: Les octets chiffrés à déchiffrer
        key_bytes: La clé de déchiffrement (même clé que pour le chiffrement)
    
    Returns:
        Les octets déchiffrés (plaintext)
    """
    return xor_encrypt(ciphertext_bytes, key_bytes)


# Exemple d'utilisation
if __name__ == "__main__":
    # Message à chiffrer
    message = "Bonjour, ceci est un message secret!"
    key = "cle_secrete"
    
    # Conversion en bytes
    plaintext_bytes = message.encode('utf-8')
    key_bytes = key.encode('utf-8')
    
    # Chiffrement
    encrypted = xor_encrypt(plaintext_bytes, key_bytes)
    print(f"Message original: {message}")
    print(f"Message chiffré (hex): {encrypted.hex()}")
    
    # Déchiffrement
    decrypted = xor_decrypt(encrypted, key_bytes)
    print(f"Message déchiffré: {decrypted.decode('utf-8')}")
