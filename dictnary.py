#..dictnary mathode:-

bio = {
    "name": "alex",
    "pashon": "programer",
    "sub" : {
        "python": "first start",
        "c": "secandary",
        "c++": "running"
    }
}

print(bio) #all print
print(bio.keys()) # ('name','pashon','sub')
print(bio.values()) # (['alex',program {pythone:'first start','c':secondary,'c++':running}])
print(bio.items()) #([('name', 'alex'), ('pashon', 'programer'), ('sub', {'python': 'first start', 'c': 'secandary', 'c++': 'running'})])
print(bio.get("pashon")) #programer
bio.update({"name": "rocky"})
print(bio) # aname:rocky change then all same 
bio.update({"age": 21})
print(bio) # add 'age':21