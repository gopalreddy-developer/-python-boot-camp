# 1.creating a function and retuing calc
def calc(x,y):
    add = x+y
    sub = x-y
    mul = x*y
    div = x/y
    
    print("the sum is",add)
    print("the diference is:",sub)
    print("the multiplication is",mul)
    print("the division is ",div)
x = int(input("enter first value"))
y = int(input("enter second value"))
calc(x,y)
        

#2. using function covid()

def covid(name,temp):

    print("name of patient is",name)
    if temp =="":
        print("body temp is 98 ")
    else:
        print("body temp is",temp)


name = input("enter name")
temp = input("enter body temp")
covid(name,temp)
