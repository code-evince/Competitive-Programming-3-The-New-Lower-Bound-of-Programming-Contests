while(True):
    test = int(input())
    if (test==0):
        break
    hx,hy = map(int,input().split())
    for i in range(test):
        a = list(map(int,input().split()))
        if(a[0]<hx and a[1]>hy):
            print('NO')
        elif(a[0]>hx and a[1]>hy):
            print("NE")
        elif(a[0]>hx and a[1]<hy):
            print("SE")
        elif(a[0]<hx and a[1]<hy):
            print("SO")
        else:
            print("divisa")

# boring
