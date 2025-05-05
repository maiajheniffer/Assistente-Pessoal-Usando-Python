import os 
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia

#=== definindo o idioma

engine = pyttsx3.init("sapi5")
engine.setProperty('voice', engine.getProperty( "voices")[0].id)
wikipedia.set_lang("pt")

# === fazendo o(a) assistente falar

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

#==== ouvir

def getCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Estou te ouvindo")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("reconhendo o comando")
        command = r.recognize_google(audio, language="pt-br")
        print(f"Fala entendida: {command}\n")
        
    except Exception as e:
        print(e)
        print("erro ao ouvir")
    return command

if __name__ == "__main__":
    speak("Olá, sou sua assistente!")
    speak("em que posso te ajudar?")
    
    #=== chamar funções para interagir com assistente
    
    while(True):
        command = getCommand().lower()
        if 'wikipédia' in command:
            #cancelar ruídos
            command = command.replace("wikipédia", "")
            command = command.replace("procure na", "")
            
            results = wikipedia.summary(command, sentences = 2)
            
            speak("De acordo com a Wikipédia")
            speak(results)
        elif 'google' in command:
            speak("google")
            webbrowser.open("google.com")
            exit(0)
        elif 'calculadora' in command:
            speak("abrindo a calculadora")
            loc = "caminho para a sua calculadora"  
            os.startfile(loc) 
        #=== desligar assistente
        elif 'tchau' in command:
            speak("Tchau!")
            exit(0)
    