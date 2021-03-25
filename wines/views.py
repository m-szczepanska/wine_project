from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from wines.models import Wine, Grade
from wines.forms import WineForm, AddGradeForm


@login_required
def wines_list(request):
    wines = Wine.objects.order_by('-created_at')
    context = {'wines': wines}
    return render(request, 'wines/list.html', context)


@login_required
def wine_details(request, wine_id):
    wine = Wine.objects.get(id=wine_id)
    context = {'wine': wine}
    return render(request, 'wines/wine_details.html', {'wine': wine})


@login_required
def add_wine(request):
    if request.method == "POST":
        form = WineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wines:wines_list')
    else:
        form = WineForm()
    return render(request, 'wines/add_wine.html', {'form': form})


@login_required
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

@login_required
def add_grade(request, wine_id):
    if request.method == "POST":
        form = AddGradeForm(request.POST)
        if form.is_valid():
            Grade.objects.create(
                user_id=request.user.id,
                wine_id=wine_id,
                grade=form.data['grade']
            )
            return redirect('wines:wine_details', wine_id)
    else:
        form = AddGradeForm()
    return render(request, 'wines/add_grade.html', {'form': form})