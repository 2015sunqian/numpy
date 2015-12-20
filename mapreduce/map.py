#!/usr/bin/python
import sys
for line in sys.stdin:
    try:
        flags = line[:-1].split('\t')

        stat_date=flags[0]
        version = flags[1]
        ip = flags[2]
        print stat_date,',',version,',',ip,'\t',1

    except Exception,e:
        pass
