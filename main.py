f = open('Talk.txt', 'r', encoding='utf-8')

savedText = {}

for line in f:
    l = line.split(':')
    if len(l) > 2:
        words = l[2].split(' ')
        for word in words:
            if len(word) > 1:
                if word[-1] == '을':
                    word = word[:-1]
                elif word[-1] == '를':
                    word = word[:-1]
                elif word[-1] == '은':
                    word = word[:-1]
                elif word[-1] == '는':
                    word = word[:-1]
                elif word[-1] == '이':
                    word = word[:-1]
                elif word[-1] == '가':
                    word = word[:-1]
                elif word[-1] == '에':
                    word = word[:-1]
                elif word[-1] == '\n':
                    word = word[:-1]
                    
                word = word.replace('ㅋㅋㅋㅋㅋㅋㅋ','ㅋㅋ')
                word = word.replace('ㅋㅋㅋㅋㅋㅋ','ㅋㅋ')
                word = word.replace('ㅋㅋㅋㅋㅋ','ㅋㅋ')
                word = word.replace('ㅋㅋㅋㅋ','ㅋㅋ')
                word = word.replace('ㅋㅋㅋ','ㅋㅋ')
                
                if word in savedText:
                    savedText[word] += 1
                else:
                    savedText[word] = 1

newtext = {}
for key, value in savedText.items():
    if value > 2:
        newtext[key] = value

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

mask = Image.new("RGBA",(1200,1200), (255,255,255)) 
font='./font2.ttf'
word_cloud = WordCloud(font_path=font, 
                        background_color='black',
                        max_font_size=1000, 
                        max_words=2000, 
                        colormap='prism').generate_from_frequencies(newtext)

plt.figure(figsize=(10,8))
plt.imshow(word_cloud)
plt.axis('off')
plt.savefig('talk.png', bbox_inches='tight')
plt.show()