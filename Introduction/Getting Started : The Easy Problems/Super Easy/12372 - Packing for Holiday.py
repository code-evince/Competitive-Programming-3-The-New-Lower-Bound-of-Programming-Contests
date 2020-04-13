test = int(input())
count=1
for x in range (test):

    l,b,w = map(int,input().split())
    if(l<=20 and b<=20 and w<=20):
        print("Case {}: good".format(count))
        count+=1
    else:
        print("Case {}: bad".format(count))
        count+=1
