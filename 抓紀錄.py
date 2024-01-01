
with open("tmuans.txt",mode="r",encoding="utf-8") as file:
    data = file.read()
all=data.split("isCorrect")
for i in range(len(all)):
    ch=all[i][3]
    if ch ==str(0):
        un=all[i-1].split("nswer")
        cn=un[1][4]
        yn=un[2][4]
        ck=[]
        for y in range(5):
            ck.append(un[2][21+y*2])
        print("第"+str(i)+"題: 你選"+str(ck.index(yn)+1)+" 答案是"+str(ck.index(cn)+1))

