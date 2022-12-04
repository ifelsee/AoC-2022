inp = [ i for i in [i.split() for i in open("inp","r")][:-2]]


def main(inp) -> int:
    count = 0
    for i in inp:
        x,y = [j.split("-") for j in i[0].split(",")]
        a,b,c,d =  [int(f) for f in x+y]
    
        if a <= c and b >= d or c <= a and d >= b: 
            count +=1 

    
    return count 
        


print(main(inp))


