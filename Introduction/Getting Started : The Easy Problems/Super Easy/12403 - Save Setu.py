amount=0
test = int(input())
for x in range (test):
    store = list(map(str,input().split()))
    if(len(store)==2):
        add = int(store[1])
        amount+=add
    if(len(store)==1):
        print(amount)
