shopping_list={ 
            "chaco":15,
            "Biscuits":50,
            "Dairy_milk":30,
            "ice_cream":20,
        } 
show_shoping_list={}
quantity=int(input("how many things you want"))
j=0
sum=0
while j<quantity:
    userinput=input("what you wants to buy").lower()
    j=j+1
    for i in shopping_list:
        if userinput==i.lower():
            if j<=quantity:
                sum=sum+shopping_list[i]
                show_shoping_list[i]=shopping_list[i]
print(show_shoping_list)
