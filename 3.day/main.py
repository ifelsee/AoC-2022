inp = [i.split() for i in open("inp","r")][:-1]


def main(inp):
    result  = 0
    for i in inp:

        common_item  = set()
        i = i[0]
        l = len(i)
        
        
        for j in i[0:l//2]:
            item = [ j if j == k else None for k in i[l//2:]]
            [common_item.add(k) if k !=  None else ""  for k in item]

        x = lambda x:  ord(x)-96 if not x.isupper() else  ord(x)-38
        result+=(sum(map(x, common_item)))
    print(result)

main(inp)
