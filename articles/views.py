from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms


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


def article_detail(request, my_slug):
    article = Article.objects.get(slug=my_slug)
    # return HttpResponse(article.body)
    return render(request, "articles/article_detail.html", context={"article": article})


@login_required(login_url="/accounts/login/")  # This decorator protects this view
def article_create(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            # Attach author to instance of article
            instance.author = request.user
            instance.save()
            return redirect("articles:list")
    else:
        form = forms.CreateArticle()
    return render(request, "articles/article_create.html", context={"form": form})
