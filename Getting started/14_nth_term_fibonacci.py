nth=5
a=0
b=1
for i in range(2,nth):
    next = a+b
    a=b
    b=next

print(next)
    