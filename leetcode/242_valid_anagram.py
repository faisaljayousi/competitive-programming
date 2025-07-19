class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap_s, hashmap_t = {}, {}

        for i in range(len(s)):
            hashmap_s[s[i]] = hashmap_s.get(s[i], 0) + 1
            hashmap_t[t[i]] = hashmap_t.get(t[i], 0) + 1

        return hashmap_s == hashmap_t
