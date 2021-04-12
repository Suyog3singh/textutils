#I have created this file - Suyog
from django.http import HttpResponse 
from django.shortcuts import render


# def index(request):
#     return HttpResponse('''<h1><a href="https://www.google.com/">Google</a></h1>''')

# def about(request):
#     return HttpResponse("This is about page")

def index(request):
    # params = {"name":"Suyog","place":"Indore"}
    return render(request, 'index.html')
    # return HttpResponse("Home")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text','default')
 
    # Get checkbox value
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newline = request.POST.get('newline','off')
    spaceremover = request.POST.get('spaceremover','off')
    countcharacters = request.POST.get('countcharacters','off')
    punctuations = '''’'()[]{}<>:,‒–—―…!.«»-‐?‘’“”;/⁄␠   ·&@*\\•^¤¢$€£¥₩₪†‡°¡¿¬#№%‰‱¶′§~¨_|¦⁂☞∴‽※'''
    analyzed = ""
    if removepunc == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char 

        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed
        # Analyze the text

    if(fullcaps=='on'):
        analyzed = djtext.upper()
        params = {'purpose':'Capitalize','analyzed_text':analyzed}
        djtext = analyzed

    if(newline=='on'):
        for char in djtext:
            if char !='\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose':'New Line Remover','analyzed_text':analyzed}
        djtext = analyzed

    if(spaceremover=='on'):
        for char in djtext:
            if char !=' ':
                analyzed = analyzed + char
        params = {'purpose':'Space Remover','analyzed_text':analyzed}
        djtext = analyzed

    elif(countcharacters=='on'):
        i = 0
        for char in djtext:
            i = i+1
            analyzed = i
        params = {'purpose':'Chracter Counter','analyzed_text':analyzed}
        
    if(removepunc != 'on' and fullcaps != 'on' and newline != 'on' and spaceremover != 'on' and countcharacters != 'on'):
        
        return HttpResponse("Please select any operation and try again"+(s))
     

    return render(request,'analyze.html',params)


# def removepunc(request):
#     # Get the text
#     djtext = request.GET.get('text','default')
#     print(djtext)
#     # Analyze the text
#     return HttpResponse("removepunc")

# def capitalize(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newlineremove")

# def spaceremove(request):
#     return HttpResponse("spaceremove")

# def charcount(request):
#     return HttpResponse("charcount")




