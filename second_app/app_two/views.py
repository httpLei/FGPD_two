from django.shortcuts import render

def home(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            context["greeting"] = f"Hello, {name}! Welcome to my Website."
    return render(request, 'app_two/home.html', context)
