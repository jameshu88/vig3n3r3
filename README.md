
# Vig3n3r3 - A Python Vigenère Cipher Cracking Tool


```python
██╗   ██╗██╗ ██████╗ ███████╗███╗   ██╗███████╗██████╗ ███████╗    ██████╗ ██╗   ██╗    ██╗ ██████╗██╗  ██╗██████╗ ██╗   ██╗███████╗       ██╗ 
██║   ██║██║██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔════╝    ██╔══██╗╚██╗ ██╔╝    ██║██╔════╝██║  ██║██╔══██╗██║   ██║██╔════╝    ██╗╚██╗
██║   ██║██║██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝█████╗      ██████╔╝ ╚████╔╝     ██║██║     ███████║██████╔╝██║   ██║███████╗    ╚═╝ ██║
╚██╗ ██╔╝██║██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══╝      ██╔══██╗  ╚██╔╝      ██║██║     ╚════██║██╔══██╗██║   ██║╚════██║    ▄█╗ ██║
 ╚████╔╝ ██║╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║███████╗    ██████╔╝   ██║       ██║╚██████╗     ██║██║  ██║╚██████╔╝███████║    ▀═╝██╔╝
  ╚═══╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚══════╝    ╚═════╝    ╚═╝       ╚═╝ ╚═════╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝       ╚═╝
```


## About Vig3n3r3
Vig3n3r3 is a Python-based cryptography tool designed to encrypt, decrypt, and crack Vigenère cipher-encrypted messages using various cryptanalysis methods like brute force, dictionary attacks, and crib attacks. This project is built as a tribute to one of history's most famous ciphers and demonstrates how modern techniques can unravel what was once thought to be unbreakable.

## Table of Contents
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Citing Data Sources](#citing-data-sources)
- [Contributing](#contributing)
- [License](#license)
- [Link to Medium Article](#medium-article)

## Features
- **Encrypt and Decrypt** messages using the Vigenère cipher.
- **Brute-force Attack**: Crack a cipher by trying all possible keys.
- **Dictionary Attack**: Use a predefined wordlist to guess the key.
- **Crib Attack**: Use known plaintext segments to deduce the key.

## Setup

To get started with Vig3n3r3, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/vig3n3r3.git
cd vig3n3r3
```

### 2. Install dependencies

The project does not require any external Python packages. Just ensure you are using Python 3.x by checking:

```bash
python --version
```

### 3. Run the script

To run the script, use the following command:

```bash
python vig3n3r3.py "CIPHERTEXT" --method METHOD_NUMBER --keylength LENGTH --crib "KNOWN_PLAINTEXT"
```

- `CIPHERTEXT`: The encrypted message.
- `METHOD_NUMBER`: Choose from `1` (dictionary), `2` (brute force), `3` (crib attack), etc..
- `LENGTH`: The length of the key (required for methods 1 and 2).
- `KNOWN_PLAINTEXT`: The known part of the plaintext (required for method 3).

## Usage

### Example 1: Brute-force attack

```bash
python vig3n3r3.py "KXRKGIKXBKAL" --method 2 --keylength 3
```

This will attempt to brute force the key of length 3 and decrypt the message.

### Example 2: Dictionary attack

```bash
python vig3n3r3.py "KXRKGIKXBKAL" --method 1 --keylength 3
```

This will search for a valid key of length 3 using the words from `words.txt`.

### Example 3: Crib attack

```bash
python vig3n3r3.py "KXRKGIKXBKAL" --method 3 --crib "ATTACK"
```

This will attempt to find the key by using "ATTACK" as known plaintext.

## Citing Data Sources

- The **wordlist** for the dictionary attack was sourced from the [Openwall wordlists](https://www.openwall.com/wordlists/).
- The **monograms, bigrams, trigrams, and quadgrams** data used for frequency analysis were obtained from publicly available English text datasets, including Google's N-gram dataset.

## Contributing

Welcoming contributions! Please feel free to submit a pull request or open an issue if you'd like to improve or fix something.

### Instructions for contributing:
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Link to Medium Article
For a detailed breakdown of the history behind the Vigenère cipher, modern cryptography techniques, and the story of Vig3n3r3, read our [Medium article here](https://medium.com/your-link-to-article](https://medium.com/@jamesjinghuang/the-vigen%C3%A8re-cipher-from-unbreakable-enigma-to-cryptographic-relic-215761d30af8).

```python
███████╗██╗   ██╗ ██████╗ ██████╗██████╗ ███████╗███████╗
██╔════╝██║   ██║██╔════╝██╔════╝╚════██╗██╔════╝██╔════╝
███████╗██║   ██║██║     ██║      █████╔╝███████╗███████╗
╚════██║██║   ██║██║     ██║      ╚═══██╗╚════██║╚════██║
███████║╚██████╔╝╚██████╗╚██████╗██████╔╝███████║███████║
```

