# Mnemonic CLI

A command-line interface tool for managing your secret phrases securely.

## Installation

The tool needs to be installed in your global Python environment. The easiest way to install Mnemonic CLI is using [pipx](https://pypa.github.io/pipx/):

```bash
git clone https://github.com/SIPLIbY/encoding-cli.git
cd encoding-cli
pipx install .
```

If you don't have pipx installed, you can install it first:

### On macOS:

```bash
brew install pipx
pipx ensurepath
```

### On Linux:

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

### On Windows:

```bash
python -m pip install --user pipx
python -m pipx ensurepath
```

## Usage

After installation, you can use the tool with the following commands:

### Basic Commands

```bash
# Encrypt a secret phrase
mnemonic encode -m "your secret phrase"
# or securely input the phrase when prompted
mnemonic encode

# Decrypt an encrypted message
mnemonic decode -m "encrypted-message"
# or securely input the message when prompted
mnemonic decode
```

### File Operations

```bash
# Encrypt a text file
mnemonic encode-file -i input.txt -o encrypted.txt
# or print result to console if no output specified
mnemonic encode-file -i input.txt

# Decrypt an encrypted file
mnemonic decode-file -i encrypted.txt -o decrypted.txt
# or print result to console if no output specified
mnemonic decode-file -i encrypted.txt
```

### Security Features

- All sensitive inputs (secrets and passwords) can be entered securely without showing up in terminal
- Passwords are never stored in shell history
- Uses AES-GCM encryption with PBKDF2 key derivation
- Optional file output to prevent sensitive data from appearing in terminal

## Requirements

- Python 3.7 or higher
- cryptography>=41.0.0
