# Vig3n3r3 - Vigenère Cipher Cracker

Vig3n3r3 is a Python toolkit for encrypting, decrypting, and cracking Vigenère ciphers using various cryptanalysis techniques. This project pays tribute to the historical Vigenère cipher while showcasing modern methods for breaking it, including brute-force attacks, dictionary attacks, and crib-based attacks.

## Features

- **Encrypt and Decrypt**: Encode and decode messages using the Vigenère cipher.
- **Brute-Force Attack**: Automatically crack the cipher by trying all possible key combinations up to a given length.
- **Dictionary Attack**: Use a word list to crack the cipher if the key is an English word.
- **Crib Attack**: Crack the cipher by leveraging known plaintext segments.
- **Fitness Scoring**: Evaluate the likelihood of decrypted text based on letter frequency and n-gram models (monograms, bigrams, trigrams, quadgrams).

## Requirements

- Python 3.x
- `english_monograms.txt`, `english_bigrams.txt`, `english_trigrams.txt`, `english_quadgrams.txt`
- `enable1.txt` (wordlist for dictionary attack)

## Installation

Clone the repository and install any necessary dependencies.

```bash
git clone https://github.com/yourusername/vig3n3r3.git
cd vig3n3r3
```

Make sure to download and place the required n-gram files and `enable1.txt` dictionary in the working directory.

## Usage

The tool can be used via the command line to crack encrypted messages. Below are some common use cases:

### Brute-Force Attack

```bash
python vig3n3r3.py "CIPHERTEXT" --method 2 --keylength 3
```

This will attempt to crack the ciphertext using a brute-force attack with a key length of 3.

### Dictionary Attack

```bash
python vig3n3r3.py "CIPHERTEXT" --method 1 --keylength 3
```

This will attempt to crack the ciphertext using a dictionary attack with a key length of 3, using words from `enable1.txt`.

### Crib Attack

```bash
python vig3n3r3.py "CIPHERTEXT" --method 3 --crib "KNOWNPLAINTEXT"
```

This will attempt to crack the ciphertext using a known plaintext (crib).

## Tests

Run the test suite to ensure the encrypt and decrypt functions work correctly:

```bash
python -m unittest test_vig3n3r3.py
```

## Attribution

This project uses the **ENABLE (Enhanced North American Benchmark LExicon)** word list for dictionary attacks, sourced from the [ENABLE project](https://www.wordgamedictionary.com/enable/). The n-gram frequency data (monograms, bigrams, trigrams, quadgrams) was sourced from various public datasets commonly used in cryptography research.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to fork this repository and submit pull requests for improvements or new cryptanalysis techniques.

---

## Addendum

You can find the full code and project details on GitHub here: [GitHub Repository](https://github.com/yourusername/vig3n3r3). Contributions and feedback are welcome!
