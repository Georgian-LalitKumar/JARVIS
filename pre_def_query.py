import 
while True:
     #if 1:
        query = takeCommand().lower() 
    # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        

        #opening youtube
        elif 'open youtube'in query:
            webbrowser.open("youtube.com")
       
       
       
        # to search via command on google
        elif ' on google'in query:
            try:

	            from googlesearch import search 
            except ImportError: 
	            print("No module named 'google' found")       
            for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
	            webbrowser.open(j) 

        #opening stackoverflow website
        elif 'open stackoverflow'in query:
            webbrowser.open("stackoverflow.com")
        
        
        
        # to play music on local device
        elif 'play music' in query:
            music_dir ='E:\\audios'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        
        
        # to get the time update
        elif ' time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open code ' in query:
            codePath="C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        
        
        # to kill the terminal
        elif 'close ' in query:
            speak("Have a nice day sir ")
            sys.exit()
            
        
        # to send an email via voice
        elif 'send email' in query:
            try:
                speak("what should i say ?")
                content = takeCommand()
                to =""
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry email has not been sent ,sir!")
        
        
        # to take a screenshot via voice command
        elif 'screenshot' in query:
            img=ImageGrab.grab()
            img.save('screenshot.bmp')
            speak(f"this is screenshot captured")
            img.show()
        
        
        # to search on youtube via command  
        elif 'on youtube' in query:
            query_string = urllib.parse.urlencode({"search_query" : query })    #Use the urllib.parse.urlencode() function to convert such dictionaries into query strings.
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])
