import random

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def mod_inverse(a, p):
    return pow(a, p - 2, p)

def generate_keypair(p):
    if not is_prime(p):
        raise ValueError("The number must be prime.")
    
    g = random.randint(2, p - 1)
    x = random.randint(1, p - 2)
    y = pow(g, x, p)
    
    return ((g, y, p), x)

def encrypt(pk, plaintext):
    g, y, p = pk
    k = random.randint(1, p - 2)
    a = pow(g, k, p)
    b = (plaintext * pow(y, k, p)) % p
    return (a, b)

def decrypt(private_key, ciphertext, p):
    a, b = ciphertext
    x = private_key
    s = pow(a, x, p)
    plaintext = (b * mod_inverse(s, p)) % p
    return plaintext

def main():
    p = int(input("Enter a prime number (p): "))

    if not is_prime(p):
        print("Number must be prime.")
        return

    public, private = generate_keypair(p)
    print(f"Public key: {public}")
    print(f"Private key: {private}")

    message = int(input("Enter a number to encrypt: "))
    encrypted_msg = encrypt(public, message)
    print(f"Encrypted message: {encrypted_msg}")

    decrypted_msg = decrypt(private, encrypted_msg, p)
    print(f"Decrypted message: {decrypted_msg}")

if __name__ == "__main__":
    main()
