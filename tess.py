import speech_recognition as sr
import webbrowser
import openai
import datetime
import os

class TESSAI:
    def __init__(self):
        self.chat_str = ""
        self.user_profiles = {}

    def chat(self, query):
        self.chat_str += f"User: {query}\nTESS: "
        response = self.get_openai_response(self.chat_str)
        self.say(response)
        self.chat_str += f"{response}\n"

    def get_openai_response(self, prompt):
        openai.api_key = "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"  
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response["choices"][0]["text"]

    def say(self, text):
        os.system(f'say "{text}"')

    def take_command(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            try:
                query = recognizer.recognize_google(audio, language="en-in")
                print(f"User said: {query}")
                return query.lower()
            except sr.UnknownValueError:
                return "Could not understand the audio"
            except sr.RequestError as e:
                return f"Could not request results from Google Speech Recognition service; {e}"

    def open_website(self, site_name, site_url):
        webbrowser.open(site_url)
        self.say(f"Opening {site_name}.")

    def play_music(self, music_path):
        os.system(f"open {music_path}")
        self.say("Playing music.")

    def get_current_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M")
        self.say(f"The current time is {current_time}.")

    def personalized_greeting(self, user_name=None):
        if user_name:
            self.say(f"Hello, {user_name}! How can I assist you today?")
        else:
            self.say("Hello! How can I assist you today?")

    def update_user_profile(self, user_name, user_data):
        self.user_profiles[user_name] = user_data

if __name__ == '__main__':
    tess = TESSAI()
    
    
    tess.update_user_profile("Anusree", {"age": 20, "location": "Kolkata"})
    
    
    tess.personalized_greeting("Anusree")

    while True:
        print("Listening...")
        user_query = tess.take_command()

        if "open youtube" in user_query:
            tess.open_website("YouTube", "https://www.youtube.com")

        elif "open wikipedia" in user_query:
            tess.open_website("Wikipedia", "https://www.wikipedia.org")

        elif "play music" in user_query:
            music_path = "C:\Users\Anusree\Downloads\music"
            tess.play_music(music_path)

        elif "the time" in user_query:
            tess.get_current_time()

        elif "using artificial intelligence" in user_query:
            tess.chat(user_query)

        elif "tess quit" in user_query:
            tess.say("Goodbye!")
            break

        elif "reset chat" in user_query:
            tess.chat_str = ""

        else:
            tess.chat(user_query)
