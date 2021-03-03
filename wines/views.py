from django.shortcuts import render, redirect

from wines.models import Wine
from wines.forms import WineForm


def wines_list(request):
    wines = Wine.objects.order_by('-created_at')
    context = {'wines': wines}
    return render(request, 'wines/list.html', context)


def wine_details(request, wine_id):
    wine = Wine.objects.get(id=wine_id)
    context = {'wine': wine}
    return render(request, 'wines/wine_details.html', {'wine': wine})


def add_wine(request):
    if request.method == "POST":
        form = WineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wines:wines_list')
    else:
        form = WineForm()
    return render(request, 'wines/add_wine.html', {'form': form})


def edit_wine(request, wine_id):
    wine = Wine.objects.get(id=wine_id)
    if request.method == "POST":
        form = WineForm(request.POST, instance=wine)
        if form.is_valid():
            form.save()
            return redirect('wines:wine_details', wine.id)
    else:
        form = WineForm(instance=wine)
    return render(request, 'wines/add_wine.html', {'form': form})