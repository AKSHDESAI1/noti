from django.http.response import HttpResponse
from django.shortcuts import render
from plyer import notification


def a1(request):
    if request.method == 'POST':
        notification.notify(
            title="please drink water",
            message="wow"
       

         )
        return HttpResponse('wow')
    return render(request, 'home.html')
