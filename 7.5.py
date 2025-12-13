N=int(input())
a=[]
for i in range(1,1000):
    if i**3<=N:
        a.append(i**3)
print(a)