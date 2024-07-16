import random
from math import gcd

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def mod_inverse(e, phi):
    x0, x1, y0, y1 = 1, 0, 0, 1
    a, b = phi, e
    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return y0 % phi

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.choice([i for i in range(2, phi) if gcd(i, phi) == 1])
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    return [pow(ord(char), key, n) for char in plaintext]

def decrypt(pk, ciphertext):
    key, n = pk
    return ''.join([chr(pow(char, key, n)) for char in ciphertext])

def main():
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))

    if not (is_prime(p) and is_prime(q)):
        print("Both numbers must be prime.")
        return

    public, private = generate_keypair(p, q)
    print(f"Public key: {public}")
    print(f"Private key: {private}")

    message = input("Enter a message to encrypt: ")
    encrypted_msg = encrypt(public, message)
    print(f"Encrypted message: {encrypted_msg}")

    decrypted_msg = decrypt(private, encrypted_msg)
    print(f"Decrypted message: {decrypted_msg}")

if __name__ == "__main__":
    main()
