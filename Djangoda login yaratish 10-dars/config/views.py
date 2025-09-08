from django.shortcuts import render

def landing_page(request):
    print(request.COOKIES["sessionid"])
    return render(request, 'landing_page.html')