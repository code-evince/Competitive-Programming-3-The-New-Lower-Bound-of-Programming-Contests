test = int(input())
for _ in range (test):
    number = int(input())
    ans = abs(((((number*567)/9 + 7492)*235)/47 - 498))

    print(int((ans//10)%10))
