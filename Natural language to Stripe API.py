import os
import openai

openai.api_key = "use your API"
model_engine = "text-davinci-003"
p = input("Give the sample of Natural language: ")
prompt = "Create code to call the Stripe API" + p

response = openai.Completion.create(
  engine=model_engine,
  prompt=prompt,
  max_tokens=2000,
  top_p=1,
  stop=None,
  temperature=0.5
)

r = response.choices[0].text
print("Stripe API:"+r)