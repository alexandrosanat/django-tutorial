from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def signup_view(request):
    # First check if request is POST
    if request.method == "POST":
        # By passing the data back to a new instance of the form we
        # are validating the data
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in
            return redirect("articles:list")
    else:
        # If it's a GET request then go to the forms
        form = UserCreationForm()
    # This will still run if the if fails
    return render(request, "accounts/signup.html", {"form": form})
