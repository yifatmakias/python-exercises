
id_list = []
id_str = str(input("Enter a 8 digit id: "))
for i in range(0, len(id_str)):
    id_list.insert(i, int(id_str[i]))
# step 1
for i in range(0, len(id_list)):
    if i % 2 == 0:
        id_list[i] = id_list[i] * 1
    else:
        id_list[i] = id_list[i] * 2
print(id_list)
# step 2
for i in range(0, len(id_list)):
    if id_list[i] > 9:
        id_list[i] = 1 + id_list[i] % 10
print(id_list)
# step 3
sum = 0
for i in range(0, len(id_list)):
        sum = sum + id_list[i]
print(sum)
# step 4
answer = 10 - (sum % 10)
print(answer)
