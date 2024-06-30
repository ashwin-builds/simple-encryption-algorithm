def encrypt(key, text):
    cipher_text = ""

    for char in text:
        ascii = ord(char)
        new_ascii = ascii + key
        new_char = str(chr(new_ascii))

        cipher_text = cipher_text + new_char

    return cipher_text


def decrypt(key, text):
    plain_text = ""

    for char in text:
        ascii = ord(char)
        new_ascii = ascii - key
        new_char = str(chr(new_ascii))
        plain_text = plain_text + new_char

    return plain_text


def start():
    key = int(input("Enter an integer as an encryption/decryption key: "))
    text = input("Enter the text you would like to encrypt/decrypt: ")
    return key, text


def run():
    while True:

        print("\n\n\n\n********************* Encryptor and Decrypter *********************\n\n")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit\n")
        try:
            choice = int(input("Choose an option: "))
        except:
            print("An error occurred, please try again")
            continue

        if choice == 3:
            break

        key, text = start()

        if choice == 1:
            text = encrypt(key, text)
        if choice == 2:
            text = decrypt(key, text)

        print("Your encrypted/decrypted message is: " + text)



run()
