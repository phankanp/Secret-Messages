from ciphers import Cipher
import string


class Atbash(Cipher):
    """Initializes Atbash cipher class"""

    def __init__(self):
        self.alphabet = string.ascii_uppercase
        self.forward_alphabet = list(self.alphabet)
        self.backward_alphabet = self.forward_alphabet[::-1]
        self.key = dict(zip(self.forward_alphabet, self.backward_alphabet))

    def encrypt(self, text):
        """Encrypts messages using the Atbash algorithm."""

        text = text.upper()

        encrypted_message = ""

        for char in text:
            try:
                encrypted_message += self.key[char]
            except KeyError:
                encrypted_message += char
        return encrypted_message

    def decrypt(self, text):
        """Decrypts Atbash encrypted message"""

        text = text.upper()

        decrypted_message = ""

        for char in text:
            try:
                decrypted_message += self.key[char]
            except KeyError:
                decrypted_message += char
        return decrypted_message
