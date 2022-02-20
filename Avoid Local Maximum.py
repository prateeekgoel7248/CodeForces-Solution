t=int(input())
while t>0:
    t-=1
    count=0
    s=int(input())
    l=input().split()
    l=list(map(int,l))
    for i in range(1,len(l)-1):
        if l[i]>l[i-1] and l[i]>l[i+1]:
            if i+2<s and l[i+2]>l[i]:
                l[i+1]=l[i+2]
            else:
                l[i+1]=l[i]
            count+=1
    print(count)
    print(l)
    
'''
Example:

inputCopy
5-testcase
3-size
2 1 2-elements
4
1 2 3 1
5
1 2 1 2 1
9
1 2 1 3 2 3 1 2 1
9
2 1 3 1 3 1 3 1 3
outputCopy
0
2 1 2
1
1 3 3 1
1
1 2 2 2 1
2
1 2 3 3 2 3 3 2 1
2
2 1 3 3 3 1 1 1 3
'''
