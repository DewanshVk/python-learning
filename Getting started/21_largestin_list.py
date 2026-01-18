numbers=[12,23,34,45,12,23,67,89,54,65,12,23,89,12]
large_val=numbers[0]

for i in numbers:
    if i>large_val:
        large_val=i

print(large_val)