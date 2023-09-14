from pygame import mixer # pip install pygame
from gtts import gTTS  # pip install gtts
from time import sleep
import os

f = open('my_text.txt', 'r', encoding='UTF-8')
my_text = f.read()
f.close()

mp3_name = 'test_2.mp3'
mixer.init()

tts = gTTS(text=my_text, lang='ru')
tts.save(mp3_name)

mixer.music.load(mp3_name)
mixer.music.play(-1)
sleep(100)

# os.remove()
# pip install pyaudio

import speech_recognition as sr # pip install speechRecognition
r = sr.Recognizer()

while True:
    with sr.Microphone(device_index=1) as source:
        print('Скажи что-нибудь...')
        audio = r.listen(source)
    audio_text = r.recognize_google(audio, language='ru_RU')
    if audio_text == 'Привет':
        tts = gTTS(text='привет, друг', lang='ru')
        tts.save(mp3_name)

        mixer.music.load(mp3_name)
        mixer.music.play()
    else:
        print(audio_text)

