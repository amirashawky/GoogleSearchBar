import re , string

words = []    # all the columns labels
matrix = []    # all the row's values in the matrix
rows = []    # all the row labels

def read_words(words):
    file = open("test1.txt", encoding='utf-8')
    for line in file:
        l = line.replace('.', ' ').replace(',', ' ').replace('-', ' ').replace(':', ' ').replace('(',' ').replace(')',' ').replace('\n',' ').replace('،',' ')
        #l=re.sub(r'[^\w\s]','',line)
        l = re.sub('\d', ' ', l)
        l = re.split('\s+', l)
        # print(l)
        if len(words) == 0:
            words.append([l[0], 1])
        for sub in l:
            found = 0
            for t in words:
                if t[0] == sub:
                    t[1] += 1
                    found = 1
            if (found == 0):
                words.append([sub, 1])
    file.close()

def get_rows(rows, data):
    list=re.split('\s+', data)
    for i in range(len(list)-1):
        l =[]
        l.append(list[i])
        l.append(list[i+1])
        if l not in rows :
            rows.append(l)
        """else:
            print(l)
            print('in')"""

def initialize_matrix(matrix):
    for i in range(len(rows)):
        row=[]
        for j in range(len(words)):
            row.append(0)
        matrix.append(row)

def get_matrix_count(rows , words , matrix , data):
    for i in range(len(rows)):
        for j in range(len(words)):
            w1=rows[i]
            w2=words[j][0]
            rejex="\s+"+w1[0]+"\s+"+w1[1]+"\s+"+w2+"\s+"
            count=len(re.findall(rejex,data ))
            matrix[i][j]=count

def save_to_file(words, rows , matrix):
    f = open('o.txt', 'w' , encoding='utf-8')
    f.write(str(words))
    f.write('\n')
    f.write(str(rows))
    f.write('\n')
    f.write(str(matrix))
    f.write('\n')
    f.close()

def load_file(words, rows , matrix):
    f = open('o.txt', encoding='utf-8')
    ws = f.readline()
    words=eval(ws)
    ws=f.readline()
    rows=eval(ws)
    ws=f.readline()
    matrix=eval(ws)

def sort_row(columns_words,one_row_in_matrix , tow_words):
    c_lables=columns_words.copy()
    o_row=one_row_in_matrix.copy()
    list_size=len(one_row_in_matrix)
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
    f = open('max_file.txt', 'a', encoding='utf-8')
    #f.write(str(tow_words))
    #f.write('\n')
    f.write(str(max_words))
    f.write('\n')
    f.close()

def sort_and_save_max():
    size=len(rows)
    for i in range(size):
        sort_row(words , matrix[i] , rows[i])

def load_max_file():
    max_words_list=[]
    f = open('max_file.txt', encoding='utf-8')
    for line in f:
        x=eval(line)
        max_words_list.append(x)
    return max_words_list

def run_to_get_file():
    read_words(words)
    file = open("test1.txt", encoding='utf-8')
    data = file.read().replace('\n', ' ').replace('.', ' ').replace(',', ' ').replace('-', ' ').replace(':',' ').replace('(', ' ').replace(')', ' ')
    data = re.sub('\d', ' ', data)
    data=re.sub('\s+',' ',data)

    get_rows(rows, data)

    initialize_matrix(matrix)

    get_matrix_count(rows , words , matrix , data)
    sort_and_save_max()
    save_to_file(words, rows , matrix)


run_to_get_file()



def get_10_predection(str):
    L=str.split()
    size=len(L)
    ll=[]
    ll.append(L[size-1])
    ll.append(L[size])
    index=0
    if ll in rows:
        index = rows.index(ll)
    result=max_words_list[index]
    return result




load_file(words, rows , matrix)
max_words_list=load_max_file()
get_10_predection()