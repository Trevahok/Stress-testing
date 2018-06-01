from ast import literal_eval
import sys
from matplotlib import pyplot as plt 
hometime=[]
fname=sys.argv[1]
f=open(fname, 'r')
data=list(map(lambda z:z.split('\n')[1:-1],f.read().split('#')))
for node in data:
    for record in node:
        if 'Could' not in record:
            x=literal_eval(record)[list(literal_eval(record).keys())[0]]['writing code test time']
            hometime.append(x)
count_dict={}
for time in hometime:
    count_dict[int(time*10)]=0

for time in hometime:
    count_dict[int(time*10)]+=1
    
plt.scatter(range(len(hometime)),hometime)
x=list(count_dict.keys())
plt.xticks(x)
plt.bar(x,height=list(count_dict.values()))
plt.title(fname)
print(hometime)
plt.xlabel('time => 1 unit = 0.1 secs') 
plt.savefig(fname)
plt.show()
