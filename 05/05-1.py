def serialize(ds):
    dtype = type(ds)
    
    if dtype is dict:
        d = "dictionaries|"
        for i in ds:	
            d = d + str(i)
            d = d + ":"
            d = d + str(ds[i])
            d = d + ","
            d = d + str(type(ds[i]))
            d = d + "|"
        return d[:-1]
        
   
    elif dtype is list:
        d = "list|"
        for i in ds:
            d = d + str(i)
            d = d + ","
            d = d + str(type(i))
            d = d + "|"
        return d[:-1]
        

def deserilize(i):
	list_of_str = i.split("|")
	dtype = list_of_str[0]
	list_of_str = list_of_str[1:]
	if dtype == 'dictionaries':
		d = dict()
		for i in list_of_str:
			a = i.split(":")
			keys = a[0]
			value = a[1]
			c = value.split(",")
			values = c[0]
			vtype = c[1]
			if vtype == "<class 'str'>":
				d[keys] = str(values)
			elif vtype == "<class 'int'>":
				d[keys] = int(values)
			else:
				d[keys] = float(values)
		return d
 
	elif dtype == 'list':
		d = list()
		for i in list_of_str:
			spl = i.split(",")
			values = spl[0]
			vtype = spl[1]
			if vtype == "<class 'str'>":
				d.append(str(values))
			elif vtype == "<class 'int'>":
				d.append(int(values))
			else: 
				d.append(float(values))
		return d


def my_compare(ds1, ds2):
	if type(ds1) is not type(ds2):
		return "Not Same Type"
	else: 
		if isinstance(ds1, list):
			if ds1 == ds2:
				return "Same"
			else:
				return "Incorrect"
		if isinstance(ds1, dict):
			if ds1 == ds2:
				return "Same"
			else:
				return "Incorrect"

"-------------------------------------------------------------------------------------------"

import json
 
path = input("Which json file do u want to open?")
fh = open(path)
data = json.load(fh)
fh.close()

s = serialize(data)

path2 = input("What is the new file name for the ds?")
fh2 = open(path2, 'w')
fh2.write(s)
fh2.close()

data2 = open(path2, 'r')
string = data2.read()
data2.close()

v_data= deserilize(string)

print(my_compare(v_data, data))
print(v_data)
print(data)


