import os
import openai

openai.api_key = "your api key"
model_engine = "text-davinci-003"
p = input("Phrase: ")
prompt = "Create an analogy for phrase" + p

response = openai.Completion.create(
  engine=model_engine,
  prompt=prompt,
  max_tokens=2000,
  top_p=1,
  stop=None,
  temperature=0.5
)

r = response.choices[0].text
print("\nAnalogy:"+r)