class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result =[]
        path = []
        def dfs(left, right):
            if left < right or left > n or right > n:
                return
            if left==n and right ==n:
                print()
                result.append("".join(path))
                return
            path.append("(")
            dfs(left+1,right)
            path.pop()
            path.append(")")
            dfs(left,right+1)
            path.pop()
        dfs(0,0)
        return result

        