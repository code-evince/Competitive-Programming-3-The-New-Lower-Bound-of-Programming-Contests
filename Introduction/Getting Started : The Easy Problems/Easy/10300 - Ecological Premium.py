t = int(input())
for x in range(t):
    farmers = int(input())
    premium = 0
    for _ in range(farmers):
        farm, animal, val = map(int,input().split())
        premium += ((farm/animal)*val)*animal
    print(int(premium))
