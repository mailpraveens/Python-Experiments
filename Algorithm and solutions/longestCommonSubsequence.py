#Refer the algorithm and pseudo code at http://www.algorithmist.com/index.php/Longest_Common_Subsequence'


def lcs(x,y):
	n = len(x);
	m = len(y);
	table = dict()
	for i in range(n+1):
		for j in range(m+1):
			if i==0 or j==0:
				table[i,j] = 0;
			elif x[i-1]== y[j-1]:
				table[i,j] = table[i-1,j-1] + 1
			else:
				table[i,j] = max(table[i-1,j],table[i,j-1])



	def reconstructLCS(i,j):
		if i==0 or j==0:
			return []
		elif x[i-1] == y[j-1]:
			return reconstructLCS(i-1,j-1) + [x[i-1]]
		elif table[i-1,j] > table[i,j-1]:
			return reconstructLCS(i-1,j)
		else:
			return reconstructLCS(i,j-1)

	return reconstructLCS(n,m)

def main():
  print(lcs("AGGTAB","GXTXAYB"))
 
 
if __name__=='__main__':
  main()