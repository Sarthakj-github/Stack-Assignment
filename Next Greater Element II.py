class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[-1]*n

        S=[]
        for i in range(n):
            while S!=[] and nums[S[-1]]<nums[i]:
                ans[S.pop()]=nums[i]
            S.append(i)

        for i in range(n):
            while S!=[] and nums[S[-1]]<nums[i]:
                ans[S.pop()]=nums[i]
            S.append(i)
            
        return ans
