test = int(input())
for _ in range (test):
    total = int(input())
    shops = list(map(int,input().split()))
    shops.sort()
    min_dist = (shops[total-1] - shops[0] )*2
    print(min_dist)
