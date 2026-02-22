# https://neetcode.io/problems/is-anagram/question?list=neetcode150

# Topic: HashSet
# Rating: Easy

# Time took to solve problem is: 5 mins.
# Solved in First try.
# AI used ? No

# first solution : 

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    
    if len(s) != len(t):
      return False
    
    hash_s = dict()
    hash_t = dict()
    
    for i in range(len(s)):

      if s[i] not in hash_s:
        hash_s[s[i]] = 1
      else: hash_s[s[i]]+=1

      if t[i] not in hash_t:
        hash_t[t[i]] = 1
      else: hash_t[t[i]]+=1

    for key in hash_s: 
      if ((key not in hash_t) or (hash_s[key] != hash_t[key])): 
        return False

    return True
  
# second using defaultdict

from collections import defaultdict

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    
    if len(s) != len(t):
      return False
    
    hash_s = defaultdict(int)
    hash_t = defaultdict(int)
    
    for i in range(len(s)):

      hash_s[s[i]] += 1
      hash_t[t[i]] += 1

    for key in hash_s: 
      if ((key not in hash_t) or (hash_s[key] != hash_t[key])): 
        return False

    return True