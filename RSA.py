"""
RSA - Algorithme de chiffrement asymétrique.
Implémente la génération de clés RSA, le chiffrement et le déchiffrement.

L'algorithme RSA est basé sur la difficulté de factoriser le produit de deux grands nombres premiers.
- Clé publique (n, e) : utilisée pour chiffrer
- Clé privée (n, d) : utilisée pour déchiffrer
"""

import random
import math


def is_prime(n: int, k: int = 10) -> bool:
    """
    Teste si un nombre est premier en utilisant le test de Miller-Rabin.
    
    Args:
        n: Le nombre à tester
        k: Le nombre d'itérations (plus k est grand, plus le test est précis)
    
    Returns:
        True si n est probablement premier, False sinon
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Écrire n-1 comme 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Test de Miller-Rabin
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True


def random_prime(bits: int) -> int:
    """
    Génère un nombre premier aléatoire de la taille spécifiée en bits.
    
    Args:
        bits: Le nombre de bits souhaité pour le nombre premier
    
    Returns:
        Un nombre premier aléatoire
    """
    while True:
        # Générer un nombre aléatoire de 'bits' bits
        n = random.getrandbits(bits)
        # S'assurer que le bit de poids fort est à 1 (pour avoir exactement 'bits' bits)
        n |= (1 << (bits - 1))
        # S'assurer que le nombre est impair
        n |= 1
        
        if is_prime(n):
            return n


def gcd(a: int, b: int) -> int:
    """
    Calcule le PGCD (Plus Grand Commun Diviseur) de deux nombres.
    Utilise l'algorithme d'Euclide.
    
    Args:
        a: Premier nombre
        b: Deuxième nombre
    
    Returns:
        Le PGCD de a et b
    """
    while b:
        a, b = b, a % b
    return a


def modular_inverse(e: int, phi: int) -> int:
    """
    Calcule l'inverse modulaire de e modulo phi.
    Utilise l'algorithme d'Euclide étendu.
    Trouve d tel que (d * e) mod phi = 1
    
    Args:
        e: Le nombre dont on cherche l'inverse
        phi: Le module
    
    Returns:
        L'inverse modulaire de e modulo phi
    
    Raises:
        ValueError: Si l'inverse modulaire n'existe pas
    """
    # Algorithme d'Euclide étendu
    original_phi = phi
    x0, x1 = 0, 1
    
    if phi == 1:
        return 0
    
    while e > 1:
        q = e // phi
        phi, e = e % phi, phi
        x0, x1 = x1 - q * x0, x0
    
    if x1 < 0:
        x1 += original_phi
    
    return x1


def rsa_keygen(keysize: int = 1024) -> tuple:
    """
    Génère une paire de clés RSA (publique et privée).
    
    Algorithme:
    1. Choisir deux grands nombres premiers distincts p et q
    2. Calculer n = p * q (le module)
    3. Calculer φ(n) = (p-1) * (q-1) (l'indicatrice d'Euler)
    4. Choisir e tel que 1 < e < φ(n) et pgcd(e, φ(n)) = 1
    5. Calculer d = inverse modulaire de e modulo φ(n)
    6. Clé publique = (n, e), Clé privée = (n, d)
    
    Args:
        keysize: La taille de la clé en bits (par défaut 1024)
    
    Returns:
        Un tuple (clé_publique, clé_privée) où:
        - clé_publique = (n, e)
        - clé_privée = (n, d)
    """
    # 1. Choisir deux grands nombres premiers distincts
    p = random_prime(keysize // 2)
    q = random_prime(keysize // 2)
    
    # S'assurer que p et q sont différents
    while p == q:
        q = random_prime(keysize // 2)
    
    # 2. Calculer le module n
    n = p * q
    
    # 3. Calculer l'indicatrice d'Euler φ(n) = (p-1) * (q-1)
    phi = (p - 1) * (q - 1)
    
    # 4. Choisir l'exposant public e
    # Valeur commune : 65537 (0x10001) si pgcd(e, φ) = 1
    e = 65537
    if gcd(e, phi) != 1:
        # Si 65537 ne convient pas, chercher un autre e
        e = 3
        while gcd(e, phi) != 1:
            e += 2
    
    # 5. Calculer l'exposant privé d (inverse modulaire de e modulo φ)
    d = modular_inverse(e, phi)
    
    # 6. Construire les clés
    public_key = (n, e)   # PK = (n, e)
    private_key = (n, d)  # SK = (n, d)
    
    return public_key, private_key


def rsa_encrypt(m: int, public_key: tuple) -> int:
    """
    Chiffre un message avec la clé publique RSA.
    
    Formule: c = m^e mod n
    
    Args:
        m: Le message à chiffrer (entier, 0 ≤ m < n)
        public_key: La clé publique (n, e)
    
    Returns:
        Le texte chiffré c (entier)
    """
    n, e = public_key
    
    # Vérifier que le message est valide (0 ≤ m < n)
    if m < 0 or m >= n:
        raise ValueError(f"Le message doit être un entier entre 0 et {n-1}")
    
    # Calculer c = m^e mod n
    c = pow(m, e, n)
    
    return c


def rsa_decrypt(c: int, private_key: tuple) -> int:
    """
    Déchiffre un texte chiffré avec la clé privée RSA.
    
    Formule: m = c^d mod n
    
    Args:
        c: Le texte chiffré (entier)
        private_key: La clé privée (n, d)
    
    Returns:
        Le message déchiffré m (entier)
    """
    n, d = private_key
    
    # Calculer m = c^d mod n
    m = pow(c, d, n)
    
    return m


def text_to_int(text: str) -> int:
    """
    Convertit une chaîne de caractères en entier.
    
    Args:
        text: La chaîne à convertir
    
    Returns:
        L'entier correspondant
    """
    return int.from_bytes(text.encode('utf-8'), 'big')


def int_to_text(number: int) -> str:
    """
    Convertit un entier en chaîne de caractères.
    
    Args:
        number: L'entier à convertir
    
    Returns:
        La chaîne de caractères correspondante
    """
    # Calculer le nombre d'octets nécessaires
    byte_length = (number.bit_length() + 7) // 8
    if byte_length == 0:
        byte_length = 1
    return number.to_bytes(byte_length, 'big').decode('utf-8')


def rsa_encrypt_text(text: str, public_key: tuple) -> int:
    """
    Chiffre un message texte avec RSA.
    
    Args:
        text: Le message texte à chiffrer
        public_key: La clé publique (n, e)
    
    Returns:
        Le texte chiffré (entier)
    """
    m = text_to_int(text)
    n, _ = public_key
    
    if m >= n:
        raise ValueError("Le message est trop long pour cette clé. Utilisez une clé plus grande.")
    
    return rsa_encrypt(m, public_key)


def rsa_decrypt_text(c: int, private_key: tuple) -> str:
    """
    Déchiffre un texte chiffré RSA en message texte.
    
    Args:
        c: Le texte chiffré (entier)
        private_key: La clé privée (n, d)
    
    Returns:
        Le message déchiffré (chaîne de caractères)
    """
    m = rsa_decrypt(c, private_key)
    return int_to_text(m)


# Exemple d'utilisation
if __name__ == "__main__":
    print("=" * 60)
    print("          DÉMONSTRATION RSA")
    print("=" * 60)
    
    # Générer les clés avec une petite taille pour la démonstration
    print("\n[1] Génération des clés RSA (512 bits pour la démo)...")
    public_key, private_key = rsa_keygen(512)
    
    n, e = public_key
    _, d = private_key
    
    print(f"\n[PUBLIC KEY] Cle publique (n, e):")
    print(f"   n = {n}")
    print(f"   e = {e}")
    
    print(f"\n[PRIVATE KEY] Cle privee (n, d):")
    print(f"   d = {d}")
    
    # Test avec un entier
    print("\n" + "-" * 60)
    print("[2] Test avec un entier")
    message_int = 42
    print(f"   Message original : {message_int}")
    
    encrypted_int = rsa_encrypt(message_int, public_key)
    print(f"   Message chiffré  : {encrypted_int}")
    
    decrypted_int = rsa_decrypt(encrypted_int, private_key)
    print(f"   Message déchiffré: {decrypted_int}")
    
    # Test avec du texte
    print("\n" + "-" * 60)
    print("[3] Test avec du texte")
    message_text = "Hello RSA!"
    print(f"   Message original : {message_text}")
    
    encrypted_text = rsa_encrypt_text(message_text, public_key)
    print(f"   Message chiffré  : {encrypted_text}")
    
    decrypted_text = rsa_decrypt_text(encrypted_text, private_key)
    print(f"   Message déchiffré: {decrypted_text}")
    
    print("\n" + "=" * 60)
    print("[OK] Demonstration terminee!")
    print("=" * 60)
