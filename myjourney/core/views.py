from django.shortcuts import render
from django.views import View

from core.models import Profile
from core.forms import SubscriberForm


def index(request):
    return render(request, 'index.html')


class IndexView(View):
    def get(self, request):
        name = Profile.objects.get(id=3).name

        form = SubscriberForm()

        desc = 'I am an Agile Engineer.'
        caption = 'Welcome to my Profile.'
        title = 'Hello you,'

        return render(
            request,
            'index.html',
            {
                'name': name,
                'desc': desc,
                'form': form,
                'caption': caption,
                'title': title,
            }
        )

    def post(self, request):
        name = Profile.objects.get(id=3).name

        form = SubscriberForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            Profile.objects.create(name=name, email=email)

        desc = 'I am an Agile Engineer.'
        caption = 'Welcome to my Profile.'
        title = 'Hello you,'

        return render(
            request,
            'index.html',
            {
                'name': name,
                'desc': desc,
                'form': form,
                'caption': caption,
                'title': title,
            }
        )
