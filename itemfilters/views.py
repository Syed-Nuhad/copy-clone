from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Filter
from .forms import FilterForm

@login_required
def filter_list(request):
    filters = Filter.objects.filter(user=request.user)
    return render(request, 'filter_list.html', {'filters': filters})

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
    return render(request, 'add_filter.html', {'form': form})




@login_required
def edit_filter(request, pk):
    filter_obj = get_object_or_404(Filter, pk=pk, user=request.user)

    if request.method == 'POST':
        form = FilterForm(request.POST, instance=filter_obj)
        if form.is_valid():
            form.save()
            return redirect('itemfilters:filter_list')
    else:
        form = FilterForm(instance=filter_obj)

    return render(request, 'itemfilters/edit_filter.html', {'form': form})

@login_required
def delete_filter(request, pk):
    filter_obj = get_object_or_404(Filter, pk=pk, user=request.user)

    if request.method == 'POST':
        filter_obj.delete()
        return redirect('itemfilters:filter_list')

    return render(request, 'itemfilters/delete_confirm.html', {'filter': filter_obj})