#1. lambda function that multiplies arugument x with argument y

s=lambda x,y:x*y
print(s(10,20))



#2. fibonic series using lambdad

def fibonacci(count):
    lista=[0,1]
    list(map(lambda _:lista.append(sum(lista[-2:])),range(2,count)))
    return lista[:count]
print(fibonacci(8))


#3. mulitplying each number in list with given number

l=[1,2,3,4,5,6]
l1=list(map(lambda x:x*2,l))
print(l1)



#4 . finding number divisible by 9 from list using filter()

#without lambda
def isodd(x):
    if x%9==0:
        return True
    else:
        return False
l=[10,11,22,18,27,9,36,40,50]
l1=list(filter(isodd,l))
print(l1)

#with lambda
l=[10,15,18,27,36,45,50,60]
l1=list(filter(lambda x:x%9==0,l))
print(l1)




#5. finding even numbers from given list
'''without lambda'''

def iseven(x):
    if x%2==0:
        return True
    else :
        return False
l=[1,2,3,4,5,6,7,8,9]
l1=list(filter(iseven,l))
print(l1)


'''with lambda'''

l=[10,11,12,13,14,15]
l1=list(filter(lambda x:x%2==0,l))
print(l1)

