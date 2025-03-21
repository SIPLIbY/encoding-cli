#!/usr/bin/env python3

import argparse
from getpass import getpass
from .core import SecretEncryption

def main():
    parser = argparse.ArgumentParser(description='Encrypt and decrypt secret phrases')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Encode command
    encode_parser = subparsers.add_parser('encode', help='Encrypt a secret phrase')
    encode_parser.add_argument('-m', '--message', required=False, help='Secret phrase to encrypt')

    # Decode command
    decode_parser = subparsers.add_parser('decode', help='Decrypt an encrypted secret')
    decode_parser.add_argument('-m', '--message', required=False, help='Secret message to decrypt')

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
        if args.command == 'encode':
            message = args.message if args.message else getpass('Enter your secret phrase: ')
            password = getpass('Enter password: ')
            encrypted = SecretEncryption.encrypt(message, password)
            print(encrypted)
        elif args.command == 'decode':
            message = args.message if args.message else getpass('Enter encrypted message: ')
            password = getpass('Enter password: ')
            decrypted = SecretEncryption.decrypt(message, password)
            print(decrypted)
        elif args.command == 'encode-file':
            with open(args.input, 'r') as f:
                content = f.read()
            password = getpass('Enter password: ')
            encrypted = SecretEncryption.encrypt(content, password)
            if args.output:
                with open(args.output, 'w') as f:
                    f.write(encrypted)
                print(f"File encrypted successfully. Output saved to: {args.output}")
            else:
                print(encrypted)
        elif args.command == 'decode-file':
            with open(args.input, 'r') as f:
                encrypted_content = f.read()
            password = getpass('Enter password: ')
            decrypted = SecretEncryption.decrypt(encrypted_content, password)
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