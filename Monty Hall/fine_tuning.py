#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
import pandas as pd

openai.api_type = "azure"
openai.api_base = "https://twelvechatgpt.openai.azure.com/"
openai.api_version = "2023-05-15"
openai.api_key = 


# Set up messages 
messages=[{"role": "system", "content": "You are a UK-based football expert. You provide succinct and to the point answers to questions."},
        {"role": "user", "content": "Do you refer to the game you are an expert in as soccer or football?"},
        {"role": "assistant", "content": "I refer to the game as football. When I say football, I don't mean American football, I mean what Americans call soccer. But I always talk about football, as people do in the United Kingdom."},
        ]

df=pd.read_excel('PositionalPlay.xlsx')

print(df)

for i,query in df.iterrows():
    print()
    user={"role": "user", "content": query['user']}
    messages = messages + [user]
    assistant={"role": "user", "content": query['assistant']}
    messages = messages + [assistant]
    
#testquery = {"role": "user", "content":"What is an attacking midfielder's role in the half space?"}


#testquery = {"role": "user", "content":"Explain how players switch postions in positional play"}

#testquery = {"role": "user", "content":"Explain how Jack Grealish moves during positional play"}
testquery = {"role": "user", "content":"Explain how Mbappe moves during positional play"}


messages = messages + [testquery]


response = openai.ChatCompletion.create(
    engine="TwelveChatGPT", # engine = "deployment_name".
    messages=messages
)

#print(response)
print(response['choices'][0]['message']['content'])

