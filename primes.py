#!/usr/bin/env python
import mincemeat

data = [range(k,k+2000) for k in xrange(2,10000000, 2000)]
print len(data)
datasource = dict(enumerate(data))

def mapfn(k, v):
    for num in v:
        m=num
        a=0
        while(m!=0):
            a = m%10+a*10
            m = m/10
        if(num==a):
            yield "Number",num

def reducefn(k, vs):
    primes=[]
    for num in vs:
        flag=1
        for j in range(2,int((num)**0.5+1)):
            if (num % j) == 0:
                flag=0
                break
        if flag:
            print num
            primes.append(num)
    return primes
    
s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results
print "Length : ", len(results["Number"])
print "Sum : ", sum(results["Number"])
