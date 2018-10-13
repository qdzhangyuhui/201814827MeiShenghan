## vsmknn
*向量空间模型 & K近邻算法*  
### 文件夹
- data  
  存放数据：包括文档的tf-idf向量(`docs.txt`)、单词表(`wordtable.json`)、含有特殊字符的文档列表(`bug.txt`)  
### 文件
- vsm.py  
  读取数据集中的文档，并将文档转换为tf-idf向量，结果存放在`data/docs.txt`，单词表存放在`data/wordtable.json`  
- knn.py  
  读取`tf-idf`向量，随机选取测试集，执行knn分类，并计算准确率  
