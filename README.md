# Caesar Cipher

## Introduction

This project contains an implementation of the Caesar cipher algorithm in Python. The Caesar cipher is a simple substitution cipher in which each letter in the text is replaced by a letter that is shifted a fixed number of positions down the alphabet. For example, with a shift of 3, A would be replaced by D, B would become E, C would become F, and so on.

The goal of the project is to provide an easy-to-use implementation of the Caesar cipher that allows users to encrypt and decrypt any text using different shift values.

## Technologies

The project was implemented in Python (version 3.11) using standard libraries and the itertools module.

## Running the Project

To run the project, follow the steps below:

1.  Download the **caesar_cipher.py** and **test_caesar_cipher.py** files and place them in the same folder.
    
2.  Make sure you have Python 3.11 installed. If not, download and install it from the following link: https://www.python.org/downloads/
    
3.  You can open the files in an IDE such as PyCharm, which can be downloaded from: https://www.jetbrains.com/pycharm/download/#section=windows . Versions for macOS and Linux are also available.
    
4.  Run the tests by entering the following command in the terminal: pytest
    
5.  After the tests are complete, the terminal will display whether all tests passed or if errors occurred.
 

To encrypt and decrypt your own text create a new object of the **CaesarCipher** class.\
See below for an example of how to use the code:

```
from caesar_cipher import CaesarCipher
import string

#### Create a new object of the CaesarCipher class with the desired parameters
sentence = "Hello, World!"
shift = 4
characters = string.ascii_letters
cipher = CaesarCipher(sentence, shift, characters)

#### Encrypt the text
encrypted = cipher.encrypt()
print(encrypted)  # Result: "Lipps, asvph!"

#### Decrypt the text
decrypted = CaesarCipher(encrypted, shift, characters).decrypt()
print(decrypted)  # Result: "Hello, World!"
```
You can change the shift value and character set to encrypt different texts.
