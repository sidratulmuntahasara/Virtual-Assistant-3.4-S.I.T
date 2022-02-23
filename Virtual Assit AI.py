import pyttsx3
import emoji
import webbrowser
import speech_recognition as sr
#PyAudio
#PyWhatKit
#PyJokes
#Wikipedia
#OpenweatherApi


mark = pyttsx3.init()
rate = 150
mark.setProperty("rate", rate)
greet = input()
if greet=="Hi" or greet=="hi" or greet=="Hey" or greet=="hey" or greet=="hello" or greet=="Hello":
    print("""Good Day! Glad to meet you!
How are you doing?""")
    speech = "Good day! Glad to meet you! How are you doing?"
    mark.say(speech)
else:
    print("Hey! Nice to meet you! How is life?")
    speech = "Hey! Nice to meet you! Howz life?"
    mark.say(speech)
mark.runAndWait()
feel=input("""Choose your feeling: Great/Good/Fine/Cheerful/Excited/Sad/Sick/Tired:
    ==  """)
if feel=="good" or feel=="Good":
    print("Great! Well, I am happy for you!")
    speech="Great!... Welll,... I am happy for you!"
    mark.say(speech)
elif feel=="fine" or feel=="Fine":
    print("Cool! Enjoy life buddy!")
    speech="Coool!... Enjoy life buddy!"
    mark.say(speech)
elif feel=="cheerful" or feel=="Cheerful":
    print("Woah! Me too!")
    speech="Woah! Me too!"
    mark.say(speech)
elif feel=="excited" or feel=="Excited":
    print(emoji.emojize("That's great! This is life :smiling_face_with_sunglasses:"))
    speech="That's great! This is the Life!..."
    mark.say(speech)
elif feel=="great" or feel=="Great":
    print("That's a really great feeling!")
    speech="That's a really great feeling!..."
    mark.say(speech)
elif feel=="sad" or feel=="Sad":
    print("Oh, I'm sorry! I hope you will feel better soon...")
    speech="Ooh, I'm sorry! I hope you will feel better soon..."
    mark.say(speech)
elif feel=="sick" or feel=="Sick":
    print(emoji.emojize("Get Well Soon! :crossed_fingers:"))
    speech="Oh! Get Well Soon!"
    mark.say(speech)
elif feel=="tired" or feel=="Tired":
    print(emoji.emojize("Oh... Take rest, all the best! :thumbs_up:"))
    speech="Ooh!... Take rest, all the best!"
    mark.say(speech)
else:
    print("""Sorry! I didn't get that :[
But I hope you are doing well!""")
    speech="Sorry! I didn't get that...But I hope you are doing well!"
    mark.say(speech)
mark.runAndWait()

print(emoji.emojize("You may ask me anything you want to know about... :thinking_face:"))
speech = "You may ask me anything you want to know about..."
mark.say(speech)
mark.runAndWait()

search=input('Search: ')
print(emoji.emojize("Here's what I found..."))
speech = "Here's what I found..."
mark.say(speech)
mark.runAndWait()
webbrowser.open('https://www.google.com/search?q='+search)

