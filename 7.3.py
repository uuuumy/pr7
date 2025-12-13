import math
i=int(input())
while int(math.sqrt(i))**2!=int(i):
    i=int(input())
else:
    print('полный квадрат')