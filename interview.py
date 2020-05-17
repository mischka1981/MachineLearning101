from gtts import gTTS
import os
import sys
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import pydub                         # ffmpeg.exe needs to be in the PATH.
from playsound import playsound
import random

# Problems:
#    scipy.io.wavfile for saving the recording produces a wave file that gTTS cannot read
#    pydub converts the broken wave into mp3 and back into wave using ffmpeg
#    playsound for playback

def hear():
    fs = 44100  # Sample rate
    seconds = 6  # Duration of recording
    filename = "output.wav"
    filename2 = "output2.wav"
    print(">>")
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    print("...")
    write(filename, fs, myrecording)  # Save as WAV file   
    sound = pydub.AudioSegment.from_wav(filename)
    sound.export(filename + ".mp3", format="mp3")
    sound = pydub.AudioSegment.from_mp3(filename+".mp3")
    sound.export(filename2, format="wav")
    r = sr.Recognizer()
    with sr.AudioFile(filename2) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data, language="de-DE")
        print(text)
        return text

def say(txt):
    print(txt)
    try:
        os.remove("spricht.mp3")
    except:
        print("")
    g = gTTS(txt, lang="de")
    g.save('spricht.mp3')
#    os.system('spricht.mp3')
    playsound('spricht.mp3')

def greeting(nm):
    greetings = ["Ich habe von Dir geträumt, <name>. ",
                 "Ich glaube, ich habe Dich schon einmal gesehen, <name>. ",
                 "Du siehst auch total so aus wie jemand der <name> heißt. ",
                 "Du könntest auch anders heißen. ",
                 "<name> soll Bundeskanzler werden! ",
                 "<name> ist ja mein Lieblingsname ! ",
                 "<name> vor, noch ein Tor! ",
                 "<name>. Das ist schöner Name!",
                 "Ich mag <name>. "]
    r = random.choice(greetings)
    return r.replace("<name>", nm)

def loop():
    while True:
        frageLoop()

def frageLoop():
    fragen = []
    fragen.append("Wie ist dein Name?")
    fragen.append("Was ist deine Lieblingsfarbe?")
    fragen.append("Wo wohnst Du?")
    fragen.append("Wie alt bist Du?")
    fragen.append("Was ist dein Lieblingsessen?")
    fragen.append("Was spielst Du am liebsten?")
    antworten={}
    for frage in fragen:
        if fragen.index(frage) > 1:
            say(antworten[fragen[0]] +" , " + frage)
        else:
            say(frage)
        antworten[frage] = ""
        while antworten[frage] == "":
            try:
                antworten[frage] = hear()
            except:
                say("Das habe ich nicht verstanden! Bitte sag es nochmal.")
                antworten[frage] = ""
            
        if fragen.index(frage)==0:
            say(greeting(antworten[fragen[0]]))
        else:
            say("Aha achso, " + antworten[frage])
            
    satz = antworten[fragen[0]] + " aus "+  antworten[fragen[2]] +", du bist ja jetzt schon " +  antworten[fragen[3]] + " Jahre alt. "
    satz = satz + "Du futterst am liebsten " +  antworten[fragen[1]] + " " +  antworten[fragen[4]]+ ". "
    satz = satz + " Beim Essen darfst Du aber auf keinen Fall " +  antworten[fragen[5]] + " spielen."
    print(satz)
    say(satz)

say("Hallo, ich bin Gitta Gittigitt.")
loop()
