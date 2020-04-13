test = int(input())
for x in range(test):
    code = input()
    code_len = len(code)
    if(code=="78" or code=="1" or code=="4"):
        print("+")
    elif(code[code_len-2:]=="35"):
        print("-")
    elif(code[0]=="9" and code[code_len-1:]=="4"):
        print("*")
    elif(code[0:3]=="190"):
        print("?")
    else:
        print("?")
