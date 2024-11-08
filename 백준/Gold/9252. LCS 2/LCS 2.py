a,b=input(),input()
d,c=[""]*len(b),[""]*len(b)
for i in a:
 for j in range(len(b)-1,-1,-1):
  if i==b[j]:d[j]=c[j]+i
 m=""
 for j in range(len(b)):
  c[j]=m
  if len(m)<len(d[j]):m=d[j]
r=""
for i in d:
 if len(r)<len(i):r=i
print(len(r),r,sep="\n")