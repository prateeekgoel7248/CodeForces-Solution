a=input().split()
a=list(map(int,a))
n=len(a)
if a[n-2]>a[n-1]:
    print(-1)
elif a[n-1]>=0:
    print(n-2)
    for i in range(n-2):
        print(i+1," ",n-1," ",n)
else:
    b=a
    b=sorted(b)
    if a==b:
        print(0)
    else:
        print(-1)
        
'''
there can be more than one solution for this question and answer will be different because we dont have to minimize the operation so we can perform less than n operation

Example
inputCopy
3
5
5 -4 2 -1 2
3
4 3 2
3
-3 -2 -1
outputCopy
2
1 2 3
3 4 5
-1
0

'''
