from django.urls import path
from . import views


#  Namespace the app so that you can reference specific list and details in your template
app_name = "resolve"

# URLConf
urlpatterns = [
    path("resolve", views.resolve_main, name="resolve"),
    path("unused", views.resolve_unused, name="unused"),
    # Here we capture the variable slug and send it through to the view:
    # path(
    #     "<slug:my_slug>/", views.article_detail, name="detail"
    # ),  # Named Capturing Group
]
