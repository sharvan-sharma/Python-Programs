#functions
def ncr(n,r):
  #variable
  i=0
  j=0
  N=1
  R=1
  value=0
  #loops
  while(i<r):
       N=N*(n-i)
       i=i+1
  while(j<r):
       R=R*(r-j)
       j=j+1
  value=int(N/R)
  return value
#func2
def total(arr):
    #variables
    s=1
    i=0
    #loops
    while(i<3):
        s=s*ncr(arr[i][0],arr[i][1])
        i=i+1
    return s
def func3(arr,qu1):
    #varaibales
    i=0
    j=0
    t=0
    store=[]
    dic={'A':1,'B':2,'C':3,'D':4,
         'E':5,'F':6,'G':7,'H':8,
         'I':9,'J':10,'K':11,'L':12,
         'M':13,'N':14,'O':15,'P':16,
         'Q':17,'R':18,'S':19,'T':20,
         'U':21,'V':22,'W':23,'X':24,
         'Y':25,'Z':26
          }
    #code
    while(i<3):
        while(j<3):
            t=t+arr[j][0]
            if dic[qu1[i]]<=t:
                store.append(j)
                break
            j=j+1
        t=0
        j=0
        i=i+1
    if store[0]!=store[1] and store[0]!=store[2] and store[1]!=store[2]:
        e1=ncr((arr[store[0]][0]-1),(arr[store[0]][1]-1))*ncr((arr[store[1]][0]-1),(arr[store[1]][1]-1))*ncr((arr[store[2]][0]-1),(arr[store[2]][1]))
        e2=ncr((arr[store[0]][0]-1),(arr[store[0]][1]-1))*ncr((arr[store[1]][0]-1),(arr[store[1]][1]-1))*ncr((arr[store[2]][0]-1),(arr[store[2]][1]-1))
        e3=(ncr((arr[store[0]][0]),(arr[store[0]][1]))*ncr((arr[store[1]][0]),(arr[store[1]][1]))*ncr((arr[store[2]][0]-1),(arr[store[2]][1]-1)))-e2
        e4=e1+e2+e3
        return e4
    elif store[0]==store[1] and store[0]!=store[2]:
        i=0
        rem=0
        while(i<3):
            if i==store[0] or i==store[2]:
              i=i+1
            else:
              rem=i
              break
        e1=ncr((arr[store[0]][0]-2),(arr[store[0]][1]-2))*ncr((arr[rem][0]),(arr[rem][1]))*ncr((arr[store[2]][0]-1),(arr[store[2]][1]))
        e2=ncr((arr[store[0]][0]-2),(arr[store[0]][1]-2))*ncr((arr[rem][0]),(arr[rem][1]))*ncr((arr[store[2]][0]-1),(arr[store[2]][1]-1))
        e3=(ncr((arr[store[0]][0]),(arr[store[0]][1]))*ncr((arr[rem][0]),(arr[rem][1]))*ncr((arr[store[2]][0]-1),(arr[store[2]][1]-1)))-e2
        e4=e1+e2+e3
        return e4
    elif store[0]!=store[1] :
        if store[0]==store[2]:
            i=0
            rem=0
            while(i<3):
               if i==store[0] or i==store[1]:
                  i=i+1
               else:
                  rem=i
                  break
            e1=ncr((arr[store[0]][0]-2),(arr[store[0]][1]-1))*ncr((arr[rem][0]),(arr[rem][1]))*ncr((arr[store[1]][0]-1),(arr[store[1]][1]-1))
            e2=ncr((arr[store[0]][0]-2),(arr[store[0]][1]-2))*ncr((arr[rem][0]),(arr[rem][1]))*ncr((arr[store[1]][0]-1),(arr[store[2]][1]-1))
            e3=(ncr((arr[store[0]][0]-1),(arr[store[0]][1]-1))*ncr((arr[rem][0]),(arr[rem][1]))*ncr((arr[store[1]][0]),(arr[store[1]][1])))-e2
            e4=e1+e2+e3
            return e4
        elif store[1]==store[2]:
            i=0
            rem=0
            while(i<3):
               if i==store[0] or i==store[1]:
                  i=i+1
               else:
                  rem=i
                  break
            e1=ncr((arr[store[1]][0]-2),(arr[store[1]][1]-1))*ncr((arr[rem][0]),(arr[rem][1]))*ncr((arr[store[0]][0]-1),(arr[store[0]][1]-1))
            e2=ncr((arr[store[1]][0]-2),(arr[store[1]][1]-2))*ncr((arr[rem][0]),(arr[rem][1]))*ncr((arr[store[0]][0]-1),(arr[store[0]][1]-1))
            e3=(ncr((arr[store[1]][0]-1),(arr[store[1]][1]-1))*ncr((arr[rem][0]),(arr[rem][1]))*ncr((arr[store[0]][0]),(arr[store[0]][1])))-e2
            e4=e1+e2+e3
            return e4
    elif store[0]==store[1] and store[0]==store[2]:
        i=0
        r=[]
        while(i<3):
            if i!=store[0]:
              r.append(i)
            i=i+1
        e1=ncr((arr[store[0]][0]-3),(arr[store[0]][1]-2))*ncr((arr[r[0]][0]),(arr[r[0]][1]))*ncr((arr[r[1]][0]),(arr[r[1]][1]))
        e2=ncr((arr[store[0]][0]-3),(arr[store[0]][1]-3))*ncr((arr[r[0]][0]),(arr[r[0]][1]))*ncr((arr[r[1]][0]),(arr[r[1]][1]))
        e3=(ncr((arr[r[1]][0]),(arr[r[1]][1]))*ncr((arr[r[0]][0]),(arr[r[0]][1]))*ncr((arr[store[2]][0]-1),(arr[store[2]][1]-1)))-e2
        e4=e1+e2+e3
        return e4
#input
i=0
k=[0,0]
arr=[]
while(i<3):
    k1=int(input())
    k2=int(input())
    k=[k1,k2]
    arr.append(k)
    i=i+1
i=0
while(i<2):
    if i==0:
      k3=input()
      qu1=k3.split(' ')
    else:
      k3=input()
      qu1.append(k3)
    i=i+1
#output
result1=total(arr)
print(result1)
result2=func3(arr,qu1)
res=(result1-result2)+1
print(res,end="")
