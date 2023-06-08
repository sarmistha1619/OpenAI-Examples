import os
import openai
import pyttsx3

openai.api_key = "your api key"
model_engine = "text-davinci-003"
user_input = input("Topic:")
prompt = "Create interview questions:" + user_input

response = openai.Completion.create(
    model=model_engine,
    prompt=prompt,
    max_tokens=1000,
    top_p=1,
    stop=None,
    temperature=0.5,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

r = response.choices[0].text
print("Questions:"+r)

test_to_speech = pyttsx3.init()
speech = r
test_to_speech.say(speech)
test_to_speech.runAndWait()
