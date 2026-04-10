
# LCM of two integers a and b 
# is the smallest positive integer that is divisible by both a and b.

## A program that finds the LCM between a and b
# a, b = map(int,input().split())
# mx = a if a>b else b

# while (True):
#   if (mx % a == 0 and mx % b == 0):
#     print(mx)
#     break
#   mx += 1


## Using GCD: (a * b) / gcd(a, b)
# a, b = map(int,input().split())
# mn = a if a < b else b

# while (mn):
#   if (a % mn == 0 and b % mn == 0):
#     break
#   mn -= 1

# print((a * b) // mn)