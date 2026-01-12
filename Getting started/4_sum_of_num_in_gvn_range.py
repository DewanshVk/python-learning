num1=int(input("Enter a number to start:"))
num2=int(input("Enter a number to end with:"))
sum=0
for i in range(num1,num2+1):
    sum+=i
print(f"Sum of numbers =",sum)
