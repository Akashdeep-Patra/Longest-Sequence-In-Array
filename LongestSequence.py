def longestSequence(a):
  mem=dict()
  visited=set()
  ans=[]
  for i,j in enumerate(a):
    mem[j]=i
  max_length=0
  for key in mem.keys():
    if key in visited:
      continue
    value=key
    length=0
    collector1=[]
    while(value in mem):
      collector1.append(value)
      length+=1
      value+=1
      visited.add(value)
    value=key-1
    collector2=[]
    while(value in mem):
      collector2.append(value)
      value-=1
      length+=1
      visited.add(value)
    if(length>max_length):
      max_length=length
      collector2.reverse()
      ans=collector2+collector1
  return ans

