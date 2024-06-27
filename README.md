# Affine_Cipher_Tool
This repository contains a Python-based web application for encrypting and decrypting text using the Affine Cipher, one of the classical encryption techniques. Built with Flask, this application provides a simple and interactive interface to apply the Affine Cipher on any input text with customizable keys.

# Features 
Encryption and Decryption: 
Implements the Affine Cipher to encrypt and decrypt text using two keys, ensuring that the first key is coprime with 26 to have a modular inverse.
Error Handling: 
Provides error feedback when the first key is not coprime with 26, which is essential for the Affine Cipher to function properly.
Web Interface:
A user-friendly web interface that allows users to easily input text, keys, and choose to encrypt or decrypt.
Interactive Results: 
Immediate display of encrypted or decrypted results based on user input.

# Technical Details
# Affine Cipher Algorithm: 
The encryption is performed using the formula (a * x + b) % 26, where x is the position of the letter in the alphabet, and a and b are the keys provided by the user. Decryption uses the formula (a_inv * (y - b)) % 26, where a_inv is the modular inverse of a.
# Modular Arithmetic: 
Includes a utility to calculate the greatest common divisor and the modular inverse, essential for the cipher's decryption process.
# Flask Application:
Utilizes Flask to handle HTTP requests, rendering templates for the user interface, and managing form data for encryption and decryption operations.

CREATED BY MUHAMMAD HANIF MURTAZA AND YANG ZIXUN
