#json_test3.py
#!/usr/bin/env python
#coding=utf-8
import json
s = '[{"name":"鸟巢","point":{"lat":"39.990","lng":"116.397"},"desc":"奥运会主场 地"},{"name":"北大乒乓球馆","point":{"lat":"39.988","lng":"116.315"},"desc":"乒乓 球比赛场地"},{"name":"北京工人体育场","point": {"lat":"39.930","lng":"116.446"},"desc":"足球比赛场地"}]'

locations=json.loads(s)

print type(locations)

print str(len(locations))

for location in locations:
	print location["name"]
	print location["point"]["lat"]

'''运行结果：
<type 'list'>
3
鸟巢
39.990
北大乒乓球馆
39.988
北京工人体育场
39.930
'''
