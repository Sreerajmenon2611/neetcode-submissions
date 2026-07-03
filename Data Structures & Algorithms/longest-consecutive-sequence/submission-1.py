class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=list(set(nums))
        nums.sort()
        
        ans=[]
        curr=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                curr+=1
            else:
                ans.append(curr)
                curr=1
        ans.append(curr)
        return max(ans)
        