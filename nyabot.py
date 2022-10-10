alphabet = {
    " ": " ~nyaa "
}



text = str(input("Text:"))
text2 = ""

for i in text:
    i = i.lower()
    if i in alphabet:
        text2 += alphabet[i]
    else:
        text2 += i

text2 += " ~nyaa "
print(text2)