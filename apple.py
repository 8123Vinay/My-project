#Apple and Oranges

#Position of the house
st=list(map(int, input().split()))
s=(st[0])
t=(st[1])


#location of trees

ab=list(map(int, input().split()))
apl=(ab[0])
orl=(ab[1])

# number of apples and oranges
mn=list(map(int, input().split()))
apples=(mn[0])
oranges=(mn[1])

# distance of apples from the trees
dap=list(map(int, input().split()))
#distance of orange from trees

dor=list(map(int, input().split()))

num=[0,0]

for i in range(oranges):
    if (s<=dor[i]+orl<=t):
        num[1]=num[1]+1



for j in range(apples):
   if(s<=apl+dap[j]<=t):
     num[0]=num[0]+1

for i in num:
    print(i)

     

