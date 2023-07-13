from django.shortcuts import render

# from django.http import HttpResponse


views = [
    {
        'Top_Channels': 'CS GO world',
        'Title': 'CS GO',
        'Content': 'News, channels'

    },
    {
        'Top_Channels': 'The Witcher fans',
        'Title': 'The Witcher',
        'Content': 'News, channels'

    },
    {
        'Top_Channels': 'Gangsters',
        'Title': 'Grand Theft Auto 5',
        'Content': 'News, channels'

    },
    {
        'Top_Channels': 'Cowboy',
        'Title': 'Red Dead Redemption 2',
        'Content': 'News, channels'

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
    return render(request, 'vibe/about.html', {'title': 'About'})
