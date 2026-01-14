num = 1234 
reverse = 0
while num>0:
    remainder = num %10 # ye last digit nikal ke deta ha                 
    reverse =(reverse*10) + remainder 
    num = num // 10 # ye last digit hata deta ha
    
print(reverse)

