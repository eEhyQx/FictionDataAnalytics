import matplotlib.pyplot as plt
import jieba
import jieba.analyse
import numpy as np
import codecs
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import jieba.posseg as pseg
#img_array=
#,allowPOS=('nr')
stopword=[]
text=codecs.open('./章节/chap6.txt','r','utf-8').read()
tags=jieba.analyse.extract_tags(text,topK=100,
      withWeight=True,allowPOS=('n'))
tf=dict((a[0],a[1]) for a in tags)
#bg=plt.imread('')
for key,value in tf.items():
    print('{key},{value}'.format(key = key, value = value))
#,mask=bg
wc=WordCloud(stopwords=stopword,font_path='C:\Windows\Fonts\STZHONGS.TTF',width=1000,height=800,background_color='white')
wc=wc.generate_from_frequencies(tf)
wc.to_file('./章节/chap6.png')
plt.figure(num=None,figsize=(12,10),facecolor='w',edgecolor='k')
plt.imshow(wc)
plt.axis('off')
plt.show()



