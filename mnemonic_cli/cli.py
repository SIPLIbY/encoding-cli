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

    # Encode file command
    encode_file_parser = subparsers.add_parser('encode-file', help='Encrypt a text file')
    encode_file_parser.add_argument('-i', '--input', required=True, help='Input file path')
    encode_file_parser.add_argument('-o', '--output', required=False, help='Output file path (optional)')

    # Decode file command
    decode_file_parser = subparsers.add_parser('decode-file', help='Decrypt an encrypted file')
    decode_file_parser.add_argument('-i', '--input', required=True, help='Input encrypted file path')
    decode_file_parser.add_argument('-o', '--output', required=False, help='Output file path (optional)')

    args = parser.parse_args()

    try:
        password = getpass('Enter password: ')
        if args.command == 'encode':
            encrypted = MnemonicEncryption.encrypt(args.mnemonic, password)
            print(encrypted)
        elif args.command == 'decode':
            decrypted = MnemonicEncryption.decrypt(args.message, password)
            print(decrypted)
        elif args.command == 'encode-file':
            with open(args.input, 'r') as f:
                content = f.read()
            encrypted = MnemonicEncryption.encrypt(content, password)
            if args.output:
                with open(args.output, 'w') as f:
                    f.write(encrypted)
                print(f"File encrypted successfully. Output saved to: {args.output}")
            else:
                print(encrypted)
        elif args.command == 'decode-file':
            with open(args.input, 'r') as f:
                encrypted_content = f.read()
            decrypted = MnemonicEncryption.decrypt(encrypted_content, password)
            if args.output:
                with open(args.output, 'w') as f:
                    f.write(decrypted)
                print(f"File decrypted successfully. Output saved to: {args.output}")
            else:
                print(decrypted)
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == '__main__':
    main() 