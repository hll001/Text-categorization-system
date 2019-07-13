import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from user.function.classfy import Classfy_test
from user.function.getnewscontent import get_newcontent


# Create your views here.
def index(request):
    return render(request, 'mainpage.html')
    # return HttpResponse('2jygjgjug')


def main(request):
    return render(request, 'mainpage.html')


def resultpage(request):
    return render(request, 'resultpage.html')


def classfyapi(request):
    if request.method == 'POST':
        content = json.loads(request.body).get('text')
        # print(content)
        return JsonResponse(Classfy_test(content))


def newscontent(request):
    if request.method == 'POST':
        url = json.loads(request.body).get('text')
        # print(url)
        return JsonResponse(get_newcontent(url))
