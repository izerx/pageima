from django.shortcuts import render
from selenium import webdriver
from django.http import HttpResponse, JsonResponse

def index(request): 
    return render (request, 'App/index.html')

def API(request):
    driver = webdriver.PhantomJS()
    driver.set_window_size(1920, 1080)

    try:
        driver.get(request.GET.get('url'))
    except Exception as e:
        return HttpResponse(e.args)

    img = driver.get_screenshot_as_png()

    return HttpResponse(img, content_type="image/png")
