#import

#functions
def intersect(pointsarr,xarr,yarr,n,arrhigh):
    #variables
    i=0
    j=0
    m=0
    y=0
    k=0
    a=0
    #loops
    while(i<n):
        if i==(n-1):
            j=0
        else:
            j=i+1
    #code for -4,-2 and -4,2
        if pointsarr[i][0]==pointsarr[j][0] :
            if pointsarr[i][1]>pointsarr[j][1]:
                k=int((pointsarr[i][0]-(xarr[0]))//2)
                #if point 1 value is high
                #if point1 value is greater than arrhigh value than replace
                if arrhigh[k][1]=='0':
                       arrhigh[k][1]=pointsarr[i][1]
                elif arrhigh[k][1]<pointsarr[i][1]:
                       arrhigh[k][1]=pointsarr[i][1]
                #if points2 value is smaller than arrlow value than replace
                if arrhigh[k][2]=='0':
                       arrhigh[k][2]=pointsarr[j][1]
                elif arrhigh[k][2]>pointsarr[j][1]:
                       arrhigh[k][2]=pointsarr[j][1]
                k=0
            else:
                k=int((pointsarr[j][0]-(xarr[0]))//2)
                #if point2 value is high
                #if point2 value is greater than arrhigh value than replace
                if arrhigh[k][1]=='0':
                      arrhigh[k][1]=pointsarr[j][1]
                elif arrhigh[k][1]<pointsarr[j][1]:
                      arrhigh[k][1]=pointsarr[j][1]
                #if points1 value is smaller than arrlow value than replace
                if arrhigh[k][2]=='0':
                      arrhigh[k][2]=pointsarr[i][1]
                elif arrhigh[k][2]>pointsarr[i][1]:
                      arrhigh[k][2]=pointsarr[i][1]
                k=0 
        #code when value of x are not equal#tested
        else:
            #checking the difference betwween x1 and x2 to calculate number of x lines between them
            if pointsarr[i][0]<pointsarr[j][0]:
                    a=int((pointsarr[j][0]-pointsarr[i][0])//2)
                    lower=pointsarr[i][0]
            if pointsarr[i][0]>pointsarr[j][0]:
                    a=int((pointsarr[i][0]-pointsarr[j][0])//2)
                    lower=pointsarr[j][0]
            #adding values to arrlow and arrhigh
            while(m<=a):
                #value o intersection
                y=(((pointsarr[j][1]-pointsarr[i][1])*((lower+(2*m))-(pointsarr[i][0])))/(pointsarr[j][0]-pointsarr[i][0]))+pointsarr[i][1]#tested
                #getting the index value of xlin for arrhigh nad arr low
                k=int(((lower+(2*m))-xarr[0])//2)
                if arrhigh[k][1]=='0':
                    arrhigh[k][1]=y
                elif y>arrhigh[k][1]:
                    arrhigh[k][1]=y
                if arrhigh[k][2]=='0':
                    arrhigh[k][2]=y
                elif y<arrhigh[k][2]:
                    arrhigh[k][2]=y 
                m=m+1
                y=0
                k=0
            a=0
            m=0
            y=0
        i=i+1
    return arrhigh
#func2#tested
def calc(arrhigh):
    #variable
    f=0
    w1=0
    w2=0
    p=0
    s=0
    l2=len(arrhigh)
    #loops
    while(f<l2):
        w1=int(arrhigh[f][1]//1)
        w2=int((arrhigh[f][2])//1)
        if w1==w2:
            p=1
        else:
            if w1%2==0 and w2%2==0:
                p=int(((w1-w2)/2)+1)
            elif w1%2!=0 and w2%2!=0:
                p=int(((w1-w2)/2))
            else:
                p=int(((w1-w2)/2)+0.5)
        s=s+p
        p=0
        f=f+1
    return s
#input#tested
n=int(input())
i=0
arr=[0,0]
xarr=[0,0]
yarr=[0,0]
pointsarr=[]
while(i<n):
    get=input()
    l=len(get)
    j=0
    while(j<l):
        if get[j]==',':
            arr[0]=int(get[0:j])
            arr[1]=int(get[(j+1):l])
        j=j+1
    j=0
    if i==0:
        #initializing xarr
        xarr[0]=arr[0]
        xarr[1]=arr[0]
        #initializing yarr
        yarr[0]=arr[1]
        yarr[1]=arr[1]
    else:
        #adding the value of x if its is grater or smaller thAN previous value
        if arr[0]>xarr[1]:
            xarr[1]=arr[0]
        elif arr[0]<xarr[0]:
            xarr[0]=arr[0]
        #adding the value of y if its is grater or smaller thAN previous value
        if arr[1]>yarr[1]:
            yarr[1]=arr[1]
        elif arr[1]<yarr[0]:
            yarr[0]=arr[1]
    pointsarr.append(arr)
    arr=[0,0]
    i=i+1
i=0
#generating arrhigh and arrlow
t=xarr[0]
arrh=[]
narr=[0,0,0]
while(t<=(xarr[1])):
     narr[0]=t
     narr[1]='0'
     narr[2]='0'
     arrh.append(narr)
     narr=[0,0,0]
     t=t+2
t=0
narr=[0,0,0]
#output
result=intersect(pointsarr,xarr,yarr,n,arrh)
res=calc(result)
print(res)
