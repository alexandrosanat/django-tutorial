from django.shortcuts import render


def manipulate_input(input_text):
    # Perform your manipulation logic here
    # For example, you can convert the input to uppercase
    return input_text.upper()


def resolve_main(request):
    user_input = ""
    output = ""

    if request.method == "POST":
        user_input = request.POST.get("user_input", "")  # Retrieve the user's input

        # Manipulate the user input before displaying it
        output = manipulate_input(user_input)

    return render(
        request,
        "resolve_views/resolve.html",
        {"user_input": user_input, "output": output},
    )
