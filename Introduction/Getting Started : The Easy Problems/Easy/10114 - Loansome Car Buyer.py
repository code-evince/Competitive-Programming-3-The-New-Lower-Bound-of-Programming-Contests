while(True):
    try:
        months,downpay,loan,depri = map(float,input().split())
        amount = loan + downpay
        if(months < 0):
            break
    except EOFError:
        break


    a=[0 for i in range(101)]
    while(depri):
        m,r = map(float,input().split())
        depri-=1
        for i in range(int(m),101):  #you can call this the magic line, if a rate is to be carried on this helps
            a[i]=r

    i=0
    currWorth = amount * (1-a[0])

    currLoan = loan
    monthlyPay = loan/months

    while(currLoan > currWorth):
        i+=1
        currLoan -= monthlyPay;
        currWorth= currWorth*(1-a[i])
    if(i==1):
        print("{} month".format(i))
    else:
        print("{} months".format(i))
