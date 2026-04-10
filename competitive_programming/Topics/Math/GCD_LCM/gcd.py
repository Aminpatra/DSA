
## A program that gets the greatest common divisor AKA HCF (Highest Common Factor):
# a, b = map(int,input().split())
# res = min(a,b)
# while (res):
#   if (a % res == 0 and b % res == 0):
#     print(res)
#     break
#   res -=1


## Using Euclidean Algorithm:
# def gcd(a, b):
#   if a == 0:
#     return b
#   if b == 0:
#     return a
#   if a == b:
#     return a
#   if (a > b):
#     return gcd(a - b, b)

#   return gcd(a, b - a)

# print(gcd(6, 9))