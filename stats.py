from ast import literal_eval
import sys
fname=sys.argv[1]
f=open(fname, 'r')
data=list(map(lambda z:z.split('\n')[1:-1],f.read().split('#')))
def get_time(test):
	timetaken=[]
	for node in data:
		for record in node:
			if 'Could' not in record:
				x=literal_eval(record)[list(literal_eval(record).keys())[0]][test]
				timetaken.append(x)
	return timetaken
def make_counted_dict(hometime):
    count_dict={}
    for time in hometime:
        count_dict[int(time*10)]=0
    
    for time in hometime:
        count_dict[int(time*10)]+=1
    return count_dict



count_dict=make_counted_dict(get_time('writing code test time'))
average=sum([ x*y for x,y in count_dict.items()])/ sum(count_dict.values())
mode=max(count_dict.keys(),key=lambda x: count_dict[x])
print('all times in 0.1 seconds multplier')
print('max time taken for code test compilation: '+str(max(count_dict.keys()))+'\n'+'min time taken for code test compilation: '+str(min(count_dict.keys()))+'\nmean time taken: '+str(average)+'\nmode time taken for code test compilation: '+str(mode))
