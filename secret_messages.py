from affine import Affine
from atbash import Atbash
from caesar import Caesar
from key_word import Keyword
import sys


ALL_CIPHERS = {"1": Affine, "2": Atbash, "3": Caesar, "4": Keyword}


def main():
    """
    1. Shows welcome message
    2. Gets users cipher choice, message, and keyword if necessary
    3. Determines whether to encrypt or decrypt the message
    4. Determines whether to continue or exit program
    """
    welcome_message()

    choice = "Yes"

    while choice.lower() == "yes":
        show_all_ciphers(ALL_CIPHERS)
        cipher_choice = get_user_cipher_choice()
        encrypt_or_decrypt = get_user_action_choice()

        if ALL_CIPHERS[cipher_choice] == Keyword:
            if encrypt_or_decrypt == "encrypt":
                message = get_user_message()
                keyword = get_user_keyword()
                keyword_cipher = Keyword()
                encrypted_message = keyword_cipher.encrypt(message, keyword)
                print("\nThe encrypted message: " + encrypted_message)
            else:
                message = get_user_message()
                keyword = get_user_keyword()
                keyword_cipher = Keyword()
                decrypted_message = keyword_cipher.decrypt(message, keyword)
                print("\nThe decrypted message: " + decrypted_message)
        else:
            if encrypt_or_decrypt == "encrypt":
                message = get_user_message()
                encrypted_message = encrypt_message(cipher_choice, message)
                print("\nThe encrypted message: " + encrypted_message)
            else:
                message = get_user_message()
                decrypted_message = decrypt_message(cipher_choice, message)
                print("\nThe decrypted message: " + decrypted_message)

        choice = input("\nWould you like to try again(Yes or No)? ")

    sys.exit()


def welcome_message():
    """Prints programs welcome message"""

    print("\nWelcome to the Cipher tool - Secret Messages Project")


def show_all_ciphers(ciphers):
    """Shows a list of all available ciphers"""

    print("\nAvailable Ciphers:\n")

    num = 1
    for k, v in ciphers.items():
        print(k + "." + v.__name__)
        num += 1
    print("\n")


def get_user_cipher_choice():
    """Gets cipher choice from the user"""

    cipher_choice = input("Please enter the number of the cipher you would like to use: ")

    try:
        choice = ALL_CIPHERS[cipher_choice]
    except KeyError:
        print("Invalid choice, please try again.\n")
        cipher_choice = get_user_cipher_choice()
    return cipher_choice


def get_user_action_choice():
    """Get user choice to encrypt or decrypt"""

    choice = input("Please enter '1' to encrypt or '2' to decrypt: ")

    if choice == "1":
        choice = "encrypt"
        return choice
    elif choice == "2":
        choice = "decrypt"
        return choice
    else:
        print("Invalid choice, please try again: ")
        choice = get_user_action_choice()
        return choice


def get_user_message():
    """Gets the message that user wants to encrypt or decrypt"""

    message = input("Please enter a message: ")

    return message


def get_user_keyword():
    """Gets user's keyword choice for the keyword cipher"""

    keyword = input("Please enter a keyword: ")
    keyword = keyword.upper()

    if len(keyword) > 10:
        print("Length Error. A keyword cannot be longer than 10 characters.")
        keyword = get_user_keyword()
    else:
        if not keyword.isalpha():
            print("Keyword must contain letters only, please try again.")
            keyword = get_user_keyword()

    char_seen = []
    for char in keyword:
        if char in char_seen:
            print("Keyword must contain unique letters, please try again.")
            keyword = get_user_keyword()
        char_seen.append(char)

    return keyword


def encrypt_message(cipher_choice, message):
    """Determines users choice of cipher
    Calls the encrypt method and returns the encrypted message
    """

    cipher = ALL_CIPHERS[cipher_choice]()

    encrypted_message = cipher.encrypt(message)

    return encrypted_message


def decrypt_message(cipher_choice, message):
    """Determines users choice of cipher
    Calls the decrypt method and returns the decrypted message
    """

    cipher = ALL_CIPHERS[cipher_choice]()

    decrypted_message = cipher.decrypt(message)

    return decrypted_message


if __name__ == '__main__':
    main()