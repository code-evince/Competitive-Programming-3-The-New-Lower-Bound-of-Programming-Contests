numbers = int(input())
for i in range (numbers):
    take = input()
    store = list(take)
    if((store[0]=='o' and store[1]=='n')  or (store[0]=='o' and store[2]=='e') or (store[1]=='n' and store[2]=='e')):
        print(1)
    elif((store[0]=='t' and store[1]=='w')  or (store[0]=='t' and store[2]=='o') or (store[1]=='w' and store[2]=='o')):
        print(2)
    else:
        print(3)
