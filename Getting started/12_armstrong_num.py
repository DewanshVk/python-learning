num=370
temp=num
length=len(str(num))

check_amstg=0

while temp>0:
    digit = temp%10
    check_amstg += digit **length
    temp = temp//10

if(num == check_amstg):
    print(num,"is armstrong")
else:
    print(num,"is not armstrong")


