inp = open("inp","r").read().split("\n")[:-2]

from collections import Counter 


def main(inp):
    l = [[] for j in range(8)]
    for i in inp:
        for idxJ, j in enumerate(i):
            l[idxJ].append(j)

    
    result = ["",""]
    for i in l:
        f = Counter(i).most_common()
        result[0] += f[0][0][0]
        result[1] += f[-1][0][0]


    print("first answer=> "+ result[0]+"\n"+"second answer => "+result[1])







main(inp)
