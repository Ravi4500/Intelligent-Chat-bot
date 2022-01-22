import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_input():
    with sr.Microphone() as source:
        print("I am listening....,speak out")
        speak("I am listening....,speak out")
        voice = listener.listen(source)
        input = listener.recognize_google(voice)
        input = input.lower()

    return input

def message():
    print("Please enter a mobile number")
    print("Please enter a message which you want to send")
    print("Please enter the time in hrs")
    print("Please enter the number in minutes\n")
    input1 = str(input())
    input2 = str(input())
    input3 = int(input())
    input4 = int(input())
    return [input1,input2,input3,input4]



def run():
    command = take_input()
    if 'play' in command:
        song = command.replace('play', '')
        speak('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        speak('current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)

    elif 'search' in command:
        thing = command.replace('search', '')
        speak("Give me a second,I will get you results")
        pywhatkit.search(thing)

    elif 'send message' in command:
        ans = message()
        pywhatkit.sendwhatmsg("+91"+" "+ans[0],ans[1],ans[2],ans[3])

    elif 'How are you' in command:
        print(command)
        speak("I am good, Thanks for asking and what about you")

    elif 'what is' in command:
        what = command.replace('what is', '')
        speak("Give me a second,I will get you results")
        pywhatkit.search(what)


run()
