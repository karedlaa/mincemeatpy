#!/usr/bin/env python
import mincemeat
import sys

hashcode = sys.argv[1]
data = [(hashcode,1),(hashcode,2),(hashcode,3),(hashcode,4)]
datasource = dict(enumerate(data))


def mapfn(k, v):
    import itertools
    ele = "abcdefghijklmnopqrstuvwxyz1234567890"
    for i in itertools.product(ele,repeat=v[1]):
        yield v[0], ''.join(i)

def reducefn(k, vs):
    import hashlib
    pas = []
    for i in vs:
        hash1 = hashlib.md5(i).hexdigest()[:5]
        if(k == hash1):
            pas.append(i)
    res = dict()
    res["found"] = pas
    return res

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn


results = s.run_server(password="changeme")
print "Attacking",hashcode
print results[hashcode]