from django.shortcuts import render

def landing_page(request):
    # print(request.COOKIES["csrftoken"])
    return render(request, 'landing_page.html')