#repeated string

string=str(input())


n=int(input())
l=len(string)

cou=int(n/l)

reminder=(n%l)

B=*(string.count('a'))



if reminder!=0:
 y=string[:reminder]

 s=y.count('a')       

if reminder==0:
  s=0

print(B+s)
