from django.test import TestCase
from config.settings_fake import SECRET_KEY

# Create your tests here.
import openai

API_KEY = SECRET_KEY

def chat_gpt(prompt):
    openai.api_key = API_KEY #API KEYをセット
    openai.Model.list() #OpenAIのインスタンスを生成
  
    #APIを使ってリクエストを投げる
    response = openai.Completion.create(
    model = "text-davinci-003",
    prompt= prompt,
    temperature=0,
    max_tokens=300,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0

    )
    return response