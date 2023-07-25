from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    return HttpResponse("<h1>This is my first output in Django!!!</h1>")

def login(request):
    return HttpResponse("<marquee style='color:#BB860B; direction:'up';'>Welcome to Login Page</marquee>")

def tableDemo(request):
    return HttpResponse("""
    <table border=1 solid bgcolor='Red' style='text:white;' align='center'>  
        <tr>
            <th>First_Name</th>
            <th>Last_Name</th>
            <th>Marks</th>
        </tr>  
        <tr>
            <td>Sonoo</td>
            <td>Jaiswal</td>
            <td>60</td>
        </tr>  
        <tr>
            <td>James</td>
            <td>William</td>
            <td>80</td>
        </tr>  
        <tr>
            <td>Swati</td>
            <td>Sironi</td>
            <td>82</td>
        </tr>  
        <tr>
            <td>Chetna</td>
            <td>Singh</td>
            <td>72</td>
        </tr>  
    </table> 
""")