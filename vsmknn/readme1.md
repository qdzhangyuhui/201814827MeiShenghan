## vsmknn
*向量空间模型 & K近邻算法*  
### 文件夹
- data  
  存放数据：包括文档的tf-idf向量(`tfidf.txt`)、单词表(`wordtable.json`)、含有特殊字符的文档列表(`bug.txt`)  
### 文件
- delbug.bat  
  windows批处理文件，可以删除含有特殊字符的文档  
- vsm.py  
  读取数据集中的文档，并将文档转换为tf-idf向量，结果存放在`data/tfidf.txt`，单词表存放在`data/wordtable.json`  
- knn.py  
  读取`tf-idf`向量，在每个类里随机选取20%测试集，执行knn分类，并计算准确率  
### 运行
```
delbug.bat
python vsm.py
python knn.py
```