import json
from gtts import gTTS
import os

with open('config.json', 'r') as f:
    config = json.load(f)
    language=config['lang']
    doc_path=config['doc_path']
with open(doc_path, 'r') as f:
    myText = f.read()

myobj = gTTS(text=myText, lang=language, slow=False)
  
myobj.save("output/converted.mp3")