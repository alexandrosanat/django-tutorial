from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def signup_view(request):
    # First check if request is POST
    if request.method == "POST":
        # By passing the data back to a new instance of the form we
        # are validating the data
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect("accounts:login")  # Redirect to the login page
    else:
        # If it's a GET request then go to the forms
        form = UserCreationForm()
    # This will still run if the if fails
    return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        # Get the username and password from the submitted form
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            messages.success(request, "Login successful.")

            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("articles:list")
        else:
            messages.error(request, "Invalid username or password.")

    # If the request method is GET or authentication failed, display login form
    form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    if request.method == "POST":
        # Use the logout() function to log the user out
        logout(request)
    return redirect(
        "articles:list"
    )  # Redirect to the home page or any desired page after logout
