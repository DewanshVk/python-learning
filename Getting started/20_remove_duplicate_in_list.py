numbers=[12,23,34,45,12,23,67,89,54,65,12,23,89,12]
unique_list=[]

for i in numbers:
    if i not in unique_list:
        unique_list.append(i)


print(unique_list)