from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import ChatForm
from .tests import chat_gpt

# Create your views here.


def home(request):
    return render(request, 'clearskin/home.html', {})

def index(request):
    chat_results=""
    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            # TODO: ChatGPT処理
            prompt=form.cleaned_data['prompt']
            response=chat_gpt(prompt)
            chat_results=response["choices"][0]["text"]
    else:
        form = ChatForm()
    template = loader.get_template('authtest/home.html')
    context = {
        'form': form,
        'chat_results': chat_results
    }
    return HttpResponse(template.render(context, request))

