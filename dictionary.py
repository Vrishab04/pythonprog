'''employee={"name":"pragna","age":19,"company":"cisco","dob":"2005-01-23"}
print(employee)
del employee["age"]#del particular value or all
print(employee)


#creating a dictionary
#with dict()method
Dict=dict({1:"poorvi",2:"pragna",3:"sindhu"})
print(Dict)


#tuple converted to dict
Dict=dict([(12,"geetha"),(11,"mj")])
print(Dict)'''


dict1={1:'cisco',2:'tcs',3:'infosys',4:'accenture'}
pop_key=dict1.pop(2)
print(dict1)
'''emp={"name":"poo","age":19}
print("name:%s"%emp["name"])
print("age:%d"%emp["age"])



Dict[0]="poO"
Dict[1]="prag"
Dict[2]="SINDH"
print(Dict)

Dict['age']=20,23,42
print(Dict)'''



'''employee={"name":"pragna","age":19,"company":"cisco","dob":"2005-01-23"}
for x in employee:
    print(employee[x])'''





employee={"name":"pragna","age":19,"company":"cisco","dob":"2005-01-23"}
for x in employee.items():
    print(x)
print("---------")
dict1={1:'cisco',3:'tcs',4:'infosys',2:'accenture'}
print(len(dict1))
dict1={1:'cisco',3:'tcs',4:'infosys',2:'accenture'}
print(sorted(dict1))



dict1={1:'cisco',2:'tcs',3:'infosys',4:'accenture'}
print(dict1.keys())
print(dict1.items())
dict1.update({3:"mindtree"})
print(dict1)