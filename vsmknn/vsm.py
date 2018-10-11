import nltk
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords
import re
import string


def main():
    with open("../testdata/a", "r") as f:
        artical = f.read()
    f.close()
    # 预处理
    tokens = nltk.word_tokenize(artical)  # 分词
    n = len(tokens)
    ls = LancasterStemmer()
    for i in range(n):
        tokens[i] = ls.stem(tokens[i])  # 词干还原
    nst = [w for w in tokens if w not in stopwords.words('english')]  # 去除停用词
    rep = re.compile('[%s]' % re.escape(string.punctuation))
    nws = list(filter(lambda word: word != "", [
               rep.sub("", word) for word in nst]))  # 去除标点符号
    print(nws)


if __name__ == '__main__':
    main()
