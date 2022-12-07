import sys 
import numpy as np
inp = [i.strip() for i in open("inp","r")]



def xInp(hInp):
    inp = hInp[:8]
    inpMax = max([len(i) for i in inp])
    transposeInp = [[] for _ in range(9)]

    for index,row in enumerate(inp):

        #normalization
        if row.__len__() < inpMax:
            row += " " * (inpMax-row.__len__())
        
        #parsing and transpose
        prev,st = 0,4
        for i in range(9):
            if row[prev:st-1] != "   ":
                transposeInp[i].append(row[prev:st-1])

            prev = st
            st += 4
    

    return [i[::-1] for i in transposeInp]   


import time 






def main(hInp):
    base = xInp(hInp)
    inp = hInp[10:]
    print(base)

    def test(base):
        #normalleştirme
        maxofbase = max(map(len, base)) 
        basecopy = []
        for idx,row in enumerate(base):
            if len(row) < maxofbase:   
                basecopy.append(row+["   " for _ in range(maxofbase-len(row))])
            else:
                basecopy.append(row)

        tmp  = [[f" {i+1} " for i in range(9)] for _ in range(maxofbase+1)]

        for row in range(maxofbase):
            for colm in range(len(basecopy)):
                try:
                    tmp[maxofbase-row-1][colm] = basecopy[colm][row]  
                except: pass
                

        print(*["\n" for i in range(50)])
        for i in tmp: 
            for j in i:
                print( j,"", end="")
            print()

    
    test(base)


    for row in inp:
        cMove = int(row.split()[1])
        cFrom = int(row.split()[3])-1
        cTo = int(row.split()[5])-1





        base[cTo] += base[cFrom][-(cMove):]
        for i in range(cMove):
            base[cFrom].pop()
        
        count =0
        for i in base:
            for j in i:
                count+=1
        print(f"{count}".center(20,"#"))
        time.sleep(0.01)
        test(base)
        

        print("cMove => ",cMove," cFrpm => ",cFrom+1, " cTo => ",cTo  )
    for i in base:
        print(i[-1][1:2],end="")


   
 



    return " "










if __name__ == "__main__" and len(sys.argv) == 1:
    print()
    [print("#",end="") for _ in range(80)]
    print("\n")
    [print(_) for _ in main(inp)]





