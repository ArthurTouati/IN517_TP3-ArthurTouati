import random

def text_to_binary(text):
    """Convertit un texte en chaîne binaire (8 bits par caractère)."""
    binary = ""
    for char in text:
        # Convertir chaque caractère en valeur ASCII puis en binaire sur 8 bits
        binary += format(ord(char), '08b')
    return binary

def binary_to_text(binary):
    """Convertit une chaîne binaire en texte."""
    text = ""
    # Traiter par blocs de 8 bits
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) == 8:
            text += chr(int(byte, 2))
    return text

def xor(a, b):
    """Effectue un XOR entre deux chaînes binaires de même longueur."""
    result = ""
    for i in range(len(a)):
        # XOR: 0^0=0, 0^1=1, 1^0=1, 1^1=0
        result += '1' if a[i] != b[i] else '0'
    return result

def generate_key(length):
    """Génère une clé binaire aléatoire de la longueur spécifiée."""
    key = ""
    for _ in range(length):
        key += str(random.randint(0, 1))
    return key

def feistel_encrypt(plaintext, key1, key2):
    """
    Chiffrement Feistel à 2 tours.
    
    Étapes:
    1. Convertir le texte en binaire
    2. Diviser en deux moitiés (L0 et R0)
    3. Tour 1: f1 = R0 XOR K1, R1 = L0 XOR f1, L1 = R0
    4. Tour 2: f2 = R1 XOR K2, R2 = L1 XOR f2, L2 = R1
    5. Texte chiffré = L2 || R2
    """
    # Étape 1: Convertir le texte clair en binaire
    binary = text_to_binary(plaintext)
    
    # S'assurer que la longueur est paire (ajouter un padding si nécessaire)
    if len(binary) % 2 != 0:
        binary += '0'
    
    # Étape 2: Diviser en deux moitiés
    mid = len(binary) // 2
    L0 = binary[:mid]  # Moitié gauche
    R0 = binary[mid:]  # Moitié droite
    
    # Ajuster les clés à la taille des moitiés
    half_size = len(L0)
    K1 = (key1 * ((half_size // len(key1)) + 1))[:half_size]
    K2 = (key2 * ((half_size // len(key2)) + 1))[:half_size]
    
    # Tour 1 (Encryption)
    f1 = xor(R0, K1)      # Calculer f1 = R0 XOR K1
    R1 = xor(L0, f1)      # Nouvelle moitié droite: R1 = L0 XOR f1
    L1 = R0               # Nouvelle moitié gauche: L1 = R0
    
    # Tour 2 (Encryption)
    f2 = xor(R1, K2)      # Calculer f2 = R1 XOR K2
    R2 = xor(L1, f2)      # Nouvelle moitié droite: R2 = L1 XOR f2
    L2 = R1               # Nouvelle moitié gauche: L2 = R1
    
    # Texte chiffré final: concaténer L2 et R2
    ciphertext_binary = L2 + R2
    
    return binary_to_text(ciphertext_binary)

def feistel_decrypt(ciphertext, key1, key2):
    """
    Déchiffrement Feistel à 2 tours.
    
    Le déchiffrement utilise le même algorithme que le chiffrement,
    mais avec les clés appliquées dans l'ordre inverse (K2 puis K1).
    """
    # Convertir le texte chiffré en binaire
    binary = text_to_binary(ciphertext)
    
    # Diviser en deux moitiés
    mid = len(binary) // 2
    L2 = binary[:mid]
    R2 = binary[mid:]
    
    # Ajuster les clés à la taille des moitiés
    half_size = len(L2)
    K1 = (key1 * ((half_size // len(key1)) + 1))[:half_size]
    K2 = (key2 * ((half_size // len(key2)) + 1))[:half_size]
    
    # Tour inverse 2 (avec K2) - inverse du Tour 2
    R1 = L2               # R1 = L2
    f2 = xor(R1, K2)      # Recalculer f2 = R1 XOR K2
    L1 = xor(R2, f2)      # L1 = R2 XOR f2
    
    # Tour inverse 1 (avec K1) - inverse du Tour 1
    R0 = L1               # R0 = L1
    f1 = xor(R0, K1)      # Recalculer f1 = R0 XOR K1
    L0 = xor(R1, f1)      # L0 = R1 XOR f1
    
    # Reconstituer le texte clair
    plaintext_binary = L0 + R0
    
    return binary_to_text(plaintext_binary)


# === Exemple d'utilisation ===
if __name__ == "__main__":
    # Texte clair à chiffrer
    plaintext = "Hello"
    print(f"Texte clair: {plaintext}")
    
    # Générer deux clés aléatoires pour les 2 tours
    # Chaque clé a une longueur égale à la moitié de la taille du bloc
    key_length = (len(plaintext) * 8) // 2  # Moitié de la taille en bits
    key1 = generate_key(key_length)
    key2 = generate_key(key_length)
    
    print(f"Clé K1: {key1}")
    print(f"Clé K2: {key2}")
    
    # Chiffrement
    ciphertext = feistel_encrypt(plaintext, key1, key2)
    print(f"Après chiffrement → Texte chiffré: {ciphertext}")
    
    # Déchiffrement
    decrypted = feistel_decrypt(ciphertext, key1, key2)
    print(f"Après déchiffrement → Texte retrouvé: {decrypted}")
    
    print("\n" + "="*50)
    
    # Deuxième exemple avec "Geeks"
    plaintext2 = "Geeks"
    print(f"\nTexte clair: {plaintext2}")
    
    key_length2 = (len(plaintext2) * 8) // 2
    key1_b = generate_key(key_length2)
    key2_b = generate_key(key_length2)
    
    print(f"Clé K1: {key1_b}")
    print(f"Clé K2: {key2_b}")
    
    ciphertext2 = feistel_encrypt(plaintext2, key1_b, key2_b)
    print(f"Après chiffrement → Texte chiffré: {ciphertext2}")
    
    decrypted2 = feistel_decrypt(ciphertext2, key1_b, key2_b)
    print(f"Après déchiffrement → Texte retrouvé: {decrypted2}")
