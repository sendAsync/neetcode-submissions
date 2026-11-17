class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map ={}
        start =0
        ans =0
        for i,ch in enumerate(s):
            
            if ch in char_map:
                start = max(start, char_map[ch] + 1)
            ans = max(ans, i-start+1)
            char_map[ch]= i
        return ans

        