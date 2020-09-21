import json
from difflib import get_close_matches

data = json.load(open("data.json"))


print("WELCOME TO ZORAVARS OXFORD DICTIONARY")       

l="Y"

def search(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w , data.keys())) > 0 :
        print("did you mean %s instead" %get_close_matches(w, data.keys())[0])
        decide = input("press y for yes or n for no ::")
        if decide == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif decide == "n":
            return("Its a wrong Damn word")
        else:
            return("You have entered wrong input please enter just y or n")
    else:
        print("Word doesnt fucking exist bitch")


while(l=="y" or l=="Y"):
    w = input("enetr word to search : ")

    op = search(w)

    if type(op) == list:
        for i in op:
            print(i)
                
    else:
        print(op)

    l=input("Press Y for another word search else press N  :")    
    print("This Library is made by ILMAAN ZIA")


    












    

