import os
import openai



openai.api_key = "your api key"
model_engine = "text-davinci-003"
user_input = input("Input:")
p = "print the name: and mailing address:" + user_input

response = openai.Completion.create(
    model=model_engine,
    prompt=p,
    max_tokens=1000,
    top_p=1,
    stop=None,
    temperature=0.9,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

r = response.choices[0].text
print("Output"+r)