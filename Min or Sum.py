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
