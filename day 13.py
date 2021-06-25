#1
import re
matcher = re.finditer("[a-zA-Z0-9]","GopalReddy123")
for match in matcher:
    print(match.start(),"...",match.group())
    
print("\n")

#2
matcher = re.finditer("ab","abaabaaabaaaab")
for match in matcher:
    print(match.start(),"...",match.end(),"...",match.group())
print()


#3
def end_num(string):
    text= re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False
print(end_num("abcdef"))
print(end_num("abcef3"))

print()


#4
results =re.finditer("([0-9]{1,3})","exercises number 1,12,13,and 345 are important")
print("number of lenth 1to3")
for n in results:
    print(n.group())
print("\n")

#5
matcher =re.finditer("[A-Z]","AbCDEfGH")
for match in matcher:
    print(match.start(),"...",match.group())
