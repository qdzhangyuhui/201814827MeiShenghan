import math
import random


# 余弦相似度存放类
class Cosine:
    def __init__(self, index, cos):
        self.index = index
        self.cos = cos


# 加载文档向量
def loaddata(filepath):
    vectors = []
    label = []
    with open(filepath, 'r') as f:
        line = f.readline()
        while line:
            vector = []
            item = str(line).split(',')
            for i in range(len(item) - 1):
                vector.append(float(item[i]))
            label.append(str(item[len(item) - 1]).replace('\n', ''))
            vectors.append(vector)
            line = f.readline()
    return vectors, label


# 随机选出测试集
def dataset(length):
    n = length // 40
    tests = random.sample(range(length), n)
    return tests


# knn分类器（利用余弦相似度划分）
def classification(tests, vectors, label, k):
    results = []
    correct = 0
    leng = len(vectors[0])
    for i in tests:
        result = []
        result.append(i)
        result.append(label[i])
        topk = []
        for j in range(k):
            topk.append(Cosine(-1, -1))
        minj = 0
        for j in range(len(vectors)):
            if j == i:
                continue
            dot = 0
            ''' Cosine '''
            modi = modj = 0
            for m in range(leng):
                dot = dot + vectors[i][m]*vectors[j][m]
                modi = modi + pow(vectors[i][m], 2)
                modj = modj + pow(vectors[i][m], 2)
            cosine = dot / (math.sqrt(modi) * math.sqrt(modj))
            ''' Distance
            for m in range(leng):
                dot = dot + pow(vectors[i][m] - vectors[j][m],2)
            cosine = math.sqrt(dot)
            '''
            cur = Cosine(j, cosine)
            flag = False
            for m in range(k):
                if cur.cos > topk[m].cos:
                    topk[minj] = cur
                    flag = True
                    break
            if flag:
                minj = 0
                for m in range(k):
                    if topk[m].cos < topk[minj].cos:
                        minj = m
        numc = {}
        for j in range(k):
            if label[topk[j].index] in numc:
                numc[label[topk[j].index]] = numc[label[topk[j].index]] + 1
            else:
                numc[label[topk[j].index]] = 1
        ma = sorted(numc.items(), key=lambda x: x[1], reverse=True)
        print(ma)
        result.append(ma[0][0])
        result.append(str(result[1]) == str(ma[0][0]))
        if str(result[1]) == str(ma[0][0]):
            correct = correct + 1
        results.append(result)
        print(str(result[1]) == str(ma[0][0]))
    return results, correct/len(results)


def main():
    filepath = 'data/docs.txt'
    vectors, label = loaddata(filepath)
    tests = dataset(len(vectors))
    print(tests)
    knnn, ap = classification(tests, vectors, label, 5)
    print(knnn)
    print(ap)


if __name__ == "__main__":
    main()
