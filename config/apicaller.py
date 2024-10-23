import os
import google.generativeai as genai
import anthropic
from openai import OpenAI
from groq import Groq
from together import Together

#Yourkeys

openai_key = ""
gemini_key = ""
claude_key = ""
sambanova_key = ""
groq_key = ""
together_key = ""

#Gemini
genai.configure(api_key=gemini_key)
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)
#OpenAI
clientopenAI = OpenAI(
    api_key=openai_key,
)
#Claude
clientClaude = anthropic.Anthropic()
clientClaude = anthropic.Client(api_key=claude_key)

#Groq
clientGroq = Groq(
    api_key=groq_key,
)

#Together
clienttogether = Together(api_key=together_key)

#Sambanova
clientsamba = OpenAI(
    base_url="https://api.sambanova.ai/v1", 
    api_key=sambanova_key
)

#final response saving variable
def apicallermain(apiagent,jtitle,jdesc,jcomp,aboutys):
  finalResponse = ""
  print("Generating Cover content from API call")
  mainprompt = "Only provide content requested in the answer with no extra details in end or beginning, and no greetings like dear hiring manager etc in beginning and no endings salutations - just the main paragraphs or the content keep this in mind. So I want to create a concise yet powerful cover letter for the company"+jcomp+" and for job title"+jtitle+"the description for the job is the following"+jdesc+"and some information about me is the following"+aboutys+"write me the cover letter just the main paragraph according to the instructions given and please don't write something which is not true like some experience that i dont have just write a compelling and professional letter content according to information given"
  if apiagent == "groq":
    user_instructions = ""
    chat_completion = clientGroq.chat.completions.create(
    messages=[
        {"role": "system", "content": user_instructions},
        {
            "role": "user",
            "content": mainprompt,
        }
    ],
    model="llama3-8b-8192",)
    finalResponse=chat_completion.choices[0].message.content
  elif apiagent == "openai":
    response = clientopenAI.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": mainprompt}],)
    finalResponse=response.choices[0].message.content
  elif apiagent == "claude":
    message = clientClaude.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    temperature=0,
    system="answer concicely and professionally",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": mainprompt
                }
            ]
        }
    ])
    finalResponse=message.content
  elif apiagent == "gemini":
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(mainprompt)
    finalResponse=response.text
  elif apiagent == "sambanova":
    completion = clientsamba.chat.completions.create(
    model="Meta-Llama-3.1-405B-Instruct",
    messages = [
      {"role": "system", "content": "Answer concicely and professionally"},
      {"role": "user", "content": mainprompt}
    ],
    stream= True)
    for chunk in completion:
        finalResponse= finalResponse + (chunk.choices[0].delta.content)
  elif apiagent == "deepseek":
    print("deepseek coming soon")
  elif apiagent == "together":
    instructions = "answer concicely and professionally"
    stream = clienttogether.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages=[{"role": "user", "content": mainprompt}],
     stream=True,)
    for chunk in stream:
        finalResponse= finalResponse + (chunk.choices[0].delta.content)
  else:
    print("No such API service found.")
  #print(finalResponse)
  #finalResponse= "debug"+ jtitle+" "+jcomp+" "+jdesc
  return finalResponse
  
