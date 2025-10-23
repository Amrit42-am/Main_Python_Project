
# from py_compile import main
import google.generativeai as genai
import pyttsx3
import os


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

engine = pyttsx3.init()

def speak(text: str):
    engine.say(text)
    engine.runAndWait()

# chat = ""

# def main():
#     # global chat
#     # Start a persistent chat session with history memory
#     # chat = model.start_chat(history=[])

#     speak("Gemini Chatbot is ready.")
#     speak("How can I assist you today?")
#     print("🤖 Gemini Chatbot ready! Say 'exit/quit' to quit/exit.\n")


def chat_start(user_words):
        chat = model.start_chat(history=[])
        # speak("Gemini Chatbot is ready.")
        # speak("If you want to exit, say 'exit' or 'quit'.")
        # speak("How can I assist you today?")
        # print("🤖 Gemini Chatbot ready! Say 'exit/quit' to quit/exit.\n")
        # global chat
        while True:

            user_input = user_words
            print("You:", user_input)
            if user_input.lower() in ["exit", "quit"]:
                speak("Goodbye")
                print("Bot: Goodbye! 👋")
                break

            # Send message to Gemini chat session
            response = chat.send_message(user_input)

            # Get text response
            bot_reply = getattr(response, "text", str(response))

            print("Bot:", bot_reply)
            speak(bot_reply)
            break

# if __name__ == "__main__":
#     main()
