from django.shortcuts import render


def resolve_main(request):
    return render(
        request,
        template_name="resolve_views/resolve.html",
    )
