import speech_recognition as sr
import pyttsx3
import openai as ai
r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 250)
engine.setProperty('voice', 'english-us')
with sr.Microphone() as source:
   audio = r.listen(source)
ai.api_key = "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"
def generate_gpt3_response(user_text, print_output=False):
    completions = ai.Completion.create(
        engine='text-davinci-003', 
        temperature=0.5,            
        prompt=user_text,          
        max_tokens=200,            
        n=1,                        
        stop=None,                  
    )
    return completions.choices[0].text
run = True
while run:
    if __name__ == '__main__':
        usr = r.recognize_google
        print(usr)
        prompt = usr
        response = generate_gpt3_response(prompt)
        engine.say(response)
        engine.runAndWait()