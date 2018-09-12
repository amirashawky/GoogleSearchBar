
file=open("test1.txt",encoding='utf-8')
words=[]


# reading file

for line in file:
    l=line.replace('.',' ').replace(',',' ').replace('-',' ').replace(':',' ')
    l=line.split(' ')
    #print(l)
    if len(words)==0:
        words.append([l[0],1])
    for sub in l:
        found=0
        for t in words:
            if t[0]==sub:
                t[1]+=1
                found=1
        if(found==0):
            words.append([sub,1])
file.close()

# to set matrix

rows=[]
matrix=[]
for i in range(len(words)-1):
    l=[]
    l.append(words[i][0])
    l.append(words[i+1][0])
    rows.append(l)
for j in range(len(words)):
    init=[]
    for k in range(len(rows)):
        init.append(0)
    matrix.append(init)


## count number of occurance
file=open("test1.txt",encoding='utf-8')
data = file.read().rstrip("\n")


for i in range(len(words)):
    for j in range(len(rows)):
        w=words[i][0]+' '+rows[j][0]+' '+rows[j][1]
        print('word   ',w)
        count=data.count(w)
        print('count = ',count)
        matrix[i][j]=count


# -----------------------------------------------------------------------------------------------

user_input=input('enter word\n')
line=user_input.split(' ')
size=len[line]




