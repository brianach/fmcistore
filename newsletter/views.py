from django.shortcuts import render, redirect
from .forms import SubscriberForm
from .models import Subscriber
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if not Subscriber.objects.filter(email=email).exists():
                form.save()
                messages.success(request, 'You have successfully subscribed to the newsletter.')
            else:
                messages.warning(request, 'You are already subscribed to the newsletter.')
            return redirect('signup')
    else:
        form = SubscriberForm()
    return render(request, 'newsletter/signup.html', {'form': form})

def success(request):
    return render(request, 'newsletter/success.html')
