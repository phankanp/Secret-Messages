from ciphers import Cipher
import string


class Keyword(Cipher):
    """Initializes Keyword cipher class"""

    def __init__(self):
        self.alphabet = list(string.ascii_uppercase)

    def encrypt(self, text, keyword):
        """Encrypts messages using the Keyword algorithm."""

        text = text.upper()
        encrypted_message = ""

        keyword_alphabet = self.create_kw_alphabet(keyword)

        encryption_key = dict(zip(self.alphabet, keyword_alphabet))

        for char in text:
            try:
                encrypted_message += encryption_key[char]
            except KeyError:
                encrypted_message += char
        return encrypted_message

    def decrypt(self, text, keyword):
        """Decrypts Keyword encrypted message"""

        text = text.upper()
        decrypted_message = ""

        keyword_alphabet = self.create_kw_alphabet(keyword)
        decryption_key = dict(zip(keyword_alphabet, self.alphabet))

        for char in text:
            try:
                decrypted_message += decryption_key[char]
            except KeyError:
                decrypted_message += char
        return decrypted_message

    def create_kw_alphabet(self, keyword):
        kw_alphabet = list(keyword)

        for char in self.alphabet:
            if char not in kw_alphabet:
                kw_alphabet.append(char)
        return kw_alphabet
