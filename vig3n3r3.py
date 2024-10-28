import argparse
import math
from itertools import product
import random

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def load_ngrams(filename):
    ngrams = {}
    total = 0
    with open(filename) as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                key, count = parts
                ngrams[key] = float(count)  # Use float() to handle decimal values
                total += float(count)
    for key in ngrams:
        ngrams[key] = math.log10(ngrams[key] / total)
    return ngrams

# Load n-grams
monograms = load_ngrams('english_monograms.txt')
bigrams = load_ngrams('english_bigrams.txt')
trigrams = load_ngrams('english_trigrams.txt')
quadgrams = load_ngrams('english_quadgrams.txt')

# ASCII Art Banner for the top
def display_top_banner():
    banner = """
██╗   ██╗██╗ ██████╗ ███████╗███╗   ██╗███████╗██████╗ ███████╗    ██████╗ ██╗   ██╗    ██╗ ██████╗██╗  ██╗██████╗ ██╗   ██╗███████╗       ██╗ 
██║   ██║██║██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔════╝    ██╔══██╗╚██╗ ██╔╝    ██║██╔════╝██║  ██║██╔══██╗██║   ██║██╔════╝    ██╗╚██╗
██║   ██║██║██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝█████╗      ██████╔╝ ╚████╔╝     ██║██║     ███████║██████╔╝██║   ██║███████╗    ╚═╝ ██║
╚██╗ ██╔╝██║██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══╝      ██╔══██╗  ╚██╔╝      ██║██║     ╚════██║██╔══██╗██║   ██║╚════██║    ▄█╗ ██║
 ╚████╔╝ ██║╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║███████╗    ██████╔╝   ██║       ██║╚██████╗     ██║██║  ██║╚██████╔╝███████║    ▀═╝██╔╝
  ╚═══╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚══════╝    ╚═════╝    ╚═╝       ╚═╝ ╚═════╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝       ╚═╝
    """
    print(banner)

# ASCII Art Banner for success
def display_success_banner(key):
    banner = f"""
███████╗██╗   ██╗ ██████╗ ██████╗██████╗ ███████╗███████╗
██╔════╝██║   ██║██╔════╝██╔════╝╚════██╗██╔════╝██╔════╝
███████╗██║   ██║██║     ██║      █████╔╝███████╗███████╗
╚════██║██║   ██║██║     ██║      ╚═══██╗╚════██║╚════██║
███████║╚██████╔╝╚██████╗╚██████╗██████╔╝███████║███████║

      Key Cracked: {key}
      Cipher Successfully Decrypted! 🕵️‍♂️
    """
    print(banner)

def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    decrypted = ''
    for i in range(len(ciphertext)):
        if ciphertext[i] in ALPHABET:
            c = ALPHABET.index(ciphertext[i])
            k = ALPHABET.index(key[i % len(key)])
            p = (c - k + 26) % 26
            decrypted += ALPHABET[p]
        else:
            decrypted += ciphertext[i]
    return decrypted

def fitness(text):
    score = 0.0
    length = len(text)
    if length == 0:
        return float('-inf')
    
    # Monograms
    for char in text:
        if char in monograms:
            score += monograms[char]
        else:
            score += -5
    
    # Bigrams
    for i in range(len(text) - 1):
        bigram = text[i:i+2]
        if bigram in bigrams:
            score += bigrams[bigram]
        else:
            score += -3
    
    # Trigrams
    for i in range(len(text) - 2):
        trigram = text[i:i+3]
        if trigram in trigrams:
            score += trigrams[trigram]
        else:
            score += -6
    
    # Quadgrams
    for i in range(len(text) - 3):
        quadgram = text[i:i+4]
        if quadgram in quadgrams:
            score += quadgrams[quadgram]
        else:
            score += -9
    
    return score / length

# Brute-force attack (restored)
def brute_force(ciphertext, period):
    max_score = float('-inf')
    best_key = None
    best_plaintext = ''
    
    # Iterate through all possible key combinations
    for key_tuple in product(ALPHABET, repeat=period):
        key = ''.join(key_tuple)
        plaintext = decrypt(ciphertext, key)
        fit_score = fitness(plaintext)
        
        # Track the best result
        if fit_score > max_score:
            max_score = fit_score
            best_key = key
            best_plaintext = plaintext
    
    # Output the best result
    display_success_banner(best_key)
    print(f"Decrypted Text: {best_plaintext}")
    return list(best_key), best_plaintext

def dictionary_attack(ciphertext, keylength):
    words = [word.strip().upper() for word in open('words.txt') if len(word.strip()) == keylength]
    max_score = float('-inf')
    best_key = None
    best_plaintext = ''
    for key in words:
        plaintext = decrypt(ciphertext, key)
        fit_score = fitness(plaintext)
        if fit_score > max_score:
            max_score = fit_score
            best_key = key
            best_plaintext = plaintext
    display_success_banner(best_key)
    print(f"Decrypted Text: {best_plaintext}")
    return list(best_key), best_plaintext

def crib_attack(ciphertext, crib):
    crib = crib.upper()
    for i in range(len(ciphertext) - len(crib) + 1):
        segment = ciphertext[i:i + len(crib)]
        key_segment = ''
        for c_char, p_char in zip(segment, crib):
            c_idx = ALPHABET.index(c_char)
            p_idx = ALPHABET.index(p_char)
            k_idx = (c_idx - p_idx) % 26
            key_segment += ALPHABET[k_idx]
        print(f"Position {i}: Possible Key Segment: {key_segment}")
    return None

def main():
    display_top_banner()
    
    parser = argparse.ArgumentParser(description="Vigenère Cipher Cracker")
    parser.add_argument('ciphertext', type=str, help="Ciphertext to crack")
    parser.add_argument('--method', type=int, choices=[1, 2, 3], required=True, help="Select the attack method (1: Dictionary, 2: Brute-force, 3: Crib Attack)")
    parser.add_argument('--keylength', type=int, help="Key length for brute-force")
    parser.add_argument('--crib', type=str, help="Known plaintext (crib) for crib attacks")
    
    args = parser.parse_args()
    ciphertext = ''.join(filter(str.isalpha, args.ciphertext.upper()))
    
    if args.method == 1 and args.keylength:
        dictionary_attack(ciphertext, args.keylength)
    elif args.method == 2 and args.keylength:
        brute_force(ciphertext, args.keylength)
    elif args.method == 3 and args.crib:
        crib_attack(ciphertext, args.crib)
    else:
        print("Invalid method or missing arguments.")

if __name__ == "__main__":
    main()
