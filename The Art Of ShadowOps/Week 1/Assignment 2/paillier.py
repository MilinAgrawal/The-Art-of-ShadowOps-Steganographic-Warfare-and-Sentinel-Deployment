import random
from math import gcd

def lcm(x, y):
    return x * y // gcd(x, y)

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(p, q):
    n = p * q
    nsquare = n * n
    g = random.randint(1, nsquare)
    lambda_ = lcm(p - 1, q - 1)
    mu = mod_inverse((pow(g, lambda_, nsquare) - 1) // n, n)
    return ((g, n), (lambda_, mu))

def encrypt(pk, plaintext):
    g, n = pk
    r = random.randint(1, n - 1)
    nsquare = n * n
    ciphertext = (pow(g, plaintext, nsquare) * pow(r, n, nsquare)) % nsquare
    return ciphertext

def decrypt(pk, ciphertext):
    lambda_, mu = pk
    n = int(len(bin(ciphertext)[2:]) // 2)
    nsquare = n * n
    x = pow(ciphertext, lambda_, nsquare) - 1
    plaintext = ((x // n) * mu) % n
    return plaintext

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))

    if not (is_prime(p) and is_prime(q)):
        print("Both numbers must be prime.")
        return

    public, private = generate_keypair(p, q)
    print(f"Public key: {public}")
    print(f"Private key: {private}")

    message = int(input("Enter a number to encrypt: "))
    encrypted_msg = encrypt(public, message)
    print(f"Encrypted message: {encrypted_msg}")

    decrypted_msg = decrypt(private, encrypted_msg)
    print(f"Decrypted message: {decrypted_msg}")

if __name__ == "__main__":
    main()
