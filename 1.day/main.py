l = []
with open("input","r") as inp:
    tmp =0
    for i in inp.read().split("\n"):
        try:
            tmp+= int(i)
        except: 
            l.append(tmp)
            tmp = 0 

