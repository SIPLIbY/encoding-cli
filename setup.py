from setuptools import setup, find_packages

setup(
    name="mnemonic-cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'cryptography>=41.0.0',
    ],
    entry_points={
        'console_scripts': [
            'mnemonic=mnemonic_cli:main',
        ],
    },
    author="xyz",
    description="A CLI tool for encrypting and decrypting mnemonic phrases",
    python_requires=">=3.7",
) 