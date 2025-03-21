#!/usr/bin/env python3

import argparse
from getpass import getpass
from .core import MnemonicEncryption

def main():
    parser = argparse.ArgumentParser(description='Encrypt and decrypt mnemonic phrases')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Encode command
    encode_parser = subparsers.add_parser('encode', help='Encrypt a mnemonic phrase')
    encode_parser.add_argument('-m', '--mnemonic', required=True, help='Mnemonic phrase to encrypt')

    # Decode command
    decode_parser = subparsers.add_parser('decode', help='Decrypt an encrypted mnemonic')
    decode_parser.add_argument('-m', '--message', required=True, help='Encrypted message to decrypt')

    args = parser.parse_args()

    try:
        password = getpass('Enter password: ')
        if args.command == 'encode':
            encrypted = MnemonicEncryption.encrypt(args.mnemonic, password)
            print(encrypted)
        elif args.command == 'decode':
            decrypted = MnemonicEncryption.decrypt(args.message, password)
            print(decrypted)
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == '__main__':
    main() 