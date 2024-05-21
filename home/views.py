from django.shortcuts import render, redirect
from .models import contactMessage
from django.contrib import messages
from .forms import ContactForm

# Create your views here.


def index(request):
    """ A view to render home page """

    return render(request, 'home/index.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was sent successfully! We will contact you shortly.')
            return redirect('home')  # Redirect to home or any other page after successful form submission
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})
