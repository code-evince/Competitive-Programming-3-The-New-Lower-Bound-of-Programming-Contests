while(True):
    try:
        a = list(map(int,input().split()))
    except EOFError:
        break
    if(a[0]==a[1]==a[2]==a[3]==0):
        continue;
    total = 1080
    total += (a[0]-a[1]-40)%40*9
    total += (a[2]-a[1]-40)%40*9
    total += (a[2]-a[3]-40)%40*9
    print(total)
# maybe, remember that % can be quite powerful in arithmetic
