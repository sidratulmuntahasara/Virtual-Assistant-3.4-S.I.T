import pyttsx3
import emoji
import webbrowser
import pywhatkit
import pyjokes
import wikipedia
import requests

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your OpenWeatherMap API key
LOCATION = "YOUR_CITY"  # Replace with your city

def text_to_speech(text):
    engine = pyttsx3.init()
    rate = 150
    engine.setProperty("rate", rate)
    engine.say(text)
    engine.runAndWait()

def greet_user():
    greet = input()
    if greet.lower() in ["hi", "hey", "hello"]:
        response = "Good day! Glad to meet you! How are you doing?"
    else:
        response = "Hey! Nice to meet you! How's life?"
    print(response)
    text_to_speech(response)

def user_feeling():
    feelings = {
        "good": "Great! Well, I am happy for you!",
        "fine": "Cool! Enjoy life, buddy!",
        "cheerful": "Woah! Me too!",
        "excited": "That's great! This is life 😎",
        "great": "That's a really great feeling!",
        "sad": "Oh, I'm sorry! I hope you will feel better soon...",
        "sick": "Get well soon! 🤞",
        "tired": "Oh... Take rest, all the best! 👍",
    }
    feel = input("Choose your feeling: Great/Good/Fine/Cheerful/Excited/Sad/Sick/Tired:\n==  ").lower()
    response = feelings.get(feel, "Sorry! I didn't get that. But I hope you are doing well!")
    print(response)
    text_to_speech(response)

def search_query(search):
    print(emoji.emojize("Here's what I found..."))
    text_to_speech("Here's what I found...")
    webbrowser.open('https://www.google.com/search?q=' + search)

def tell_joke():
    joke = pyjokes.get_joke()
    print(joke)
    text_to_speech(joke)

def play_youtube_video(query):
    print("Playing video...")
    text_to_speech("Playing video...")
    pywhatkit.playonyt(query)

def get_weather_info():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={LOCATION}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    print(f"Weather in {LOCATION}: {weather}, {temp}°C")
    text_to_speech(f"Weather in {LOCATION}: {weather}, {temp} degrees Celsius")
def get_wikipedia_summary(query):
    summary = wikipedia.summary(query, sentences=2)
    print(summary)
    text_to_speech(summary)

def process_input(user_input):
    user_input = user_input.lower()
    if "joke" in user_input:
        tell_joke()
    elif "play" in user_input and "youtube" in user_input:
        play_youtube_video(user_input.replace("play", "").replace("youtube", "").strip())
    elif "weather" in user_input:
        get_weather_info()
    elif "wikipedia" in user_input:
        get_wikipedia_summary(user_input.replace("wikipedia", "").strip())
    else:
        search_query(user_input)

def main():
    greet_user()
    user_feeling()

    while True:
        print("\nAsk me anything or type 'exit' or 'bye' to end.")
        user_input = input()
        if user_input.lower() in ["exit", "bye"]:
            print("Goodbye! Have a nice day!")
            text_to_speech("Goodbye! Have a nice day!")
            break
        process_input(user_input)

if __name__ == "__main__":
    main()
