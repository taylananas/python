alphabet = {
    "a":"4",
    "b":"8",
    "c":"c",
    "d":"6",
    "e":"3",
    "f":"7",
    "g":"6",
    "h":"4",
    "i":"1",
    "j":"1",
    "k":"k",
    "l":"1",
    "m":"m",
    "n":"n",
    "o":"0",
    "p":"9",
    "r":"4",
    "s":"5",
    "t":"1",
    "u":"u",
    "v":"v",
    "y":"y",
    "z":"z",
    " ":" "
}


text = str(input("Text:"))
text2 = ""

for i in text:
    i = i.lower()
    if i in alphabet:
        text2 += alphabet[i]
    else:
        text2 += i
print(text2)