def reverse(S):
    
    #Add code here
    St=[]
    for s in S:
        St.append(s)
    S=''
    while St!=[]:
        S+=St.pop()
    return S
    
