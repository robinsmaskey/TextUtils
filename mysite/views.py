# I have created this file - Robins

from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
#    return HttpResponse('''<h1>Robins Sher Maskey</h1> <a href='https://www.manutd.com/en'> Manchester United</a>''')

#def about(request):
#    return HttpResponse('About Football')

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Home")

def ex1(request):
    s='''<h2> Navigation Bar <br> </h2>
    <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
    <a href="https://www.facebook.com/"> Facebook </a> <br>
    <a href="https://www.flipkart.com/"> Flipkart </a> <br>
    <a href="https://www.hindustantimes.com/"> Newz </a> <br>
    <a href="https://www.google.com/"> Google </a> <br> '''
    return HttpResponse(s)

def analyze(request):
    #get the text   
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charactercounter= request.POST.get('charactercounter','off')

    print(djtext)
    print(removepunc)
    #analyzed = djtext
    #analyze the text
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed= analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

        #return render(request,'analyze.html', params)

    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
        
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!= "\r":
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

        #return render(request,'analyze.html', params)

    if extraspaceremover=="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

        #return render(request, 'analyze.html', params)

    if charactercounter == "on":
        analyzed = ""
        for char in djtext:
            analyzed= len(djtext)
        params = {'purpose': 'Count the characters', 'analyzed_text': analyzed}
    
    if(removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and charactercounter != "on"):
        return HttpResponse("please select any operation and try again")
        
    return render(request, 'analyze.html', params)


def capfirst(request):
    return HttpResponse('capitalize first')

def newlineremove(request):
    return HttpResponse("capitalize first")

def spaceremove(request):
    return HttpResponse("space remover <a href = '/'> back</a>" )

def charcount(request):
    return HttpResponse("charcount ")




