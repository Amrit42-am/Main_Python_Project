import google.generativeai as genai
import os
import pyttsx3

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = genai.GenerativeModel("gemini-2.5-flash")

engine = pyttsx3.init()

def speak(text: str):
    engine.say(text)
    engine.runAndWait()

def QnA(topic: str) -> str:
    response = gemini_model.generate_content(
        f"Answer the question: {topic}"
    )
    
    text = getattr(response, "text", str(response))
    print(text)



if __name__ == "__main__":
    topic = input("Enter the question you want to ask:- ")
    print(f"\t\tAnswer of the question '{topic}' is as follows:-\n")

    content = QnA(topic)
    print("Ans:", content)
    if content:
        speak(content)