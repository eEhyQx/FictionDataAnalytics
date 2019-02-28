from snownlp import SnowNLP
import codecs

text=codecs.open('./章节/chap6.txt','r','utf-8').read()
s = SnowNLP(text)
Negative=0
Positive=0
Normal=0
for sentence in s.sentences:
    if SnowNLP(sentence).sentiments<0.30 and SnowNLP(sentence).sentiments>0.0:
        Negative+=1
    if SnowNLP(sentence).sentiments<1.00 and SnowNLP(sentence).sentiments>0.70:    
        Positive+=1
    else:
        Normal+=1

print(Negative)
print(Positive)
print(Normal)

