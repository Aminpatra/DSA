class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      if len(strs) == 0:
        return []
      hash_map = dict()
      for word in strs:
        arr = [0] * 26
        for letter in word:
          arr[ord(letter) - ord('a')] += 1
        if tuple(arr) not in hash_map:
          hash_map[tuple(arr)] = [word]
        else: 
          hash_map[tuple(arr)].append(word)
      return [*hash_map.values()]