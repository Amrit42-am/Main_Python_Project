import speech_recognition as sr
import webbrowser
import pyttsx3
import Music_lib
import AI_mode as AI
import chatbot as CB
import Que_ans as QA

recognizer = sr.Recognizer()  
engine = pyttsx3.init()  

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":

    k = True

    try:
        r = sr.Recognizer()
        print("Activation word........")
        with sr.Microphone() as source:
            print("Adjusting for background noise... Please wait.")
            r.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio_text = r.listen(source, timeout=5, phrase_time_limit=2)
            word = r.recognize_google(audio_text)

        if word.lower() == "jarvis":
            print("Jarvis is now active and ready to listen for your command.....")
            speak("Jarvis is now active and ready to listen for your command.")
            k = True
        else:
            print(f"You said: {word}, which is not the activation word.")
            speak(f"You said: {word}, which is not the activation word.")
            k = False
    except Exception as e:
        print("Activation word not detected. Exiting.")
        k = False
        # print("Error in activation word detection:", e)
        # k = False

    def process_command(command):
        command = command.lower()
        global k
        if command == "exit":
            speak("Exiting Jarvis. Goodbye!")
            k = False
            print("Exiting Jarvis. Goodbye!")
        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
            print("Opening YouTube")
        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
            print("Opening Google")
        elif "open instagram" in command:
            speak("Opening Instagram")
            webbrowser.open("https://www.instagram.com")
            print("Opening Instagram")
        elif "open facebook" in command:
            speak("Opening Facebook")
            webbrowser.open("https://www.facebook.com")
            print("Opening Facebook")
        elif command.lower() in Music_lib.music:
            speak(f"Playing {command}")
            webbrowser.open(Music_lib.music[command.lower()])
            print(f"Playing {command}")
        
        elif "ai mode" in command.lower():
            speak("Activating AI mode.")
            print("Please state your topic for AI mode:")
            while True:
                try:
                    with sr.Microphone() as source3:
                        speak("Listening for topic...")
                        print("Listening for topic...")
                        r.adjust_for_ambient_noise(source3, duration=1)
                        audio_text2 = r.listen(source3, timeout=5, phrase_time_limit=3)
                        topic = r.recognize_google(audio_text2)
                    if "exit ai mode" in topic.lower() or "exit" in topic.lower():
                        speak("Exiting AI mode.")
                        print("Exiting AI mode.")
                        speak("Now returning to normal mode.")
                        print("Now returning to normal mode....")
                        print("\n")
                        speak("Normal mode activated.")
                        break
                    else:
                        speak(f"About {topic}")
                        print(f"\t\tAbout {topic} is as follows:-\n")
                        AI.About(topic)
                except:
                    print("Sorry, I did not get that. Please repeat the topic.")
                    speak("Sorry, I did not get that. Please repeat the topic.")
        
        elif "chatbot mode" in command.lower() or "chat bot mode" in command.lower() or "chatbot" in command.lower():
            speak("Activating Chatbot mode.")
            print("Activating Chatbot mode.")

            speak("Gemini Chatbot is ready.")
            speak("If you want to exit, say 'exit' or 'quit'.")
            speak("How can I assist you today?")
            print("🤖 Gemini Chatbot ready! Say 'exit/quit' to quit/exit.\n")
            while True:
                try:
                    with sr.Microphone() as source4:
                        speak("Listening for you...")
                        print("Listening for you...")
                        r.adjust_for_ambient_noise(source4, duration=1)
                        audio_text3 = r.listen(source4, timeout=5, phrase_time_limit=3)
                        user_words = r.recognize_google(audio_text3)
                    if "exit chatbot mode" in user_words.lower() or "exit" in user_words.lower():
                        speak("Exiting Chatbot mode.")
                        print("Exiting Chatbot mode.")
                        speak("Now returning to normal mode.")
                        print("Now returning to normal mode....")
                        print("\n")
                        speak("Normal mode activated.")
                        break
                    else:
                        CB.chat_start(user_words)
                except:
                    print("Sorry, I did not get that. Please repeat.")
                    speak("Sorry, I did not get that. Please repeat.")
        
        elif "question answer mode" in command.lower() or "question and answer mode" in command.lower() or "q and a mode" in command.lower() or "qna mode" in command.lower():
            speak("Activating Question Answer mode.")
            print("Activating Question Answer mode.")
            speak("Please state your question.")
            while True:
                try:
                    with sr.Microphone() as source5:
                        speak("Listening for your question...")
                        print("Listening for your question...")
                        r.adjust_for_ambient_noise(source5, duration=1)
                        audio_text4 = r.listen(source5, timeout=10, phrase_time_limit=5)
                        question = r.recognize_google(audio_text4)
                    if "exit question answer mode" in question.lower() or "exit" in question.lower() or "quit" in question.lower() or "exit qna mode" in question.lower():
                        speak("Exiting Question Answer mode.")
                        print("Exiting Question Answer mode.")
                        speak("Now returning to normal mode.")
                        print("Now returning to normal mode....")
                        print("\n")
                        speak("Normal mode activated.")
                        break
                    else:
                        speak(f"Answering the question: {question}")
                        print(f"\t\tAnswer of the question '{question}' is as follows:-\n")
                        QA.QnA(question)
                except:
                    print("Sorry, I did not get that. Please repeat the question.")
                    speak("Sorry, I did not get that. Please repeat the question.")
        
        
        # elif "tell me about" in command.lower():
        #     topic = command.lower().replace("tell me about", "").strip()
        #     speak(f"About {topic}")
        #     AI.About(topic)
        #     print(f"Generated information on {topic}")
       
        else:
            speak("Sorry, I did not understand that command.")
            print("Sorry, I did not understand that command.")

    while k:
            
        try:
            with sr.Microphone() as source2:  
                print("Listening...")
                r.adjust_for_ambient_noise(source2, duration=1)
                audio_text = r.listen(source2, timeout=4, phrase_time_limit=2)

                command = r.recognize_google(audio_text)

                i = process_command(command)
        except:
                print("Sorry, I did not get that")