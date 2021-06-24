
# creating file and writing text into it
with open("30 days 30 hours.txt","w") as f:
    f.write("i have completed 10 days successfully\n")
    print("process completed")




# opening file and adding text to it    
f = open("30 days 30 hours.txt","a")
f.write("gopal reddy\n")
print("adding completed")
f.close()





# opening file and reading content in the file
f = open("30 days 30 hours.txt","r")
data = f.read()
print(data)
