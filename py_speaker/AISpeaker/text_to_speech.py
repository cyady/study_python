# TTS(Text To Speech)
# STT(Speech To Text)

from gtts import gTTS
from playsound import playsound

file_name = 'sample.mp3'


# 영어 문장
# text = 'Imagine that you have just arrived at a hotel after a tiring 7-hour overnight flight.'
# tts_en = gTTS(text=text, lang='en')
# tts_en.save(file_name)
# playsound(file_name) #.mp3 파일 재생

# 한글 문장
# text = '월이에요. 무었을 도와드릴 까요?'
# tts_ko = gTTS(text=text, lang='ko')
# tts_ko.save(file_name)
# playsound(file_name)


# # 긴 문장 ( 파일에서 불러와서 처리)
with open('sample.txt', 'r', encoding='utf8') as f:
    text = f.read()

tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)
playsound(file_name)



