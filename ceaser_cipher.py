# Alphabet list with repetition for easy shifting
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(input_text, shift_value, mode):
    result_text = ""
    if mode == "decode":
        shift_value *= -1
    for character in input_text:
        if character in letters:
            original_position = letters.index(character)
            new_position = original_position + shift_value
            result_text += letters[new_position]
        else:
            result_text += character
    print(f"Here's the {mode}d result: {result_text}")

# Import and display the logo from ceaser_art
from ceaser_art import logo
print(logo)

should_continue = True
while should_continue:

    action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))

    # Adjust the shift to ensure it stays within the range of the alphabet
    shift_amount = shift_amount % 26

    caesar_cipher(input_text=message, shift_value=shift_amount, mode=action)

    continue_choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if continue_choice == "no":
        should_continue = False
        print("Goodbye")