import random

def cesar_encrypt(plaintext, shift):
    """
    Chiffre un texte avec le chiffrement de César.
    
    Le chiffrement de César décale chaque lettre de l'alphabet 
    d'un nombre fixe de positions (la clé/shift).
    
    Paramètres:
        plaintext (str): Le texte clair à chiffrer
        shift (int): Le décalage (clé de chiffrement), entre 0 et 25
    
    Retourne:
        str: Le texte chiffré
    """
    ciphertext = ""
    
    for char in plaintext:
        if char.isalpha():
            # Déterminer si c'est une majuscule ou minuscule
            if char.isupper():
                # Décaler dans l'alphabet majuscule (A=65 à Z=90)
                # Formule: (position + shift) mod 26
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Décaler dans l'alphabet minuscule (a=97 à z=122)
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += new_char
        else:
            # Garder les caractères non alphabétiques inchangés
            ciphertext += char
    
    return ciphertext


def cesar_decrypt(ciphertext, shift):
    """
    Déchiffre un texte chiffré avec le chiffrement de César.
    
    Le déchiffrement est simplement le chiffrement avec un décalage 
    négatif (ou équivalent: 26 - shift).
    
    Paramètres:
        ciphertext (str): Le texte chiffré à déchiffrer
        shift (int): Le décalage utilisé lors du chiffrement
    
    Retourne:
        str: Le texte clair retrouvé
    """
    # Déchiffrer = chiffrer avec le décalage inverse
    return cesar_encrypt(ciphertext, -shift)

# === Exemple d'utilisation ===
if __name__ == "__main__":
    # Texte clair à chiffrer
    plaintext = "Hello, ca va ?"
    shift = random.randint(0, 25)     # Décalage aléatoire
    
    print(f"Texte clair: {plaintext}")
    print(f"Clé (décalage): {shift}")
    
    # Chiffrement
    ciphertext = cesar_encrypt(plaintext, shift)
    print(f"Après chiffrement → Texte chiffré: {ciphertext}")
    
    # Déchiffrement
    decrypted = cesar_decrypt(ciphertext, shift)
    print(f"Après déchiffrement → Texte retrouvé: {decrypted}")
