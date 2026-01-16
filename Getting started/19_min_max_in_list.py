numbers=[12,23,34,45,67,89,54,65]

minimum=min(numbers)
maximum=max(numbers)
print(minimum,maximum)

min_val=numbers[0]
max_val=numbers[0]

for i in numbers:
    if i<min_val:
        min_val=i
    elif i>max_val:
        max_val=i

print(min_val,max_val)
    
