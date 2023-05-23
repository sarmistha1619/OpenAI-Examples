import os
import openai

openai.api_key = "your openai API"
model_engine = "text-davinci-003"
prompt = input("Q:")

if prompt == "Ask Constance if we need some bread":
  print("A:`find ski store` Can I get my skis fixed before I leave on Thursday?")
else:
  response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1000,
    top_p=1,
    stop=None,
    temperature=0.5
  )

  r = response.choices[0].text
  print("A:" + r)

