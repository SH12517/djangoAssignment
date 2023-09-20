from django.http import HttpResponse
from django.shortcuts import render, redirect
import random
import datetime
from django.contrib import messages

def homePage(request):
    quotes = [
        "Life is what happens when you're busy making other plans By Shailendra Yadav.",
        "The only way to do great work is to love what you do .",
        "In the middle of every difficulty lies opportunity."
    ]
    random_quote = random.choice(quotes)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'index.html', {'current_time': current_time, 'random_quote': random_quote})




def submit(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        messages.success(request, 'Form submitted successfully.')
        return render(request, 'data.html', {'name': name, 'email': email})
        
     else:
        return redirect('homePage')
