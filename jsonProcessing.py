#JSON-> java script object notation ,all(" ") single quote not allowed
#better than Xml,,(ending tag headek)
import json

#loading json file from (text and json) file and loading using json.load(...)
with open('one.txt','r',encoding="utf-8") as type_txt:
	dataOne=json.load(type_txt)

print('json.load()->loading json to dictionary from json or txt file')
print(type(dataOne),type(dataOne[0]))
print(dataOne)


with open('one.json','r',encoding="utf-8") as type_json:
	dataTwo=json.load(type_json)
print('json.load()->loading json to dictionary from json or txt file')
print(type(dataTwo),type(dataTwo[0]))
print(dataTwo)

#load json from string
with open('jsonString.txt','r',encoding="utf-8") as f:
	type_str=str(f.read())
dataThree=json.loads(type_str)
print('json.loads()->loading string(json) to dictionary')
print(type(dataThree),type(dataThree[0]))
print(dataThree)


###################### dumping jaon to string

dataFour=json.dumps(dataThree,ensure_ascii=False) #preserve non ascii characters
print('json.dumps()->dumping dictinary to json')
print(type(dataFour),type(dataFour[0]))
print(dataFour)

########### dumping dictionary to json 
with open('two.txt','w',encoding="utf-8") as to_json_in_txt:
	json.dump(dataOne,to_json_in_txt,ensure_ascii=False)

with open('two.json','w',encoding="utf-8") as to_json_in_json:
	json.dump(dataOne,to_json_in_json,ensure_ascii=False)

"""
	json.load()->loading json to dictionary from json or txt file
	json.dump()->dumping dictionary to json to json or txt file

	json.loads()->loading string(json) to dictionary 
	json.dumps()->dumping dictinary to json
"""