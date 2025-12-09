import random
import string

def generate_random_mapping():
    """
    Génère une table de substitution aléatoire.
    Chaque lettre est mappée vers une autre lettre unique.
    
    Retourne:
        dict: Dictionnaire de mapping pour le chiffrement
    """
    alphabet = list(string.ascii_lowercase)
    shuffled = alphabet.copy()
    random.shuffle(shuffled)
    
    mapping = {}
    for i, letter in enumerate(alphabet):
        mapping[letter] = shuffled[i]
        # Ajouter aussi les majuscules
        mapping[letter.upper()] = shuffled[i].upper()
    
    return mapping

def get_reverse_mapping(mapping):
    """
    Crée le mapping inverse pour le déchiffrement.
    
    Paramètres:
        mapping (dict): Le mapping utilisé pour le chiffrement
    
    Retourne:
        dict: Le mapping inverse
    """
    reverse_mapping = {}
    for key, value in mapping.items():
        reverse_mapping[value] = key
    return reverse_mapping

def encrypt(text, mapping):
    """
    Chiffre un texte avec le chiffre de substitution.
    
    Paramètres:
        text (str): Le texte clair à chiffrer
        mapping (dict): La table de substitution
    
    Retourne:
        str: Le texte chiffré
    """
    result = ""
    
    for c in text:
        if c in mapping:
            # Substituer le caractère par son équivalent dans le mapping
            result += mapping[c]
        else:
            # Garder les espaces et la ponctuation inchangés
            result += c
    
    return result

def decrypt(text, reverse_mapping):
    """
    Déchiffre un texte avec le chiffre de substitution.
    
    Paramètres:
        text (str): Le texte chiffré à déchiffrer
        reverse_mapping (dict): La table de substitution inverse
    
    Retourne:
        str: Le texte clair retrouvé
    """
    result = ""
    
    for c in text:
        if c in reverse_mapping:
            # Substituer le caractère par son équivalent dans le mapping inverse
            result += reverse_mapping[c]
        else:
            # Garder les espaces et la ponctuation inchangés
            result += c
    
    return result


# === Exemple d'utilisation ===
if __name__ == "__main__":
    # Exemple de mapping comme dans le cours (a→q, b→w, c→e, d→r, ...)
    # Utilisons un mapping fixe pour la démonstration
    example_mapping = {
        'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't',
        'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p',
        'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g',
        'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z',
        'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n',
        'z': 'm',
        # Majuscules
        'A': 'Q', 'B': 'W', 'C': 'E', 'D': 'R', 'E': 'T',
        'F': 'Y', 'G': 'U', 'H': 'I', 'I': 'O', 'J': 'P',
        'K': 'A', 'L': 'S', 'M': 'D', 'N': 'F', 'O': 'G',
        'P': 'H', 'Q': 'J', 'R': 'K', 'S': 'L', 'T': 'Z',
        'U': 'X', 'V': 'C', 'W': 'V', 'X': 'B', 'Y': 'N',
        'Z': 'M'
    }
    
    print("=== Chiffre de Substitution ===\n")
    
    # Afficher la table de substitution
    print("Table de substitution:")
    for letter in 'abcd':
        print(f"  {letter} → {example_mapping[letter]}")
    print("  ...")
    
    # Texte clair à chiffrer
    plaintext = "Hello World!"
    print(f"\nTexte clair: {plaintext}")
    
    # Chiffrement
    ciphertext = encrypt(plaintext, example_mapping)
    print(f"Après chiffrement → Texte chiffré: {ciphertext}")
    
    # Déchiffrement
    reverse_mapping = get_reverse_mapping(example_mapping)
    decrypted = decrypt(ciphertext, reverse_mapping)
    print(f"Après déchiffrement → Texte retrouvé: {decrypted}")
    
    print("\n" + "="*50)
    print("\n=== Avec un mapping aléatoire ===\n")
    
    # Générer un mapping aléatoire
    random_mapping = generate_random_mapping()
    print("Nouveau mapping aléatoire généré")
    
    plaintext2 = "IPSA Crypto"
    print(f"Texte clair: {plaintext2}")
    
    ciphertext2 = encrypt(plaintext2, random_mapping)
    print(f"Après chiffrement → Texte chiffré: {ciphertext2}")
    
    reverse_random = get_reverse_mapping(random_mapping)
    decrypted2 = decrypt(ciphertext2, reverse_random)
    print(f"Après déchiffrement → Texte retrouvé: {decrypted2}")
