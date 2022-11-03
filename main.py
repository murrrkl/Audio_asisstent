import speech_recognition as sr
import sys
import pyttsx3

def talk(words):
    print(words)
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


talk("Привет, назови слово на английском, а я его переведу")

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        zadanie = r.recognize_google(audio).lower()
        print("Вы сказали:" + zadanie)
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        zadanie = command()

    return zadanie

def makeSomething(zadanie):
    if 'hi' in zadanie:
        talk("привет")
    elif 'cat' in zadanie:
        talk("кот")
    elif 'dog' in zadanie:
        talk("собака")
    elif 'stop' in zadanie:
        talk("Да, конечно, без проблем")
        sys.exit()

while True:
    makeSomething(command())
