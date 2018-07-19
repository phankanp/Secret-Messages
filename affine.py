from ciphers import Cipher
import string


class Affine(Cipher):
    """Initializes Affine cipher class"""

    def __init__(self):
        self.alphabet = string.ascii_uppercase
        self.letter_values = dict(zip(self.alphabet, range(len(self.alphabet))))
        self.number_values = dict(zip(range(len(self.alphabet)), self.alphabet))
        self.a = 5
        self.b = 8
        self.coprime = 21

    def encrypt(self, text):
        """Encrypts messages using the Affine algorithm."""

        encrypted_message = ""

        for char in text:
            try:
                encrypted_message += self.number_values[((self.a * self.letter_values[char.upper()] + self.b) % 26)]
            except KeyError:
                encrypted_message += char
        return encrypted_message

    def decrypt(self, text):
        """Decrypts Affine encrypted message"""

        decrypted_message = ""

        for char in text:
            try:
                decrypted_message += self.number_values[self.coprime * (self.letter_values[char.upper()] - self.b) % 26]
            except KeyError:
                decrypted_message += char
        return decrypted_message
