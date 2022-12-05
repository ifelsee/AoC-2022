import re
import sys 

inp = [i.strip() for i in open("inp","r")]
def matrix_inp(inp):
    m_inp =[] 

    for index_j, j in enumerate(inp[:8]): 
        c=0; tmp = ""; arr = []
        m_inp_tmp = ["   " for _ in range(8)]

        for i in j:
            c+=1; tmp+=i

            if c >3 and i == " ":
                arr.append(tmp[:-1])
                c=0; tmp=""
            
        for index_a, a in enumerate(arr):
            m_inp_tmp[index_a] = a

        m_inp.append(m_inp_tmp)
    return m_inp


if __name__ == "__main__": 
    m_inp = matrix_inp(inp)
    if len(sys.argv) == 1:
        [print(_) for _ in m_inp]




