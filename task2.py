mixed_list = [1, 1.23, "homework", False, 52, "Lizavetta"]
count = 0
for element in mixed_list:
    if type(element) == str:
        count += 1
print("Number of string elements:", count)