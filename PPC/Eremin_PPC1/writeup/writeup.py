f = open('flag.txt', 'r')
alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_+=-/{}'
# FLAG ELON{dwadewisaidwiqriwcjzdvddj=}
def test(lst):
    return {"flag": a for a in set(lst) if lst.count(a) > 1}

mas = []
for line in f:
    line = line.split("\n")[0]
    mas.append(line)
f.close()
flag = test(mas)["flag"].split(",")
strd = ""
for simp in flag:
    strd += alph[int(simp)]
print(strd)
