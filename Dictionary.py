import json
from difflib import get_close_matches

data = json.load(open("C:\\Users\\dell\\Downloads\\data.json"))

def dict(word):
    word=word.lower()
    if word in data:
        return(data[word])
    elif word.title() in data:
        return(data[word.title()])
    elif word.upper() in data:
        return(data[word.upper()])
    elif len(get_close_matches(word, data.keys()))>0:
        print("Did you mean %s " %get_close_matches(word, data.keys())[0])
        d=input("Press y for yes and n for no : ")
        if d=="y":
            return (data[get_close_matches(word, data.keys())[0]])
        elif d=="n":
            return("Word you entered does not exit")
        else:
            return("You entered wrong input please press y or n")
    else:
        return("Word you entered does not exist")
    
string=input("Enter word which you want to know meaning : ")
ans = dict(string)

if type(ans)==list:
    for i in ans:
        print(i)
else:
    print(ans)
