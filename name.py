import simplejson as json

data={"mamta":18,"pooja":19,"dhunu":19}

with open("my_file.json","w") as f:
    json.dump(data,f,indent=6)