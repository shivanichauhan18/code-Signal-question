a=raw_input("enter your which you want to sort")
new=[]
for i in a:
    b=ord(i)
    new.append(b)
print new
j=0
while j<len(new):
    k=0
    while k<(len(new)-1):
        if new[k]>new[k+1]:
            new[k],new[k+1]=new[k+1],new[k]
        k=k+1
    j=j+1
print new
res=""
for s in new:
    res=res+(chr(s))
print res
