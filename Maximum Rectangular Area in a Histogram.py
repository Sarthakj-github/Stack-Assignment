#User function Template for python3


class Solution:
    
    #Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self,histogram):
        #code here
        n=len(histogram)
        rans=[n-1]*n
        lans=[-1]*n

        S=[]
        for i in range(n):
            while S!=[] and histogram[S[-1]]>histogram[i]:
                rans[S.pop()]=i-1
            S.append(i)
        S=[]
        for i in range(n-1,-1,-1):
            while S!=[] and histogram[S[-1]]>histogram[i]:
                lans[S.pop()]=i
            S.append(i)

        ans=[]
        for i in range(n):
            ans.append((rans[i]-lans[i])*histogram[i])
        return max(ans)
