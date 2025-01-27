# HashBite 🦇

**HashBite** is a powerful and easy-to-use Python program designed to crack hashed passwords using the `hashlib` module via a **wordlist attack**. It supports a wide range of hash algorithms and offers a simple interface to attempt cracking hashes by comparing each hash with possible plaintext values from a wordlist. Supported algorithms include MD5, SHA-1, SHA-256, SHA-512, and many more.

## Features

- **Multiple Hashing Algorithms**: Supports a variety of popular hashing algorithms including SHA-1, SHA-256, SHA-512, MD5, and others.
- **Built in wordlists**: Comes prepackaged with rockyou.txt darkweb2017.txt and cain&abel.txt
- **User-Friendly**: Simple and intuitive command-line interface with colored output and interactive prompts.
- **Open Source**: Completely open-source, built with Python.

## Supported Algorithms

The following hashing algorithms are supported and guaranteed to work:

- SHA1
- SHA224
- SHA256
- SHA384
- SHA512
- SHA3_224
- SHA3_256
- SHA3_384
- SHA3_512
- MD5
- Blake2b
- Blake2s
- Shake_128
- Shake_256

## Requirements

- Python 3.x
- `rich`: For enhanced terminal output with colors and styling.
- `prompt_toolkit`: For building interactive command-line interfaces.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Jdigitalz/HashBite.git
   cd hashbite
2. Install python libraries
   ```bash
   pip install -r requirements.txt 
3. download rockyou.txt and add to wordlists
   ```bash
   wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt && mv rockyou.txt wordlists

### Usage
   ```bash
    python hashbite.py
   ```
## Images
![image_alt](https://github.com/Jdigitalz/HashBite/blob/main/assets/hash_options.png?raw=true)
##
![image_alt](https://github.com/Jdigitalz/HashBite/blob/main/assets/hashuse.png?raw=true)

