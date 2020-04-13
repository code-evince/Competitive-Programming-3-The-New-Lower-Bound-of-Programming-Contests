n = int(input())
for i in range(n):
	a = list(map(int, input().split()))
	a.sort()
	print("Case {}: {}".format(i+1, a[1]))


#this was driven by ability to write c++ format
# test = int(input())
# for i in range (test):
#     one,two,three = map(int,input().split())
#     if((one>=two and one<=three) or (one<=two and one>=three)   ):
#         print("Case {}: {}".format(i+1,one))
#     elif((two>=one and two<=three) or (two<=one and two>=three) ):
#         print("Case {}: {}".format(i+1,two))
#     elif((three>=two and three<=one)  or  (three<=two and three>=one)):
#         print("Case {}: {}".format(i+1,three))
