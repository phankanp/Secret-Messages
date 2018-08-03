Take a few of the famous ciphers listed here and implement them in Python so you can quickly encode and decode secret messages. Each cipher should be created as a Python class and each must expose two methods: encrypt and decrypt. Each of these methods should take a single string to be encoded or decoded and should return the properly encoded or decoded version of the string according to the cipher.

# Steps

- Choose at least three basic ciphers from the following list to implement encrypting and decrypting abilities.
  - Alberti cipher
  - Affine cipher
  - Atbash cipher
  - Polybius square cipher
  - Transposition cipher
  - ADFGVX cipher
  - Bifid cipher
  - Keyword cipher
  - Hill cipher
- Provide a command line menu providing an option to either encrypt or decrypt a value and then a sub menu with a list of implemented ciphers.
- Write a separate class, which inherits from cipher, and implements encrypt and decrypt functionality for each of your chosen ciphers.
- Prompt the user for input to encrypt or decrypt and, if applicable, any additional input settings required to perform the cipher process.
- The input value is correctly encrypted or decrypted using the chosen cipher and the output is displayed on the screen.
- Remember to include informative docstrings in your functions and/or methods.
- Make sure to follow the PEP 8 guidelines for coding style and write organized, easy to follow code. General code comments are great to add to your code too.
- Implement a one time pad to secure the cipher. A one time pad is an additional input step required prior to encrypting and decrypting a message. As long as both the sender and receiver use the same pad, the message itself becomes secure. Without the pad, the message cannot be recovered.
- Encrypted output is displayed in 5 character blocks, with padding added as required. For example if the message to encrypt is &quot;The quick brown fox.&quot; The output would be represented as something like &quot;LFDKA NMYML K1KZE &amp;XPQR&quot;.
