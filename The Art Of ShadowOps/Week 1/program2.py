def encrypt(key, input_file, output_file):
    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            while True:
                ch = infile.read(1)
                if not ch:
                    break
                if 'a' <= ch <= 'z':
                    ch = chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
                elif 'A' <= ch <= 'Z':
                    ch = chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
                outfile.write(ch)
        print("Encryption complete.")
    except FileNotFoundError:
        print("File not found.")

def decrypt(key, input_file, output_file):
    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            while True:
                ch = infile.read(1)
                if not ch:
                    break
                if 'a' <= ch <= 'z':
                    ch = chr((ord(ch) - ord('a') - key + 26) % 26 + ord('a'))
                elif 'A' <= ch <= 'Z':
                    ch = chr((ord(ch) - ord('A') - key + 26) % 26 + ord('A'))
                outfile.write(ch)
        print("Decryption complete.")
    except FileNotFoundError:
        print("File not found.")

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
    key = int(input("Enter the key: "))
    
    if choice == 'e':
        input_file = "plaintext.txt"
        output_file = "encrypted.txt"
        encrypt(key, input_file, output_file)
    elif choice == 'd':
        input_file = "encrypted.txt"
        output_file = "decrypted.txt"
        decrypt(key, input_file, output_file)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()