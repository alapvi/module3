mylist=[10,2,3,4,4,4,3,3,3,56,7]


print(mylist)
for index in range(len(mylist)//2):
    mylist[index], mylist[len(mylist)-index-1] = mylist[len(mylist)-index-1], mylist[index]
print(mylist)