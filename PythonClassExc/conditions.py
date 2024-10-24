import random

x = 3
if x > 5:
    print("x is greater than 5")
elif x==5:
    print("x is equal to 5")
else:
    print("x is less than 5")

r=[random.randrange(1,10) for i in range(10)]
print(r)
name=[1,2,3,4,5]
reverse=name[::2]
print(reverse)