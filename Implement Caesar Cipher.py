def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    shift = shift % 26  # Ensure the shift value is within the range of 0-25

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += new_char
        else:
            result += char  # Non-alphabetic characters are added unchanged

    return result

def main():
    while True:
        mode = input("\nDo you want to encrypt or decrypt a message? (Enter 'encrypt' or 'decrypt', or 'exit' to quit): ").strip().lower()
        if mode not in ['encrypt', 'decrypt', 'exit']:
            print("Invalid input. Please enter 'encrypt', 'decrypt', or 'exit'.")
            continue

        if mode == 'exit':
            print("Exiting the program. Goodbye!")
            break

        message = input("Enter your message: ")
        while True:
            try:
                shift = int(input("Enter the shift value (integer): "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer for the shift value.")

        if mode == 'encrypt':
            encrypted_message = caesar_cipher(message, shift, mode)
            print(f"\nThe encrypted message is: {encrypted_message}\n")
        elif mode == 'decrypt':
            decrypted_message = caesar_cipher(message, shift, mode)
            print(f"\nThe decrypted message is: {decrypted_message}\n")

if __name__ == "__main__":
    main()
