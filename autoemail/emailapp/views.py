from django.urls import reverse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import viewsets
from .models import Mail
from .serializer import MailSerializers


# Create your views here.


def homepage(request):
    if request.method == "POST":
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        mail = request.POST.get('mail')
        post = Mail( emailad = email , mailsub = subject, mailtext = mail)
        post.save()

    eve = Mail.objects.all().order_by('-mail_id')
    paginator = Paginator(eve, 10)
    page = request.GET.get('page')
    try:
        studs = paginator.page(page)
    except PageNotAnInteger:
        studs = paginator.page(1)
    except EmptyPage:
        studs = paginator.page(paginator.num_pages)

    context = {'studs':studs}
    return render(request,'index.html', context)

class MailView(viewsets.ModelViewSet):
    queryset = Mail.objects.all()
    serializer_class = MailSerializers
