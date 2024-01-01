
with open("ans.txt",mode="r",encoding="utf-8") as file:
    data = file.read()
cor=data.split("isCorrect")
usan=data.split("userAnswer")
ans=data.split(f"answer\\\":")
corlist=[]
usanlist=[]
anslist=[]
for i in range(len(cor)):
    corlist.append(cor[i][3])
    if usan[i][4].isdigit() ==True:
        usanlist.append(int(usan[i][4])+1)
    else:
        usanlist.append("null")
    if ans[i][1].isdigit() ==True:
        anslist.append(int(ans[i][1])+1)
    else:
        anslist.append("null")

for i in range (len(corlist)):
    if corlist[i] ==str(0):
        print("第"+str(i)+"題: 你選"+str(usanlist[i])+" 答案是"+str(anslist[i]))


