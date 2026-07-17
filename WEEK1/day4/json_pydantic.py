import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API KEY not found")
client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"
role="user"

from pydantic import BaseModel
class ticket(BaseModel):
    name:str
    email:str
    issue:str

schema=ticket.model_json_schema()

response_format={
    "type":"json_object"
}

system_prompt=f"""Extract personal information from the ticket strictly based on the on the schema and give a json output.
{schema}
"""

message_system={
    "role":"system",
    "content":system_prompt
}

text="Hello my name is Pranjal Prateek. Yesterday i bought an iphone for my girl but it stopped working today. I bought it from the unicorn strore in greater noida . please contact me on this mail id pranjal@gmail.com or on 84235"

prompt = f"""
Extract these fields:
- name
- email
- issue

Ticket:
{text}

Return only JSON.
"""
message={
    "role":role,
    "content":prompt
}
messages=[message_system,message]
response=client.chat.completions.create(model=model,messages=messages,response_format=response_format)
answer=response.choices[0].message.content

print(answer)

import json
raw_json=answer

data_file=json.loads(raw_json)
Ticket=ticket(**data_file)

print(Ticket.name)
print(Ticket.email)
print(Ticket.issue)