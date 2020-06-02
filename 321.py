c= list(input().strip().split())

print(c)


if 1>2:




   # Complete the compareTriplets function below.
  def compareTriplets(a, b):

  if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
C= map(int,input().split())
D= map(int,input().split()

numA=0
numB=0
if(len(C)==3 and len(D)==3):
    for i in range(3):
        if(((int (C[i]))<(int (D[i]))) and ((int (D[i]))<100)):
            numB+=1
        elif(((int (C[i]))>(int (D[i]))) and ((int (C[i]))<100)):
            numA+=1
print(numA,numB)