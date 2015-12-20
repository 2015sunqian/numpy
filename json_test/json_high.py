#json_high.py
import json
class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score
s = Student('Bob',20,90)
#print (json.dumps(s))
#给student写一个转换函数
def student2dict(std):
	return {
		'name':std.name,
		'age':std.age,
		'score':std.score
	}
print (json.dumps(s,default =student2dict))

def dict2student(d):
	return Student(d['name'],d['age'],d['score'])

json_str = '{"age":20,"score":88,"name":"Bob"}'
#print (json.loads(json_str,object_hook =dict2student))
dict1 =json.loads(json_str)
print dict1["age"]
print dict1["name"]
