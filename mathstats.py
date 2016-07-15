import mincemeat
import sys

file = open(sys.argv[1])
data = list(file)
file.close()
datasource = dict(enumerate(data))

def mapfn(k, v):
    yield 'sum',int(v)

def reducefn(k, vs):
    count = len(vs)
    total = sum(vs)
    std_sum = 0
    mean = total/count
    for number in vs:
        std_sum = std_sum + (int(number)-mean)**2
    std = (std_sum/count)**0.5
    return count,total,std


s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print "count:", results.get('sum')[0]
print "sum: ",results.get('sum')[1]
print "Std.dev:", results.get('sum')[2]

