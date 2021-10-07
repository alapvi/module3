mylist=[10,2,3,56,7]

print(mylist)
swap = True
while swap:
    swap = False
    for index in range(len(mylist)-1):
        if mylist[index] > mylist[index + 1]:
            mylist[index], mylist[index + 1] = mylist[index + 1],mylist[index]
            swap = True
print(mylist)