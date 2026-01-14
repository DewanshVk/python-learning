num=12
a=0
b=1
print(a)
print(b)
for i in range(2,num):
    next = a+b
    a=b
    b=next
    print(next)

    