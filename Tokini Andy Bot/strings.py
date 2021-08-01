#Import Strings so we can use it globally
#Import all the strings from Strings.json

import json

f = open('strings.json', encoding="utf8")
string = json.load(f)
f.close()

def getString(str):
    if not string[str]:
        return "Invalid String"
    else:
        return string[str]



