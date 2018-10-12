import nltk
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords
import re
import string
import os
import codecs
import math
import json


# 循环遍历文件夹，并返回文档列表
def cata(filepath):
    files = []
    for root, dirs, fs in os.walk(filepath):
        for f in fs:
            files.append(root+"\\"+f)
    return files


# 加载所有文档，并转换为向量
def loadfile(filelist):
    vectors = []
    for i in filelist:
        vectors.append(prodata(i))
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
def doctfidf(doc, vectors, wordtable, filelist):
    tfidfvector = []
    tf = 0
    idf = 0
    freq = wordfreq(doc)
    for i in range(len(wordtable)):
        tfidfvector.append(0)
    for i in set(doc):
        tf = freq[i]
        idf = math.log((len(filelist) + 1) / (filecount(i, vectors) + 1))
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
        if word in i:
            count = count + 1
    return count


def main():
    filepath = '..\\testdata'
    filelist = cata(filepath)
    vectors = loadfile(filelist)
    wordtable = ctable(vectors)
    with open('data/wordtable.json', 'w') as f:
        json.dump(wordtable, f)
        print("save wordtable done.")
    f.close()
    with open('data/docs.txt', 'w') as f:
        f.write("")
    f.close()
    for i in filelist:
        doc = prodata(i)
        tfidfvector = doctfidf(doc, vectors, wordtable, filelist)
        print(len(tfidfvector))
        with open('data/docs.txt', 'a') as f:
            for j in tfidfvector:
                f.write(str(j)+',')
            fp = i.split('\\')
            if(fp[-2][:4] == 'comp'):
                f.write('1')
            elif(fp[-2][:4] == 'misc'):
                f.write('2')
            elif(fp[-2][:3] == 'rec'):
                f.write('3')
            elif(fp[-2][:3] == 'sci'):
                f.write('4')
            elif(fp[-2][:4] == 'talk'):
                if(fp[-2][5:13] == 'politics'):
                    f.write('5')
            else:
                f.write('6')
            f.write('\n')
        f.close()
        print(str(i) + ' is done.')
    print("all done.")


if __name__ == '__main__':
    main()
