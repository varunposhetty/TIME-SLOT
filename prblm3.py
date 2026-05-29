s=input().strip()
d={}
l=m=0
for r,c in enumerate(s):
    if c in d and d[c]>=l:l=d[c]+1
    d[c]=r
    m=max(m,r-l+1)
print(m)