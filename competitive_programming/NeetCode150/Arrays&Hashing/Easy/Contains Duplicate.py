# https://neetcode.io/problems/duplicate-integer/question?list=neetcode150

# Topic: HashSet
# Rating: Easy

# Time took to solve problem is: 2 mins.
# Solved in First try.
# AI used ? No


class Solution:
  def hasDuplicate(self, nums: List[int]) -> bool:
    hash_set = set()
    for num in nums: 
      if num in hash_set:
        return True
      else: 
        hash_set.add(num)
    return False