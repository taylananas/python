from cryptography.fernet import Fernet
import time
x=1
starttime = time.time()
text = "seni siktim"

f = Fernet(b"ye")
f.encrypt(text)
while True:
    key = Fernet.generate_key()
    if x%100000 == 0:
        currentime = time.time()
        elapsedtime = currentime - starttime
        print(x, "|", key, "|", elapsedtime)
    x+=1