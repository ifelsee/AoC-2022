import sys 

inp = [i.strip() for i in open("inp","r")]



def xInp(hInp):
    inp = hInp[:8]
    inpMax = max([len(i) for i in inp])
    transposeLst = [[] for _ in range(9)]

    for index,row in enumerate(inp):

        #normalization
        if row.__len__() < inpMax:
            row += " " * (inpMax-row.__len__())
        
        #parsing and transpose
        prev,st = 0,4
        for i in range(9):
            if row[prev:st-1] != "   ":
                transposeLst[i].append(row[prev:st-1])

            prev = st
            st += 4
            


    

    return [i[::-1] for i in transposeLst]   




















if __name__ == "__main__" and len(sys.argv) == 1:
    mInp = xInp(inp)
    print()
    [print("#",end="") for _ in range(80)]
    print()
    [print(_) for _ in mInp]




