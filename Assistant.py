import pyttsx3
import speech_recognition as sr
import time,datetime
import wikipedia
import webbrowser
import os


engine=pyttsx3.init('sapi5')   
voices =engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
          engine.say(audio)
          engine.runAndWait()

def wishMe():
          hour=int(datetime.datetime.now().hour)
          if hour>=0 and hour<12:
                    speak("Good Morning!")
                    print("Good Morning!")
          elif hour>=12 and hour<18:
                    speak("Good Afternoon!")
                    print("Good Afternoon!")
          else:
                    speak("Good Evening!")
                    print("Good Evening!")
          speak("I am David your Voice assistant. Please Tell me Instruction")
          print("I am David your Voice assistant. Please Tell me Instruction")

def takeCommand():
          #It takes Microphone input from user and return output
          r=sr.Recognizer()
          with sr.Microphone() as source:
                    print("Listening...")
                    r.pause_threshold= 1
                    audio =r.listen(source)

          try:
                    print("Recognizing...")
                    query =r.recognize_google(audio, language='en-in')
                    print("Your command:",query)
          except Exception as e:
                   ##  print(e)   ----> this Show Exception Error on Console

                    print("Say That again please...")
                    return "none"
          return query
if __name__=="__main__":
           wishMe()

           while(1):
                    query=takeCommand().lower()
                    
                    #Logic for executing task
                    #for open Wikipedia
                    if 'wikipedia' in query:
                              speak('searching wikipedia...')
                              query=query.replace('wikipedia',"")
                              results=wikipedia.summary(query,sentences=1)
                              speak("According to wikipedia")
                              print(results)  
                              speak(results)

                    #open browsers
                    
                    elif 'open youtube' in query:
                              webbrowser.open("youtube.com")
                    elif 'open google' in query:
                              webbrowser.open("google.com")
                    elif 'open internshala' in query:
                              webbrowser.open("internshala.com")
                    elif 'open stackover flow' in query:
                              webbrowser.open("stackoverflow.com")

                    #hi,how are you,who are you asking !

                    elif 'hi david' in query:
                              speak("hello sir")
                              print("hello sir!")       
                    elif 'who are you' in query:
                              speak("I am david sir")
                              print("I am david sir!")
                    elif 'how are you' in query:
                              speak("I feel good. thanks for asking")
                              print("I feel good. thanks for asking!")

                    #For music
                    elif 'play music' in query:
                              music_dir='D:\\Music Bollywood'
                              songs=os.listdir(music_dir)
                              print(songs)
                              os.startfile(os.path.join(music_dir,songs[0]))

                    elif 'the time' in query:
                              strTime = datetime.datetime.now().strftime("%H:%M:%S")  
                              speak(strTime)    
                              print(strTime)
                   
                    
                              
                     

                    
                             