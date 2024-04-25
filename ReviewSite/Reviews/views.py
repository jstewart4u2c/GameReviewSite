from django.shortcuts import render, redirect
from .models import Review
from .forms import ContactForm
from django.contrib import messages


# Create your views here.
def review_list(request):
    review = Review.objects.all()
    return render(request, 'Reviews/review_list.html', {'review': review})


def review_details(request, review_id):
    review = Review.objects.get(pk=review_id)

    return render(request, 'Reviews/review_details.html', {'review': review})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your contact request has been submitted.')
            return redirect('review_list')
    else:
        form = ContactForm()
    return render(request, 'Reviews/contact.html', {'form': form})
