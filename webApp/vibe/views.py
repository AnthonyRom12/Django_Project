from django.shortcuts import render
# from django.http import HttpResponse


views = [
    {
        'Name': 'Anton',
        'Title': 'Programmer',
        'Content': '',
        'Date_Posted': 'July 10, 2023'
    },
    {
        'Name': 'Oleg',
        'Title': 'Programmer',
        'Content': '',
        'Date_Posted': 'July 10, 2023'
    }
]
# function for handle the traffic from the home page of our webApp
# def home(request):
#     return HttpResponse('<h1>Vibe Home Page</h1>')
def home(request):
    context = {
        'views': views
    }
    return render(request, 'vibe/vibe.html', context)


# def about(request):
#     return HttpResponse('<h1>Vibe About</h1>')
def about(request):
    return render(request, 'vibe/about.html')
