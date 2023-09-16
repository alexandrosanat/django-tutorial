from django.urls import path, re_path
from . import views


#  Namespace the app so that you can reference specific list and details in your template
app_name = 'articles'

# URLConf
urlpatterns = [
    path("hello/", views.say_hello, name="hello"),
    re_path(r'^$', views.article_list, name="list"),
     # Here we capture the variable slug and send it through to the view:
    path('<slug:my_slug>/', views.article_detail, name="detail")  # Named Capturing Group
]