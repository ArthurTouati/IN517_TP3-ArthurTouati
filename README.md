# 🔐 TP3 - Algorithmes de Chiffrement

> Travaux Pratiques - IN517 Principes Fondamentaux et Techniques de Cryptographie  
> IPSA - Aéro 5

## 📋 Description

Ce projet implémente différents algorithmes de chiffrement classiques et modernes en Python. Il permet de comprendre les principes fondamentaux de la cryptographie symétrique à travers des exemples pratiques.

## 🚀 Algorithmes Implémentés

| Algorithme | Fichier | Type |
|------------|---------|------|
| César | `cesar_cypher.py` | Substitution monoalphabétique |
| Substitution | `substitution_cypher.py` | Substitution monoalphabétique |
| XOR | `cryptage_xor.py` | Chiffrement par flux |
| Feistel | `feistel_block_cypher_cryptage.py` | Chiffrement par bloc |
| AES-GCM | `aes_gcm.py` | Chiffrement authentifié |

## 📦 Installation

```bash
# Cloner le dépôt
git clone https://github.com/votre-utilisateur/tp3-cryptographie.git
cd tp3-cryptographie

# Installer les dépendances (optionnel, pour AES-GCM)
pip install cryptography
```

## 💻 Utilisation

### Programme Principal (Menu Interactif)

```bash
python main.py
```

Le programme affiche un menu permettant de :
1. Choisir un algorithme de chiffrement
2. Entrer un texte à chiffrer
3. Voir le résultat chiffré et la vérification

### Utilisation Individuelle

Chaque module peut être exécuté séparément :

```bash
python cesar_cypher.py
python substitution_cypher.py
python cryptage_xor.py
python feistel_block_cypher_cryptage.py
python aes_gcm.py
```

## 📖 Détail des Algorithmes

### 1. Chiffrement de César
Décale chaque lettre de l'alphabet d'un nombre fixe de positions.
- **Clé** : Un entier entre 0 et 25
- **Attaque** : Force brute (26 possibilités)

### 2. Chiffrement par Substitution
Remplace chaque lettre par une autre selon une table de correspondance.
- **Clé** : Table de substitution (26! possibilités)
- **Attaque** : Analyse de fréquence

### 3. Chiffrement XOR
Applique l'opération XOR entre le texte et une clé cyclique.
- **Propriété** : Chiffrement = Déchiffrement
- **Clé** : Chaîne de caractères quelconque

### 4. Chiffrement Feistel (2 tours)
Structure de chiffrement par bloc utilisée dans DES.
- **Tours** : 2 rounds avec clés K1 et K2
- **Déchiffrement** : Même algorithme, clés inversées

### 5. AES-GCM
Chiffrement authentifié standard moderne.
- **Clé** : 128, 192 ou 256 bits
- **Authentification** : Garantit l'intégrité des données

## 📁 Structure du Projet

```
TP3/
├── main.py                         # Programme principal interactif
├── cesar_cypher.py                 # Chiffrement de César
├── substitution_cypher.py          # Chiffrement par substitution
├── cryptage_xor.py                 # Chiffrement XOR
├── feistel_block_cypher_cryptage.py # Chiffrement Feistel
├── aes_gcm.py                      # Chiffrement AES-GCM
└── README.md                       # Ce fichier
```

## 👨‍🎓 Auteur

Projet réalisé dans le cadre du cours IN517 - IPSA 2025

## 📜 Licence

Ce projet est destiné à des fins éducatives.
