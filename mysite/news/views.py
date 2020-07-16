from django.shortcuts import render
from django.http import HttpResponse

# email
# import django
# from django.conf import settings
# from django.core.mail import send_mail


from .models import News


def index(request):
    news = News.objects.all
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, template_name='news/index.html', context=context)


# email
# def sendemail(request):
#     email = request.POST.get('email', '')
#     data = """
# Hello there! Mr. Kenoby
#
#     """
#     send_mail('Welcome!', data, "Pavel",
#               [email], fail_silently=False)
#     return render(request, 'email.html')