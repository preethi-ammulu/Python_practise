#Dictionary
#Dictionaries are used to store data values in key.

#Priniting entire dictionary
emp={"sid":1,"sname":'Preethi',"mark":60}
print(emp)

#print only keys
#key method
print(emp.keys())

#print marks names
#value method
print(emp.values())

#adding new key course with python value
#update method
emp1={"course":'python'}
emp.update(emp1)
print(emp)

#To change the value for course
emp['course']='oracle'
print(emp)


