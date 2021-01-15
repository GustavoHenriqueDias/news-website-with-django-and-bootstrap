from django.shortcuts import render


# Create your views here.

def home(request):
    import requests
    import json

    news_api_request = requests.get("http://newsapi.org/v2/everything?domains=wsj.com&apiKey=0923534f8e6440f4a42e3a8096ebddb9")
    
    api = json.loads(news_api_request.content)
    
    return render(request, 'home.html', {'api':api})

def about(request):
    return render(request, 'about.html')

def info(request):
    return render(request, 'info.html')