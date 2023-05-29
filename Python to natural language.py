import os
import openai

openai.api_key = "use you secret API key"
model_engine = "text-davinci-003"
p = input("Python Code: ")
prompt = "Explain a piece of Python code in human understandable language" + p

response = openai.Completion.create(
  engine=model_engine,
  prompt=prompt,
  max_tokens=2000,
  top_p=1,
  stop=None,
  temperature=0.5
)

r = response.choices[0].text
print("Natural Language:"+r)