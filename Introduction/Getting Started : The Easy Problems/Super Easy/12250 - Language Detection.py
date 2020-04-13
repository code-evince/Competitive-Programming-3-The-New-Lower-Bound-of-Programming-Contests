i=1
while(True):
    text = input()
    if(text == '#'):
        break
    language = {"HELLO":"ENGLISH","HOLA":"SPANISH","HALLO":"GERMAN","BONJOUR":"FRENCH","CIAO":"ITALIAN","ZDRAVSTVUJTE":"RUSSIAN"}
    if(text in language):
        print("Case {}: {}".format(i,language[text]))
        i+=1
    else:
        print("Case {}: UNKNOWN".format(i))
        i=i+1

