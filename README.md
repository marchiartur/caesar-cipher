# Caesar Cipher

The Caesar cipher is a simple encryption technique that shifts each letter in a message by a fixed number of positions down the alphabet. This package provides a Python implementation of the Caesar cipher for encrypting messages with a key.

## Installation

To install the package, run:

pip install ccipher

## Usage

To use the Caesar cipher to encrypt a message, import the `ccipher` module and call the `encrypt` function with the message and the key as arguments:

```python
from ccipher import encrypt

message = "hello world"
key = 3
encrypted_message = encrypt(message, key)
print(encrypted_message)
```

This will output the encrypted message "khoor zruog".

To decrypt a message that has been encrypted with the Caesar cipher, call the decrypt function with the encrypted message and the key as arguments:

```python
from ccipher import decrypt

encrypted_message = "khoor zruog"
key = 3
decrypted_message = decrypt(encrypted_message, key)
print(decrypted_message)
```

This will output the original message "hello world".

# Contributing
If you find a bug or have a feature request, please create an issue on the GitHub repository. Pull requests are also welcome!

# License
This package is licensed under the MIT license. See the LICENSE file for more information.

Of course, feel free to modify and customize the README file to better suit your package and its features.
