from django.shortcuts import render
from .models import Registration
from .forms import RegoForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = RegoForm(request.POST)
        if form.is_valid():
            # Save stuff
            form.save()
            return render(request, 'rego/registered.html')
        return render(request, 'rego/index.html', {'form': form})
    r = len(Registration.objects.all())
    if r >= 20 or timeout():
        return render(request, 'rego/full.html')
    form = RegoForm()
    return render(request, 'rego/index.html', {'form': form})


def timeout():
    """ d0 is the registration close date (inclusive) """
    d0 = datetime.strptime('2019-09-11', '%Y-%m-%d')
    if datetime.now() < d0:
        return False
    return True
