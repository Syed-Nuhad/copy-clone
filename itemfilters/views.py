from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Filter
from .forms import FilterForm

@login_required
def filter_list(request):
    filters = Filter.objects.filter(user=request.user)
    return render(request, 'itemfilters/filter_list.html', {'filters': filters})

@login_required
def add_filter(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            filter_obj = form.save(commit=False)
            filter_obj.user = request.user
            filter_obj.save()
            return redirect('itemfilters:filter_list')
    else:
        form = FilterForm()
    return render(request, 'itemfilters/add_filter.html', {'form': form})
