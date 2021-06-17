#1. merging two dictionaries we have to use update()
dict1 = {"a":1,"b":2,"c":3}
dict2 = {"d":4,"e":5,"f":6}

dict1.update(dict2)
print(dict1)




#2. removing key from dictionary 
d={100:"gopal",101:"gopi",102:"vinod"}
print(d.popitem())
print(d)





#3. maping two ists we have to use dict(zip())

keys = ["gopal","gopi","vinod"]
values = [100,200,300]
d=dict(zip(keys,values))
print(d)



#4.finding length of the set we have to use len()
s={10,20,30,40}
print(s)
print(len(s))




#5. intersection of two sets it returns onlycommon values from two sets
s1 = {10,20,30,40}
s2 = {30,40,50,60}
print(s1.intersection(s2))
