class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for _,num in enumerate(nums):
            if num in visited:
                return True
            visited.add(num)
        return False