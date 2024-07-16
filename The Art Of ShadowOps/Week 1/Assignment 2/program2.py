def extended_gcd(a,b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b,a % b)
    x = y1
    y = x1 - (a//b) * y1
    return gcd, x, y

def solve_diophantine(A, B, C, D):
    gcd_ab, x1, y1 = extended_gcd(A,B)
    gcd_abc, x2, y2 = extended_gcd(gcd_ab, C)
    if D % gcd_abc != 0:
        return None
    x2 *= D//gcd_abc
    y2 *= D//gcd_abc
    a = x1 * x2
    b = y1 * x2
    c = y2
    return a, b, C

def main():
    try:
        A = int(input("Enter value of A: "))
        B = int(input("Enter value of B: "))
        C = int(input("Enter value of C: "))
        D = int(input("Enter value of D: "))
        result = solve_diophantine(A,B,C,D)
        if result:
            a, b, c = result
            print(f"The solution is: a = {a}, b = {b}, c = {c}")
        else:
            print("No solution exists")
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
    