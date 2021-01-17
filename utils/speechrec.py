import speech_recognition as sr
import os

rec = sr.Recognizer()

def speech2text(file_name):
    os.system('ffmpeg -i ' + file_name + '.ogg ' + file_name + '.wav')
    os.system('rm ' + file_name + '.ogg')
    nfile = sr.AudioFile(file_name + '.wav')
    with nfile as source:
        audio = rec.record(source)
    os.system('rm ' + file_name + '.wav')
    return rec.recognize_google(audio)