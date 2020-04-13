i=1
while(True):
    try:
        intake = input()
        if(intake == "*"):
            break
    except EOFError:
        break
    if(intake == "Hajj"):
        print("Case {}: Hajj-e-Akbar".format(i))
        i+=1
    if(intake == "Umrah"):
        print("Case {}: Hajj-e-Asghar".format(i))
        i+=1
                 
