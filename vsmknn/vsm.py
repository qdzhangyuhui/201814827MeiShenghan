import nltk
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords
import re
import string
import os
import math
import json


# 循环遍历文件夹，并返回文档列表
def cata(filepath):
    files = []
    for root, dirs, fs in os.walk(filepath):
        for f in fs:
            files.append(root+"\\"+f)
    return files


# 经文档转换为向量
def loadfile(filelist):
    vectors = []
    for i in filelist:
        vectors.append(prodata(i))
        print(i + " is ok.")
    return vectors


# 预处理
def prodata(i):
    with open(i, "r") as f:
        artical = f.read()
    f.close()
    tokens = nltk.word_tokenize(artical)  # 分词
    n = len(tokens)
    ls = LancasterStemmer()
    for i in range(n):
        tokens[i] = ls.stem(tokens[i])  # 词干还原
    nst = [w for w in tokens if w not in stopwords.words(
        'english')]  # 去除停用词
    rep = re.compile('[%s]' % re.escape(string.punctuation))
    nws = list(filter(lambda word: word != "", [
        rep.sub("", word) for word in nst]))  # 去除标点符号
    return nws


# 词汇表
def ctable(vectors):
    wordtable = {}
    ind = 0
    for i in vectors:
        for j in i:
            if j in wordtable:
                continue
            else:
                wordtable[j] = ind
                ind = ind + 1
    return wordtable


# 计算tf-idf
def doctfidf(doc, vectors, wordtable):
    tfidfvector = []
    tf = 0
    idf = 0
    freq = wordfreq(doc)
    for i in range(len(wordtable)):
        tfidfvector.append(0)
    for i in set(doc):
        tf = freq[i]
        idf = math.log((len(vectors) + 1) / (filecount(i, vectors) + 1))
        tfidf = tf*idf
        tfidfvector[wordtable[i]] = tfidf
    return tfidfvector


# 词频
def wordfreq(doc):
    freq = {}
    for i in doc:
        if i in freq:
            freq[i] = freq[i] + 1
        else:
            freq[i] = 1
    return freq


# 包含某一单词的文档数
def filecount(word, vectors):
    count = 0
    for i in vectors:
        if word in set(i):
            count = count + 1
    return count


def main():
    filepath = '..\\data'
    filelist = cata(filepath)
    print("load begin")
    vectors = loadfile(filelist)
    print("load end")
    wordtable = ctable(vectors)
    with open('data/wordtable.json', 'w') as f:
        json.dump(wordtable, f)
        print("save wordtable done.")
    f.close()
    with open('data/tfidf.txt', 'w') as f:
        f.write("")
    f.close()
    for i in filelist:
        doc = prodata(i)
        tfidfvector = doctfidf(doc, vectors, wordtable)
        with open('data/tfidf.txt', 'a') as f:
            for j in tfidfvector:
                f.write(str(j) + ',')
            fp = i.split('\\')
            if(fp[-2] == 'alt.atheism'):
                f.write('1')
            elif(fp[-2] == 'comp.graphics'):
                f.write('2')
            elif(fp[-2] == 'comp.os.ms-windows.misc'):
                f.write('3')
            elif(fp[-2] == 'comp.sys.ibm.pc.hardware'):
                f.write('4')
            elif(fp[-2] == 'comp.sys.mac.hardware'):
                f.write('5')
            elif(fp[-2] == 'comp.windows.x'):
                f.write('6')
            elif(fp[-2] == 'misc.forsale'):
                f.write('7')
            elif(fp[-2] == 'rec.autos'):
                f.write('8')
            elif(fp[-2] == 'rec.motorcycles'):
                f.write('9')
            elif(fp[-2] == 'rec.sport.baseball'):
                f.write('10')
            elif(fp[-2] == 'rec.sport.hockey'):
                f.write('11')
            elif(fp[-2] == 'sci.crypt'):
                f.write('12')
            elif(fp[-2] == 'sci.electronics'):
                f.write('13')
            elif(fp[-2] == 'sci.med'):
                f.write('14')
            elif(fp[-2] == 'sci.space'):
                f.write('15')
            elif(fp[-2] == 'soc.religion.christian'):
                f.write('16')
            elif(fp[-2] == 'talk.politics.guns'):
                f.write('17')
            elif(fp[-2] == 'talk.politics.mideast'):
                f.write('18')
            elif(fp[-2] == 'talk.politics.misc'):
                f.write('19')
            elif(fp[-2] == 'talk.religion.misc'):
                f.write('20')
            else:
                f.write('0')
            f.write("\n")
        f.close()
        print(i + ' is done.')
    print("all done.")


if __name__ == '__main__':
    main()
