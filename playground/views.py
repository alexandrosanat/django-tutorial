from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


# In Django views are request handlers or Actions
def say_hello(request):
    return render(request, template_name="hello.html", context={"name": "Alex"})


def article_list(request):
    articles = Article.objects.all().order_by("date")
    return render(
        request,
        template_name="articles/article_list.html",
        context={"articles": articles},
    )


