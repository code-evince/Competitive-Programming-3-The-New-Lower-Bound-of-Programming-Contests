count=1
while(True):
    try:
        test = int(input())
        if(test==0):
            break
    except EOFError:
        break
    given,pending= 0,0
    party = list(map(int,input().split()))
    for x in party:
        if(x>0 and x<=99):
            given+=1

        else:
            pending+=1

    enum = given-pending
    print("Case {}: {}".format(count,enum))
    count+=1
