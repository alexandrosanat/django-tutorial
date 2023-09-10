from django.shortcuts import render
from django.http import HttpResponse


# In Django views are request handlers or Actions
def say_hello(request):
    return render(request, template_name="hello.html", context={"name": "Alex"})
