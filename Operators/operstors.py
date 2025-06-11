# Demonstration of different types of operators in Python

a = 10
b = 3

# Arithmetic Operators
print("Arithmetic Operators:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print("a // b =", a // b)

# Assignment Operators
print("\nAssignment Operators:")
c = a
print("c =", c)
c += b
print("c += b:", c)
c -= b
print("c -= b:", c)
c *= b
print("c *= b:", c)
c /= b
print("c /= b:", c)
c %= b
print("c %= b:", c)

# Comparison Operators
print("\nComparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Logical Operators
print("\nLogical Operators:")
print("a > 5 and b < 5:", a > 5 and b < 5)
print("a > 5 or b > 5:", a > 5 or b > 5)
print("not(a > 5):", not(a > 5))

# Bitwise Operators
print("\nBitwise Operators:")
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)

# Membership Operators
print("\nMembership Operators:")
list1 = [1, 2, 3, 10]
print("a in list1:", a in list1)
print("b not in list1:", b not in list1)

# Identity Operators
print("\nIdentity Operators:")
x = 5
y = 5
print("x is y:", x is y)
print("x is not y:", x is not y)