import os
import openai

openai.api_key = "your API key"
model_engine = "text-davinci-003"
prompt = ":A table summarizing" + input("Passage:")

response = openai.Completion.create(
  engine=model_engine,
  prompt=prompt,
  max_tokens=2000,
  top_p=1,
  stop=None,
  temperature=0.5
)

r = response.choices[0].text
print("A table summarizing the main topics:"+r)