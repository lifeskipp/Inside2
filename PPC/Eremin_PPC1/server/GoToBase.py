import re

alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_+=-/{}'

FLAG = "ELON{jfrelwqekfawdjkaefkawdkaw=}"

k = []
for fl in FLAG:
    k.append(str(alph.find(fl)))
k = (",").join(k)
print(k)

