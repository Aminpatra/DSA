# https://codeforces.com/contest/215/problem/B
# Topic: Pure Math
# Rating: 1300

# Time took to solve problem is: 30 min.
# Solved in First try.
# AI used ? "Yes" 'there is no way to solve it without knowing the formula' 

from math import sqrt
xi = sorted([*map(int,input().split())][1:])
yi = sorted([*map(int,input().split())][1:])
zi = sorted([*map(int,input().split())][1:])
A, B= map(int,input().split())
print(sqrt((B*(xi[-1]**2)*yi[-1]) / ((A * zi[0]) + (B * yi[-1]))))

# Lessons: 
# m_out = Volume × density = π(r₁² - r₂²)h × ρ₁
# m_in = Volume × density = πr₂²h × ρ₂