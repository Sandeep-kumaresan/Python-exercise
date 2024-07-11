dic={0:"",1:"w",2:"e",3:{},4:[]}
print(dic)
cleaned={}
for key,value in dic.items():
    if value:
        cleaned[key]=value
print(cleaned)