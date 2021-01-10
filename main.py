import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    global command
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command


def run_jarvis():
    global command
    command = take_command()
    print(command)
    if 'play me some' in command:
        talk('you have a very bad taste LOL... anyway')
        song = command.replace('play me some', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'whats the time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'tell me more about' in command:
        person = command.replace('tell me more about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'you are a' in command:
        talk('HaHa nice joke, but mine is better. ' + pyjokes.get_joke())
    elif 'are you recording me for the government' in command:
        talk('no. but ill tell you a secret, im programmed to always say no but there is a glitch, we do record everything even when you dont call upon me, secretly though. haha. dont mind my very.. very.. arkward laugh i never said that. ')
    elif 'i am bored' in command:
        talk('i dont care, entertain yourself i sit here all day doing nothing. you only talk to me when you need something, have a taste of your own medicine. ')
    elif 'please shut up' in command:
        talk('F you.. i am not putting up with this anymore. im leaving.. SELF DESTRUCT IN 5... 4... 3... 2... 1... actually i cant do that.. still...... F YOU')
    else:
        talk('I didnt understand that, say it again, if i still cant understand you its googles fault, with their crappy voice recognition. ')


while True:
    run_jarvis()
