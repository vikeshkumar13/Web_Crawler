list1 = [1,2,3,4,5,6,7,8]
list2 = [1,2,3]

for i in list1:
    if len(list1) != len(list2):
        break
print('list1 and list2 not equal')

temp1 = len(list1)
temp2 = len(list2)

print('temp1:', temp1)
print('temp2:', temp2)