class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        for num in nums:
            if num not in hashmap:
                hashmap.add(num)
            else:
                return True
        return False
