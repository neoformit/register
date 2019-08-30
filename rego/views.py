from datetime import datetime
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Registration
from .forms import RegoForm

# Create your views here.
def index(request):

    r = len(Registration.objects.all())
    p = settings.NO_PLACES - r
    time = datetime.strftime(datetime.now(), '%H:%M:%S %d-%m-%Y')

    if timeout():
        return render(request, 'rego/timeout.html')

    if r >= 20:
        return render(request, 'rego/full.html')

    if 'registered' in request.session.keys():
        if request.session['registered']:
            return render(request, 'rego/registered.html')

    if request.method == 'POST':
        form = RegoForm(request.POST)
        if form.is_valid():
            # Save stuff
            form.save()
            request.session['registered'] = form.cleaned_data['email']
            return render(request, 'rego/registered.html')
        return render(request, 'rego/index.html',
                {'form': form, 'places_left': p, 'current_time': time})

    form = RegoForm()
    return render(request, 'rego/index.html',
            {'form': form, 'places_left': p, 'current_time': time})


def timeout():
    """ d0 is the registration close date (inclusive) """
    d0 = datetime.strptime(settings.TIMEOUT_DATE, '%Y-%m-%d')
    if datetime.now() < d0:
        return False
    return True


def cancel(request):
    """ Cancel booking and return to homepage """
    user_email = request.session['registered']
    r = Registration.objects.get(email=user_email)
    r.delete()
    request.session['registered'] = None
    return redirect('/')
