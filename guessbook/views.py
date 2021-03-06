from django.shortcuts import render

from guessbook.forms import GuestEntryForm
from guessbook.models import GuestEntry, Hit


def home(request):
    if request.method == 'POST':
        form = GuestEntryForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = GuestEntryForm()

    entries = GuestEntry.objects.all()[:10]

    # Create a new hit for our hit counter
    Hit().save()
    Hit().save()
    Hit().save() 

    hits = Hit.objects.count()

    return render(request, 'main.html', {
        'entries': entries, 'form': form, 'hits': hits
    })
