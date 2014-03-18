#method to check for anagrams within a set
from operator import itemgetter

def checkForAnagrams(input):
	temp = dict()
	#Sort the input values individually
	for k,v in input.items():
		temp[k]=''.join(sorted(v))
	#Now sort the entire list based on the value of the key
	temp2 = sorted(temp.items(),key = itemgetter(1))
	#Group the similar names together and return the list
	returnVal = []
	for x in temp2:
		returnVal.append(input[x[0]])
	return returnVal




def main():
	print(checkForAnagrams({1:"cat", 2:"dog", 3:"tac", 4:"god", 5:"act"}))


if __name__ == '__main__':
	main()