"""
This program encrypts a message using a Caesar Cipher.
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TO do-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):
    #TO DO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    """_summary_

    Args:
        text (str): Mensaje a cifrar
        shift (int): Numero de desplazamiento
    """
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

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TO DO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

encrypt(text, shift)