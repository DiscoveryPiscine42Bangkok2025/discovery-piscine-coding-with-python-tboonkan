array = [2,8,9,48,8,22,-12,2]
new_array = [x + 2 for x in array]
modify_array = [x for x in new_array if x > 5]
print(array)
print(modify_array)