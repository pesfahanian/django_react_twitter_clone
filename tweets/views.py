from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Tweet

# Create your views here.

def home(request, *args, **kwargs):
    context = {}
    # return render(request, 'home.html', context)
    return render(request, "pages/home.html", context={}, status=200)
    # return HttpResponse('<h1>Fuck You!</h1>')

def tweet_lits(request, *args, **kwargs):
    qs = Tweet.objects.all()
    data = [{"id": x.id, "content": x.content} for x in qs]

def tweet_detail(request, tweet_id, *args, **kwargs):
    data = {
        "id": tweet_id,
        # "content": obj.content,
        # "image_path": obj.image.url
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Tweet not found!"
        status = 404
    return JsonResponse(data, status=status)