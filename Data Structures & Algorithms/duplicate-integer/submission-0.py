class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for _,n in enumerate(nums):
            print(n)
            if n in s:
                return True
            s.add(n)
        return False