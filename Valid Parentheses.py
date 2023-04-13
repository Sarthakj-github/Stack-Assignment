class Solution:
    def isValid(self, s: str) -> bool:
        d={'(':')','[':']','{':'}'}

        L=[]

        for i in s:
            if i in d:
                L.append(i)
            elif L!=[] and d[L[-1]]==i:
                L.pop()
            else:
                return False

        if L!=[]:
            return False

        return True
