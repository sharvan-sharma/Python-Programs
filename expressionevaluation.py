def postfixfunction(exp):
    l=len(exp)
    number=['1','2','3','4','5','6','7','8','9','0','.']
    operator={'*':2,'/':2,'%':2,'+':1,'-':1}
    i=0;j=0
    res=''
    stack=['phi']
    while(i<l):#traversing every element of expression
        if exp[i] in number:#if exp[i] is an number or decimal(.)
            if i==(len(exp)-1):#if the last index is number
                j=j+1
                res=res+exp[((i-j)+1):i+1]+','#comma is added to seperate the numbers #add the earlier number exp[i-j:i] in res
                j=0#making j back to zero
            else:
                j=j+1
        elif exp[i]=='(':#if we encounter withleft bracket
            if j!=0:
                res=res+exp[i-j:i]+','#add the earlier number exp[i-j:i] in res
                j=0#making j back to zero
            stack.append(exp[i])#appending at the end of stack
        elif exp[i]==')':# where we encounter with right bracket
            if j!=0:
                res=res+exp[i-j:i]+','#add the earlier number
                j=0
            k=len(stack)-1#getting the last index of stack array
            while(k>=0):# run until the index 0
                if stack[k]!='(' and stack[k]!='phi':#if the last value in stack is a operator not a ( and 'phi'
                    res=res+stack[k]#add the operator to end of res
                    stack.pop(k)# removing the last element
                    k=k-1# reducing the k
                elif stack[k]=='phi':#if we reach 'phi' that means exp is invalid
                    return 'invalid expression'
                    break
                elif stack[k]=='(':# if we find the left bracket
                    stack.pop(k)
                    break
        elif exp[i] in list(operator.keys()):# if the exp[i] is in operator
            if j!=0:
                res=res+exp[i-j:i]+','#add the earlier number
                j=0
            m=len(stack)-1#getting the last index of stack array
            while(m>=0):
                if stack[m]=='(':#means if the last index store the left bracket 
                    stack.append(exp[i])
                    break
                elif stack[m]=='phi':#if the stack is already empty
                    stack.append(exp[i])
                    break
                elif operator[exp[i]]<=operator[stack[m]]:#if the last element is operator check the precedence order
                    res=res+stack[m]#if the stack last element is of lower precedence
                    stack.pop(m)#pop the stack
                    m=m-1#reduce the last counter
                elif operator[exp[i]]>operator[stack[m]]:# if the last element of higher precedence
                    stack.append(exp[i])#just add the exp[i]at the end
                    break
        i=i+1
    #flushing out the remaining stack
    i=0
    if len(stack)>1:
        i=len(stack)-1
        while(i>=1):
            res=res+stack[i]
            i=i-1
    return res      
#calculator function for calculation of the postfix expression
def calcpostfix_with_stacktrace(exp):
    l=len(exp)
    i=0;j=0
    number=['1','2','3','4','5','6','7','8','9','0','.']
    operator={'*':2,'/':2,'%':2,'+':1,'-':1}
    s=''
    stack=['phi']
    while(i<l):
        if exp[i] in number:
            j=j+1
        elif exp[i]==',':
            s=s+exp[i-j:i]
            stack.append(float(s))
            s=''
            j=0
            print(stack)
        elif exp[i] in list(operator.keys()):
            op2=stack[len(stack)-1]
            op1=stack[len(stack)-2]
            stack.pop(len(stack)-1)
            stack.pop(len(stack)-1)
            print(stack)#for showing stack trace
            if exp[i]=='*':
                stack.append(op1*op2)
            elif exp[i]=='+':
                stack.append(op1+op2)
            elif exp[i]=='-':
                stack.append(op1-op2)
            elif exp[i]=='%':
                stack.append(op1%op2)
            elif exp[i]=='/':
                stack.append(op1/op2)
            print(stack)
        i=i+1
    return stack[len(stack)-1]
#function without stack trace
def calcpostfix(exp):
    l=len(exp)
    i=0;j=0
    number=['1','2','3','4','5','6','7','8','9','0','.']
    operator={'*':2,'/':2,'%':2,'+':1,'-':1}
    s=''
    stack=['phi']
    while(i<l):
        if exp[i] in number:
            j=j+1
        elif exp[i]==',':
            s=s+exp[i-j:i]
            stack.append(float(s))       
            s=''
            j=0
        elif exp[i] in list(operator.keys()):
            op2=stack[len(stack)-1]
            op1=stack[len(stack)-2]
            stack.pop(len(stack)-1)
            stack.pop(len(stack)-1)
            if exp[i]=='*':
                stack.append(op1*op2)
            elif exp[i]=='+':
                stack.append(op1+op2)
            elif exp[i]=='-':
                stack.append(op1-op2)
            elif exp[i]=='%':
                stack.append(op1%op2)
            elif exp[i]=='/':
                stack.append(op1/op2)
        i=i+1
    return stack[len(stack)-1]
#input (Description: a string which include a mathematical expression basically a calculator input)
print('Enter the expression which include *,+,-,/,% operators,"(",")"  barackets or any real number')
exp=input()
#OUTPUT and fuction calling
postfixexp=postfixfunction(exp)
if postfixexp=='invalid expression':
    print("invalid expression")
else:
    print("Postfix expression : "+postfixexp)
    print("Do you want to print Stack trace: y/n")
    ans=input()
    if ans=='y' :
        res=calcpostfix_with_stacktrace(postfixexp)
        print("Answer : "+str(res))
    elif ans=='n':
        res=calcpostfix(postfixexp)
        print("Answer : "+str(res))
    else:
        print("invalid input")
