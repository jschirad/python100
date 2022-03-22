"""
This program encrypts a message using a Caesar Cipher.
"""
from secrets import choice


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    """Encriptar

    Args:
        text (str): Mensaje a cifrar
        shift (int): Numero de desplazamiento
    """
    print ("The encoded text is:")
    for letter in text:
        if letter in alphabet:
            """Buscamos la letra en el alfabeto"""
            index = alphabet.index(letter)
            """Obtenemos el nuevo indice de la letra"""
            new_index = (index + shift) % 26
            new_letter = alphabet[new_index]
            print(new_letter, end='')
        else:
            print(letter, end='')

#TO DO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

def decrypt(text, shift):
    """Desencriptar 

    Args:
        text (str): Mensaje a decifrar
        shift (int): Numero de desplazamiento
    """
    print ("The decoded text is:")
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index - shift) % 26
            new_letter = alphabet[new_index]
            print(new_letter, end='')
        else:
            print(letter, end='')



#TO DO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
def choice_direction(direction):
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Please type 'encode' or 'decode'")

choice_direction(direction)