# https://codeforces.com/contest/363/problem/A
# Topic: implementation
# Rating: A: 800

# Time took to solve problem is: 5 min.
# Solved in First try.
# AI used ? NO

hash_map = {
  '0': 'O-|-OOOO',
  '1': 'O-|O-OOO',
  '2': 'O-|OO-OO',
  '3': 'O-|OOO-O',
  '4': 'O-|OOOO-',
  '5': '-O|-OOOO',
  '6': '-O|O-OOO',
  '7': '-O|OO-OO',
  '8': '-O|OOO-O',
  '9': '-O|OOOO-',
}

num = input()[::-1]
for n in num: 
  print(hash_map[n])