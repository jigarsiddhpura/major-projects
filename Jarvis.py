import email , datetime
import pyttsx3 , requests
import datetime , re
import speech_recognition as sr
import wikipedia , random 
import webbrowser , os
import smtplib , pyjokes


def speak(audio):
    '''speak func takes string input and returns audio of the string'''
    converter = pyttsx3.init('sapi5')
    voices = converter.getProperty('voices')
    converter.setProperty('voice', voices[2].id)
    converter.setProperty('rate', 190)
    converter.setProperty('volume', 1)
    converter.say(audio)
    converter.runAndWait()


def takecommand():
    '''takecommand func takes user audio command and recognizes it'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')
    except Exception as e:
        print('Say that again please...')
        return 'None'
    return query


def wishMe():
    '''wishMe func wishes us according to present time'''
    time = int(datetime.datetime.now().hour)
    if time >= 0 and time <= 12:
        speak('Good Morning!')

    elif time >= 1 and time <= 6:
        speak('Good Afternoon!')

    else:
        speak('Good Evening!')

    speak('I am Jarvis , How may i help u ?')


def sendEmail(to, content):
    '''sendEmail func sends email using smtplib module'''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('my_gmail','my_password')
    server.sendmail('my_gmail', to, content)
    server.close()
    # my_gmail & my_password must be entered in the code to send email through that gmail

def sayNews(str):
    '''sayNews gives audio ouput of LATEST news in English '''
    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    converter.setProperty('volume', 1.2)
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    converter.setProperty('voice', voice_id)
    converter.say(str)
    converter.runAndWait()


if __name__ == '__main__':
    wishMe()
    while(1):
        query = takecommand().lower()
        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia')
                query = query.replace('wikipedia', '')
                results = wikipedia.summary(query, sentences=2)
                speak('According to Wikipedia:\n')
                print(results)
                speak(results)
            except Exception as e:
                speak(f'No information available about {query} on wikipedia')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            song = random.choice(songs)
            os.startfile(os.path.join(music_dir, song))

        elif 'the time' in query:
            present_time = datetime.datetime.now().strftime('%H:%M:%S')
            print(present_time)
            speak(f'Present time is {present_time}')

        elif 'send email ' in query:
            try:
                mail_dic = {'mahek':'maheksid07@gmail.com','rohan':'rohan@gmail.com','aman':'amanmanju4312@gmail.com'}
                for name,mail in mail_dic.items():
                    if name in query:
                        to = mail_dic[name]
                speak('What should i write?')
                content = takecommand()
                content = content.replace('say that', '')
                sendEmail(to, content)
                speak('Email has been sent!!')
            except Exception as e:
                print(e)
                speak('Oops! Something went wrong')

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'news' in query:
            try:
                sayNews("Starting Latest News")
                response = requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=54ad484f6aa7489a96182a950f2ab6d4")
                a = response.json()
                list1 = a["articles"]
                for i in list1:
                    print(i["title"])
                    sayNews(i["title"])
                    # Above line can be used to read the news.
                sayNews("Thanks for patient listening")
            except KeyboardInterrupt as e:
                exit()

        elif 'quit' in query:
            break
