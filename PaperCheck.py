# coding=utf-8


import jieba
import re
import gensim

def getFileContents(path):
    str=''
    f=open(path,'r',encoding='UTF-8')
    line=f.readline()
    while line:
        str=str+line
        line=f.readline()
    f.close()
    return str


#��䴦��ģ�飬�����ӷִ��ҹ��˵�����ת�����
def strFilter(string):
    #ʹ��������ʽ���˵�����ת�����
    pattern = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]") 
    string = pattern.sub("", string)
    #���ӷִ�
    result = jieba.lcut(string)
    return result

#ת���ͼ���ģ�飬������ת��Ϊ�������������������ƶ�
def transAndComput(text1,text2):
    texts=[text1,text2]
    #����ת��Ϊ����
    dictionary=gensim.corpora.Dictionary(texts)
    corpus=[dictionary.doc2bow(text) for text in texts]    
    #�����������ƶ�
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(text1)
    cosine_sim = similarity[test_corpus_1][1]
    return cosine_sim

def conduct(path1,path2):
    save_path = "D:\PythonApplication1\save.txt"
    str1 = getFileContents(path1)
    str2 = getFileContents(path2)
    text1 = strFilter(str1)
    text2 = strFilter(str2)
    similarity = transAndComput(text1, text2)
    print("\nSimilarity Of 2 passages:%.4f\n"%similarity)
    #�����ƶȽ��д��ָ���ļ�
    f = open(save_path, 'a', encoding='UTF-8')
    f.write("Similarity Of 2 passages:%.4f\n"%similarity)
    f.close()



if __name__ == '__main__':
    conduct("D:\PythonApplication1\orig_0.8_dis_10.txt","D:\PythonApplication1\orig_0.8_dis_15.txt")
    conduct("D:\PythonApplication1\orig_0.8_add.txt","D:\PythonApplication1\orig.txt")
    conduct("D:\PythonApplication1\orig_0.8_dis_1.txt","D:\PythonApplication1\orig_0.8_del.txt")