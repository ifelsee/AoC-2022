inp = [i.split() for i in open("inp","r")][:-1]
result  = 0
for i in inp:
    op,me = i
    v1 = {"X":1,
          "Y":2,
          "Z":3}[me]
    v2 = {"A X":3, "B Y":3, "C Z":3,
          "A Z":0, "B X":0, "C Y":0,
          "A Y":6, "B Z":6, "C X":6}[op+" "+me]
        
    result+=(v2+v1 )

print(result)
# A = Taş 
# X = Taş 

# B = Kağıt 
# Y = Kağıt 

# C = Makas
# Z = Makas
