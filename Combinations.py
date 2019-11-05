#combination of length m from given array of length l and all the elemnts of arrays are distinct
import sys
def inputfunction():
    i=0;
    print("enter the space seperated array of elements ")
    arr = list(map(str , input().rstrip().split()))
    if len(arr) == 0:
        print("please enter atleast single elment either write exit")
        arr = inputfunction()
    elif arr[i] == 'exit':
        sys.exit()
    return arr
def addxitocomb(x,arr):
    for i in range(0,len(arr)):
        arr[i].append(x)#[[e..],[.e..],[e...],[e..]] to [[x,e..],[x,e..],[x,e...],[x,e..]]
    return arr

def mycombination(arr , m):
    if m == 1:
        #converting[2,3,4,5] to [[2],[3],[4],[5]]
        for i in range(0,len(arr)):
            arr[i]=[arr[i]]
        return arr
    else:
        i=0 ; bigarr=[]
        while(i <= (len(arr)-m)):
             xi = arr[i]
             remarr = [arr[t] for t in range(i+1,len(arr))]
             #decreasing recursion by 1
             prefix = mycombination(remarr , m-1)
             prefix = addxitocomb(xi,prefix)
             for _ in prefix:
                 bigarr.append(_)
             i = i + 1
        return bigarr
             

def Allcombi(arr):
    for i in range(1,len(arr)+1):
        print("combination of length " + str(i))
        combarr = mycombination(arr,i)
        for j in combarr:
            print(j)

#code
arr = inputfunction()
Allcombi(arr)
