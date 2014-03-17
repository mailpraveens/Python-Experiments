#Finds a largest increasing subsequence in O(n^2) time
#algorithm at http://www.algorithmist.com/index.php/Longest_Increasing_Subsequence
def LongestSubsequence(array):
  n=len(array)
  q=[0]*n
  prevHigh=[-1]*n # Contains all the previos elements to the increasing sequence
 
  for i in range(n):
    maxLen=0
    for j in range(i):
      if array[i]>array[j] :
        if q[j]>maxLen :
          maxLen=q[j]
          prevHigh[i]=j

    q[i]=maxLen+1
 
  idx=q.index(max(q))
  seq=[]
  while(idx!=-1):
    seq=[array[idx]]+seq
    idx=prevHigh[idx]
 
  return seq
 
def main():
  print(LongestSubsequence([4,2,6,1,9,0,11,7,12]))
 
 
if __name__=='__main__':
  main()