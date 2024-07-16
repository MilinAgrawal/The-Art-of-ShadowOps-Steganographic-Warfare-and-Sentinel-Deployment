def gcd_on(a,b):
    gcd = 1
    for i in range(1, min(a,b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

def gcd_eulerian(a,b):
    while b != 0:
        a, b =b, a % b
    return a

def main():
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        gcd_on_result = gcd_on(a,b)
        gcd_eulerian_result = gcd_eulerian(a,b)
        print(f"GCD of {a} and {b} using O(N) approach: {gcd_on_result}")
        print(f"GCD of {a} and {b} using Eulerian approach: {gcd_eulerian_result}")
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()