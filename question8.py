import json 
list1=["neelam","programer",24,2400]
list2=["komal","trainer",24,20000]
list3=["anuradha","HR",25,40000]
list4=["Abhishek","manager","29","63000"]
key=["name","designation","age","salary"]
emp1={}
emp2={}
emp3={}
emp4={}
dict1={"emp1":emp1,"emp2":emp2,"emp3":emp3,"emp4":emp4}
for i in range(len(list1)):
    emp1.update({key[i]:list1[i]})
for j in range(len(list2)):
    emp2.update({key[j]:list2[j]})
for k in range(len(list3)):
    emp3.update({key[k]:list3[k]})
for l in range(len(list4)) :
    emp4.update({key[l]:list4[l]})
with open("mamta.json","w")as f:
    json.dump(dict1,f,indent=6)
# with open("mamta.json","r")as f:
#     data=json.load(f)
#     print(data)
