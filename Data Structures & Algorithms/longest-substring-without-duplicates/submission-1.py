class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longest=''
        li=[]
        for i in s:
            if i not in longest:
                longest+=i
            else:
                li.append(len(longest))
                idx=longest.index(i)
                longest=longest[idx+1:]+i
        if longest:
            li.append(len(longest))
        if li:

            return max(li)
        return 1


        