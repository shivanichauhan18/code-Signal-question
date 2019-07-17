b=[[1,1,1,0],
    [0,5,0,1],
    [2,1,3,10]]
def matrixElementsSum(a):
    i=0
    count=0
    while i<len(a):
        j=0
        while j<len(a[i]):
            if i==0:
                if a[i][j]!=0:
                    count=count+a[i][j]
            elif i==1:
                if a[i][j]!=0 and a[i-1][j]!=0:
                    count=count+a[i][j]
            elif i==2:
                if a[i][j]!=0 and a[i-1][j]!=0 and a[i-2][j]!=0:
                    count=count+a[i][j]
            j=j+1
        i=i+1
    return count
print matrixElementsSum(b)