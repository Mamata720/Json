import simplejson as json

a={"name":"Divid",
   "class":"I",
   "age":18
}

with open("json_object.json","w")as f:
    json.dump(a,f,indent=6)