from django.shortcuts import render
from django.http import HttpResponse

def home_page_view(request):
    """
    Whenever this function is called, return text that says "Hello,
    World!"
    
    This is a function-based view: it returns a view from a function.
    """
    return HttpResponse("Hello, World!")

