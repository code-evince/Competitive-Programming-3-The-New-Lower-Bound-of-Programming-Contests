check=0
while(True):
    try:
        x = input()
    except EOFError:
        break

    a=[]
    for i in x:
        if(i=='\"'):
            if(check%2==0):
                a.append('``')
                check=check+1
            else:
                a.append("''")
                check=check+1
        else:
            a.append(i)

    print("".join(a))


'''
OR USING FLAG
The EOFError is crucial for ensuring multiple testcases when no. of testcases
aren't given

check=0
while(True):
    try:
        x = input()
    except EOFError:
        break

    a=[]
    for i in x:
        if(i=='\"'):
            if(check==0):
                a.append('``')
                check=1
            else:
                a.append("''")
                check=0
        else:
            a.append(i)

    print("".join(a))

    '''
