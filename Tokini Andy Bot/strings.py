#Import Strings so we can use it globally
#Import all the strings from Strings.json

import json

with open('strings.json', encoding="utf8") as f:
    string = json.load(f)

def getString(str):
    if not string[str]:
        return "Invalid String"
    else:
        return string[str]



