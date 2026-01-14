num = 121 
temp = num
reverse = 0

while num>0:
    remainder = num %10                 
    reverse =(reverse*10) + remainder 
    num = num // 10 
    
if reverse == temp:
    print("Palindrome")
else:
    print("Not a Palindrome")


