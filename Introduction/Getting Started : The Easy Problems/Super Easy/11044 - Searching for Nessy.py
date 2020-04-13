import math
test = int(input())
for _ in range(test):
    rows, cols = map(int,input().split())
    print(  (math.ceil((rows-2)/3))  *  (math.ceil((cols-2)/3))  )
    
# find patterns and the code becomes one-liner
