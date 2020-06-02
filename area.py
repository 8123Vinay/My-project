A='abcdefghijklmnopqrstuvwxyz'
B=list(A)



h=list(map(int, input().rstrip().split()))


word = input()
C=[]
D=[]
for i in range(len(word)):
   C.append(A.index(word[i]))

for j in C:
  D.append(h[j])
print(len(word)*(max(D)))
  