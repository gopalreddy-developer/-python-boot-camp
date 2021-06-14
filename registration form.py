import tkinter.messagebox
from tkinter import *
from tkinter import messagebox

# creating window
root = Tk()


# creating size of window
root.geometry("600x400")

# creating colour of window
root.configure(background = "red")

# creating title for window
root.title("registration form")

label_0 = Label(root, text = "registration form", width = 15, font = ("bold", 20)).grid(row = 0, column =2)

# creating labels for window
label_1 = Label(root, text = "First Name", width = 10, font= ("bold", 10)).grid(row = 1, column =1 )
label_2 = Label(root, text = "Last Name", width = 10, font = ("bold", 10)).grid(row = 2, column= 1)
label_3 = Label(root, text = "Address", width = 10, font = ("bold", 10)).grid(row = 3, column = 1)
label_4 = Label(root, text = "Mandal", width = 10, font = ("bold", 10)).grid(row = 4, column = 1)
lable_5 = Label(root, text = "City", width = 10, font = ("bold", 10)).grid(row = 5, column = 1)
lable_6 = Label(root, text = "Postal code", width = 10, font = ("bold", 10)).grid(row = 6, column = 1)
lable_7 = Label(root, text = "gender", width = 10, font = ("bold", 10)).grid(row = 7, column = 1)
# variable var mentioned here integral value ,defalut value= 0
var = IntVar()
#these creats radio button
Radiobutton(root, text = "Male", padx = 5, variable = var, value= 1).grid(row = 7, column = 2)
Radiobutton(root, text = "Female", padx = 10, variable = var, value = 2).grid(row = 7, column = 3)

lable_8 = Label(root, text = "country", width = 10, font = ("bold", 10)).grid(row = 8, column = 1)

# these list contains contry names
list = ["india", "usa", "paksithan", "japan"]

# c contains stringvar defalt string=""
c =StringVar()
droplist = OptionMenu(root, c,*list)
droplist.config(width = 15)
c.set("select your country")
droplist.grid(row = 8, column = 2)


lable_9 = Label(root, text = "Programing language", width = 15, font = ("bold", 10)).grid(row = 9, column = 1)

var1 = IntVar()
Radiobutton(root, text = "python", padx = 5,variable = var1, value = 1).grid(row =9, column = 2 )
Radiobutton(root, text = "jawa", padx = 10, variable = var1, value = 2).grid(row = 9, column = 3)

# crtating entries
entry_0 =  Entry(root).grid(row = 1, column = 2)
entry_1 =  Entry(root).grid(row = 2, column = 2)
entry_2 =  Entry(root).grid(row = 3, column = 2)
entry_3 =  Entry(root).grid(row = 4, column = 2)
entry_4 =  Entry(root).grid(row = 5, column = 2)
entry_5 =  Entry(root).grid(row = 6, column = 2)


btn= Button(root, text = "submit", width = 10, font = ("bold", 10)).grid(row = 11, column = 0)


root.mainloop()

