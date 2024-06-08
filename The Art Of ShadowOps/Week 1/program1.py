def encrypt(text, key):
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        elif 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
        else:
            result += ch
    return result

def decrypt(text, key):
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') - key + 26) % 26 + ord('a'))
        elif 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') - key + 26) % 26 + ord('A'))
        else:
            result += ch
    return result

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
    text = input("Enter the text: ")
    key = int(input("Enter the key: "))
    
    if choice == 'e':
        encrypted_text = encrypt(text, key)
        print("Encrypted text:", encrypted_text)
    elif choice == 'd':
        decrypted_text = decrypt(text, key)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
