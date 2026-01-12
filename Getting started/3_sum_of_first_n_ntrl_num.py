num=int(input("Enter a number:"))
sum=0
l=[]
for i in range(1,num+1):
    l.append(i)
    sum+=i
print(f"Where first {num} number is",l)
print(f"Sum of numbers =",sum)
