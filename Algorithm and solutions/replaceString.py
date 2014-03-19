def replacechar(w,index):
	if index == 0:
		return str(w):
	elif index > len(str(w)):
		return str(w)
	index = index-1;
	string = str(w)
   	val = string[:index] 
   	if index +1 < len(string):
	    val = val + string[index+1:]
   	return val
    
n = int(raw_input(""))

inputlist = []
inputnum = []
outputlist = []
for i in range(0,n):
	string = raw_input("");
	ab = string.split()
	inputlist.append(ab[1])
	inputnum.append(ab[0])

for key in range(0,n):
	outputlist.append(replacechar(inputlist[key],int(inputnum[key])))
    
for i in range(0,n):
    print str(i+1),
    print outputlist[i]