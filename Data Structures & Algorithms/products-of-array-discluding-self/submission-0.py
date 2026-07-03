class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front=[0 for i in range(len(nums))]
        back=[0 for i in range(len(nums))]
        front[0]=1
        for i in range(1,len(nums)):
            front[i]=front[i-1]*nums[i-1]
        
        back[-1]=1
        for i in range(len(back)-2,-1,-1):
            back[i]=back[i+1]*nums[i+1]
        for i in range(len(nums)):
            nums[i]=front[i]*back[i]
        return nums
        

        