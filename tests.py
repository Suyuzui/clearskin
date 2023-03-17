from django.test import TestCase

# Create your tests here.
import openai

APK_KEY = ""

def chat_gpt(prompt):
    openai.api_key = APK_KEY #API KEYをセット
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