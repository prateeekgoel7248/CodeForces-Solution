n=int(input())
l=input().split()
l=list(map(int,l))
chk=[False for i in range(31)]
for i in range(n):
    for j in range(31):
        if l[i] & (1<<j):
            chk[j]=True
ans=0
print(chk)
for i in range(31):
    if chk[i]:
        ans+=(1<<i)
print(ans)

'''
Examples : 

Input
4-No of test cases
3 - size of list
1 3 2 - element of the list
5
1 2 4 8 16
2
6 6
3
3 5 6
Output
3
31
6
7
'''
