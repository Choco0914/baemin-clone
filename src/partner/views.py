from django.shortcuts import render

def signup(request):
    """Define signup pages"""

    context={}
    
    return render(request, "partner/signup.html", context)
