from datetime import datetime
from django.shortcuts import render
from .models import Registration
from .forms import RegoForm

# Create your views here.
def index(request):

    r = len(Registration.objects.all())
    p = 20 - r
    if timeout():
        return render(request, 'rego/timeout.html')
    if r >= 20:
        return render(request, 'rego/full.html')
    if 'registered' in request.session.keys():
        return render(request, 'rego/registered.html')

    if request.method == 'POST':
        form = RegoForm(request.POST)
        if form.is_valid():
            # Save stuff
            form.save()
            request.session['registered'] = True
            return render(request, 'rego/registered.html')
        return render(request, 'rego/index.html',
                {'form': form, 'places_left': p})

    form = RegoForm()
    return render(request, 'rego/index.html', {'form': form, 'places_left': p})


def timeout():
    """ d0 is the registration close date (inclusive) """
    d0 = datetime.strptime('2019-09-11', '%Y-%m-%d')
    if datetime.now() < d0:
        return False
    return True
