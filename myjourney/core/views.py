from django.shortcuts import render
from django.views import View

from core.models import Profile, Subscriber
from core.forms import SubscriberForm


def index(request):
    return render(request, "index.html")


class IndexView(View):
    def get(self, request):
        name = Profile.objects.all().first().name
        email = Profile.objects.all().first().email

        form = SubscriberForm()

        desc = "I am an Agile Engineer."
        email = "Email: " + email
        caption = "Welcome to my Profile."
        title = "Hello you,"

        return render(
            request,
            "index.html",
            {
                "name": name,
                "desc": desc,
                "form": form,
                "caption": caption,
                "title": title,
            },
        )

    def post(self, request):
        name = Profile.objects.all().first().name
        email = Profile.objects.all().first().email

        form = SubscriberForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            Subscriber.objects.create(email=email)

        desc = "I am an Agile Engineer."
        email = "Email: " + email
        caption = "Welcome to my Profile."
        title = "Hello you,"

        return render(
            request,
            "index.html",
            {
                "name": name,
                "desc": desc,
                "form": form,
                "caption": caption,
                "title": title,
            },
        )
