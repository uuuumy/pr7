a=[]
s=0
for i in range(100,1000):
    if i%17==0:
        a.append(i)
        s+=1
    b=' '.join(map(str, a))
print(b,s)
