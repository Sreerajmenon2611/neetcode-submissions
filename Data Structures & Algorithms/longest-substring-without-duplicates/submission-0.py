class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        mp={}
        for i in s:
            mp[i]=0
        curr_len=1
        max_len=-float('inf')
        while r<len(s):
            if mp[s[r]]==0:
                mp[s[r]]=1
                curr_len+=1
            else:
                max_len=max(max_len,curr_len)
                while s[r]!=s[l]:
                    mp[s[l]]-=1
                    l+=1
                    curr_len-=1
                l+=1
            r+=1
        max_len=max(max_len,curr_len)
        return max_len-1


        