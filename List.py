#List
#List is created by placing all elements inside square brackets.
marks = [100,67,89,45,76]
print(marks)

#Add 50 at position
#Syntax-list.insert(postion,element)
#list.insert()
marks.insert(2, 50)
print(marks)

#format specifier
#syntax='{}'.format()
marks1='{}'.format(marks)
print(marks1)

#Remove 45 element-POP Method
#syntax-list.remove()
marks.remove(45)
print(marks)

#Sort list in ascending order
#syntax-list.sort()
marks.sort()
print(marks)

#Finding position of ele 89
#syntax-list.index()
x=89
position=marks.index(x)
print(position)
