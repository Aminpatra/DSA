n = int(input())
divisors = []
i = 1

while i * i <= n:
  if (n % i == 0):
    divisors.append(i)
    if (n // i != i):
      divisors.append(n//i)
  i += 1

print(*divisors)