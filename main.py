"""
Programme principal pour tester différents algorithmes de chiffrement.
L'utilisateur peut choisir un algorithme et chiffrer/déchiffrer un texte.
"""

import cesar_cypher
import substitution_cypher
import cryptage_xor
import feistel_block_cypher_cryptage

# Pour AES-GCM (nécessite la bibliothèque cryptography)
try:
    import aes_gcm
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    AES_AVAILABLE = True
except ImportError:
    AES_AVAILABLE = False


def afficher_menu():
    """Affiche le menu principal."""
    print("\n" + "="*50)
    print("       OUTILS DE CHIFFREMENT - TP3 IPSA")
    print("="*50)
    print("\nChoisissez un algorithme de chiffrement:")
    print("  1. Chiffrement de César")
    print("  2. Chiffrement par Substitution")
    print("  3. Chiffrement XOR")
    print("  4. Chiffrement Feistel (2 tours)")
    if AES_AVAILABLE:
        print("  5. Chiffrement AES-GCM")
    else:
        print("  5. Chiffrement AES-GCM (non disponible - installer cryptography)")
    print("  0. Quitter")
    print("-"*50)


def chiffrement_cesar():
    """Interface pour le chiffrement de César."""
    print("\n--- Chiffrement de César ---")
    texte = input("Entrez le texte à chiffrer: ")
    
    while True:
        try:
            decalage = int(input("Entrez le décalage (0-25): "))
            if 0 <= decalage <= 25:
                break
            print("Le décalage doit être entre 0 et 25.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    
    chiffre = cesar_cypher.cesar_encrypt(texte, decalage)
    print(f"\nTexte chiffré: {chiffre}")
    
    # Proposer le déchiffrement
    dechiffre = cesar_cypher.cesar_decrypt(chiffre, decalage)
    print(f"Vérification (déchiffré): {dechiffre}")


def chiffrement_substitution():
    """Interface pour le chiffrement par substitution."""
    print("\n--- Chiffrement par Substitution ---")
    texte = input("Entrez le texte à chiffrer: ")
    
    # Générer un mapping aléatoire
    mapping = substitution_cypher.generate_random_mapping()
    print("\nTable de substitution générée aléatoirement.")
    
    chiffre = substitution_cypher.encrypt(texte, mapping)
    print(f"\nTexte chiffré: {chiffre}")
    
    # Déchiffrement
    reverse_mapping = substitution_cypher.get_reverse_mapping(mapping)
    dechiffre = substitution_cypher.decrypt(chiffre, reverse_mapping)
    print(f"Vérification (déchiffré): {dechiffre}")


def chiffrement_xor():
    """Interface pour le chiffrement XOR."""
    print("\n--- Chiffrement XOR ---")
    texte = input("Entrez le texte à chiffrer: ")
    cle = input("Entrez la clé: ")
    
    # Conversion en bytes
    texte_bytes = texte.encode('utf-8')
    cle_bytes = cle.encode('utf-8')
    
    # Chiffrement
    chiffre = cryptage_xor.xor_encrypt(texte_bytes, cle_bytes)
    print(f"\nTexte chiffré (hex): {chiffre.hex()}")
    
    # Déchiffrement
    dechiffre = cryptage_xor.xor_decrypt(chiffre, cle_bytes)
    print(f"Vérification (déchiffré): {dechiffre.decode('utf-8')}")


def chiffrement_feistel():
    """Interface pour le chiffrement Feistel."""
    print("\n--- Chiffrement Feistel (2 tours) ---")
    texte = input("Entrez le texte à chiffrer: ")
    
    # Générer les clés
    key_length = (len(texte) * 8) // 2
    if key_length < 1:
        key_length = 8
    
    key1 = feistel_block_cypher_cryptage.generate_key(key_length)
    key2 = feistel_block_cypher_cryptage.generate_key(key_length)
    
    print(f"\nClé K1 générée: {key1[:20]}..." if len(key1) > 20 else f"\nClé K1 générée: {key1}")
    print(f"Clé K2 générée: {key2[:20]}..." if len(key2) > 20 else f"Clé K2 générée: {key2}")
    
    # Chiffrement
    chiffre = feistel_block_cypher_cryptage.feistel_encrypt(texte, key1, key2)
    print(f"\nTexte chiffré: {chiffre}")
    
    # Déchiffrement
    dechiffre = feistel_block_cypher_cryptage.feistel_decrypt(chiffre, key1, key2)
    print(f"Vérification (déchiffré): {dechiffre}")


def chiffrement_aes_gcm():
    """Interface pour le chiffrement AES-GCM."""
    if not AES_AVAILABLE:
        print("\nAES-GCM n'est pas disponible. Installez la bibliothèque cryptography:")
        print("  pip install cryptography")
        return
    
    print("\n--- Chiffrement AES-GCM ---")
    texte = input("Entrez le texte à chiffrer: ")
    
    # Générer une clé AES-256
    key = AESGCM.generate_key(bit_length=256)
    print(f"\nClé AES-256 générée: {key.hex()[:32]}...")
    
    # Chiffrement
    texte_bytes = texte.encode('utf-8')
    nonce, chiffre = aes_gcm.aes_gcm_encrypt(key, texte_bytes)
    
    print(f"\nNonce: {nonce.hex()}")
    print(f"Texte chiffré (hex): {chiffre.hex()}")
    
    # Déchiffrement
    dechiffre = aes_gcm.aes_gcm_decrypt(key, nonce, chiffre)
    print(f"Vérification (déchiffré): {dechiffre.decode('utf-8')}")


def main():
    """Fonction principale du programme."""
    print("\nBienvenue dans l'outil de chiffrement TP3!")
    
    while True:
        afficher_menu()
        choix = input("\nVotre choix: ").strip()
        
        if choix == "1":
            chiffrement_cesar()
        elif choix == "2":
            chiffrement_substitution()
        elif choix == "3":
            chiffrement_xor()
        elif choix == "4":
            chiffrement_feistel()
        elif choix == "5":
            chiffrement_aes_gcm()
        elif choix == "0":
            print("\nAu revoir!")
            break
        else:
            print("\nChoix invalide. Veuillez réessayer.")
        
        input("\nAppuyez sur Entrée pour continuer...")


if __name__ == "__main__":
    main()
