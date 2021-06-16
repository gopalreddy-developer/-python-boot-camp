#to create a list of n integers using list comprehinsion
l=[s for s in range(10)]
print(l)
print(type(l))


#to add element to list
l.append(11)
print(l)


#to remove element from the above given list
print(l.pop())
print(l)

#to remove particular element from the above list
print(l.pop(2))
print(l)

# to show minimum value of above given t list
min1 = min(l)
print(min1)

#to show maximum value from the above given  list
max1 = max(l)
print(max1)


#creating aa tuple
t=(1,2,3,4,5,6)
print(t)
print(type(t))

#to print in reverse order of given tuple
print(t[::-1])


#to convert tuple  into list we have to use list()
t=(10,20,30,40,50)
print(t)
l=list(t)
print(l)
print(type(l))

#to convert list into tuple we hve to use tuple()
l=[100,200,300,400]
t=tuple(l)
print(t)
print(type(t))

# to sort the list(to write in ascending order)
l1 = [60,10,80,90,50,40]
l.sort()
print(l)

