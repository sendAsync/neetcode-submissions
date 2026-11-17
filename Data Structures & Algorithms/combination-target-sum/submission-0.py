class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result =[]
        path= []
        
        def dfs(cur_sum, index):
            if cur_sum == target:
                result.append(list(path.copy()))
                return 
            for i in range(index,len(nums)):
                if nums[i]+cur_sum <= target:
                    path.append(nums[i])
                    dfs(cur_sum+nums[i],i)
                    path.pop()
        dfs(0,0)
        return result