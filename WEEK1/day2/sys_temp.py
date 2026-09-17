import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("api error")
client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"
role="user"
prompt="Suggest a name for my clothing brand"
message_system={
    "role":"system",
    "content":"You are a brand manager and i have been developing a fitness tracker for past few months and i want a unique name for my fitness tracker. so suggest me a name and make sure that it should be in one word"
}

message={
    "role":role,
    "content":prompt
}
messages=[message_system,message]
response=client.chat.completions.create(model=model,messages=messages,temperature=1)
#print(response.choices[0].message)
print("#############################################################################################")
answer=response.choices[0].message.content
print(answer)
 