#!/usr/bin/python
import sys
res = {}
for line in sys.stdin:
    try:
        flags = line[:-1].split('\t')
       
        skey= flags[0]
        if res.has_key(skey) == False:
            res[skey]=0
        res[skey] += 1

    except Exception,e:
        pass
for key in res.keys():
    print key,'\t',res[key]
