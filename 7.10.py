t1=0
u=0
while True:
    p=float(input())
    if p==0:
        break
    if p<t1:
        u+=1
    t1=p
print(u)

