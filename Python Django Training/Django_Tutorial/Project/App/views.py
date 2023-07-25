from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    return HttpResponse("""
                        <h1>
                            This is First Tutorial in Django.
                        </h1>
                        """)