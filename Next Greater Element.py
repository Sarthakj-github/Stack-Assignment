#User function Template for python3


class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        S=[]
        ans=[-1]*n
        for i in range(n):
            while S!=[] and arr[S[-1]]<arr[i]:
                ans[S.pop()]=arr[i]
            S.append(i)
        return ans
