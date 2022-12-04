inp = [ i for i in [i.split() for i in open("inp","r")][:-2]]

def main(inp) -> int:
    count = 0
    for i in inp:
        x,y = [j.split("-") for j in i[0].split(",")]
        a,b,c,d =  [int(f) for f in x+y]
        
        #if a == c or a == d or b == c or b == d:
        #   count+=1

        x_range = [j for j in range(a,b+1)]
        y_range = [j for j in range(c,d+1)]

        for j in x_range:
            if j in y_range:
                count+=1
                break

    return count 
        


print(main(inp))


