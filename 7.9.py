N,K,R=map(int, input().split())
d=1
while N<R:
    N*=((K/100)+1)
    d+=1
print(d)