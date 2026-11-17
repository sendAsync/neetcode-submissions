class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result =[]
        path = []
        vis =[False]*n
        def dfs():
            if len(path) == n:
                result.append(list(path.copy()))
                return
            
            for i in range(0,n):
                if not vis[i]:
                    vis[i]=True
                    path.append(nums[i])
                    dfs()
                    path.pop()
                    vis[i]= False
        dfs()
        return result
                    

