alphabet = {
    "4":"a",
    "8":"b",
    "c":"c",
    "6":"d",
    "3":"e",
    "7":"f",
    "6":"g",
    "4":"h",
    "1":"i",
    "1":"j",
    "k":"k",
    "1":"l",
    "m":"m",
    "n":"n",
    "0":"o",
    "9":"p",
    "4":"r",
    "5":"s",
    "1":"t",
    "u":"u",
    "v":"v",
    "y":"y",
    "z":"z",
   " ": " "
}

overlap = ["a","e","i","o","u"]
sessiz = ["b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "p", "r", "s", "t", "v", "y", "z"]

text = str(input("Text:"))
text2 = ""
index = 0



for i in text:
    i = i.lower()
    if i in alphabet:
        pass
    else:
        text2 += i
    
    index += 1


print(text2)