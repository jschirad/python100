"""
This program encrypts a message using a Caesar Cipher.
"""
from secrets import choice


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TO do : Create ine sigle function call caesar_cipher(direction, text, shift)

def caesar_cipher(direction, text, shift):
    for letter in text:
        if letter in alphabet:
            """Buscamos la letra en el alfabeto"""
            index = alphabet.index(letter)
            """Obtenemos el nuevo indice de la letra"""
            if direction == "encode":
                new_index = (index + shift) % 26
            elif direction == "decode":
                new_index = (index - shift) % 26
            new_letter = alphabet[new_index]
            print(new_letter, end='')
        else:
            print(letter, end='')

caesar_cipher(direction, text, shift)