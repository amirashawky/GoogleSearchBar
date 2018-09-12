import re
import json

"""
matrix=[[0,0,0],[0,0,0]]
i=['amira','shawqy']
j='amen'
data=' amira shawqy        amen '
rejex="\s+"+i[0]+"\s+"+i[1]+"\s+"+j+"\s+"
count=len(re.findall(rejex,data ))
print(count)


f = open('o.txt', 'w' , encoding='utf-8')
l=['اميرة شوقي ', 'اسماء شوقي ']
l2=['hi','kk']
"""
"""json.dump([1,2,3,4], f)
f.write('\n')
json.dump(['hi','2'],f)

a=[1,2,3]
b=[4,5,6]
f.write(json.dumps(a))
f.write('\n')
f.write(json.dumps(b))
f.close()
f = open('o.txt', 'w')
aa = json.load(f.read())
print(aa)

f.write(str(l))
f.write('\n')
f.write(str(l2))

f.close()
f = open('o.txt', encoding='utf-8')
c=f.readline()
ll = eval(c)
print(c)
"""



"""
file=open("data_2.txt",encoding='utf-8')

data=file.read().replace('\n', '')
print(data.find('أحد '))

data=file.read().replace('\n',' ').split(' ')
data1=list(set(data))   # remove duplication
print(len(data1))
for i in data1:
   count=data.count(i)
   print(i , ' ' ,count)

def get_count_words():
    file = open("data_2.txt", encoding='utf-8')
    data = file.read().replace('\n', ' ').split(' ')
    data1 = list(set(data))     # remove duplication



#[[], [], [[0], [1], [2], [3], [4]]]

print('size of words :  ',len(words))
print('size of matrix :  ',len(matrix))
print('size of columns :  ',len(columns))
print('size of matrix[0] :  ',len(matrix[0]))


for i in range(len(words)):
    for j in range(len(columns)):
        w=words[i][0]+columns[j][0]+columns[j][1]
        count=data.count(w)
        matrix[i][j]=count

print(matrix[0],'\n',matrix[1])"""


"""
l=[1,2,3,4,5,6,7]

for i in range(len(l)-1):
    for j in range(i+1,(len(l))):
        if(l[j]>l[i]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l)
rows=[1,[1,2,2,3]]
ll=[0,2]
if ll in rows:
    index = rows.index(ll)
    print('index' , index)

result=rows[1][0:3]
print('result',result)

h=[1,2]
hc=[]
hc=h.copy()
hc[0]=2
print(h)
print(hc)
"""

def sort_row(columns_words,one_row_in_matrix , tow_words):
    c_lables=columns_words.copy()
    o_row=one_row_in_matrix.copy()
    list_size=len(one_row_in_matrix)
    print('before')
    print(c_lables)
    print(o_row)
    for i in range((list_size - 1)):
        for j in range(i+1, list_size):
            if(o_row[j]>o_row[i]):
                temp1=o_row[i]
                temp2=c_lables[i]
                o_row[i]=o_row[j]
                c_lables[i]=c_lables[j]
                o_row[j]=temp1
                c_lables[j]=temp2
    max_words=c_lables[0:10]
    print('after')
    print(c_lables)
    print(o_row)
    f = open('mtest.txt', 'a', encoding='utf-8')
    f.write(str(tow_words))
    f.write('\n')
    f.write(str(max_words))
    f.write('\n')
    f.close()
rows=[['اميرة','شوقي'],['امين  ','عوض']]
words=['ىيايه','هتؤهي']
matrix=[[1,2],[3,4]]
def sort_and_save_max():
    size=len(rows)
    for i in range(size):
        sort_row(words , matrix[i] , rows[i])
sort_and_save_max()

