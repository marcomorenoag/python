from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.timezone import datetime
from django.views.generic import ListView

from .forms import LogMessageForm
from .models import LogMessage


# def home(request):
#     return render(request, "hello/home.html")
class HomeListView(ListView):
    """Renders the home page, with a list of all messages.
    """
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


def about(request):
    return render(request, "hello/about.html")


def contact(request):
    return render(request, "hello/contact.html")


def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if not form.is_valid():
            return HttpResponse("Bad request")

        message = form.save(commit=False)
        message.log_date = datetime.now()
        message.save()
        return redirect("home")

    return render(request, "hello/log_message.html", {"form": form})


def hello_there(request, name):
    # now = datetime.now()
    # formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # # Filter the name argument to letters only using regular expressions.
    # # URL arguments can contain arbitrary text, so we restrict to safe characters only.
    # match_object = re.match("[a-zA-Z]+", name)

    # if match_object:
    #     clean_name = match_object.group(0)
    # else:
    #     clean_name = "Friend"

    # content = f'Hello there, {clean_name}! It´s {formatted_now}'
    # return HttpResponse(content)
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
