import json
from gtts import gTTS
import os

with open('config.json', 'r') as f:
    config = json.load(f)
    language=config['lang']
    doc_path=config['doc_path']
    tld=config['tld']
with open(doc_path, 'r',encoding='utf-8') as f:
    #read the file with utf-8 encoding
    myText = f.read()
    print(myText)


# a function that will divide up a long text into smaller chunks
def partition_text(text):
    # split the text into smaller chunks
    # each chunk is a list of sentences
    chunks = []
    chunk = []
    for sentence in text.split('.'):
        if len(chunk) < 10:
            chunk.append(sentence)
        else:
            chunks.append(chunk)
            chunk = [sentence]
    chunks.append(chunk)
    return chunks


myobj = gTTS(text=myText, lang=language, tld=tld,slow=False)
  
myobj.save("output/converted.mp3")