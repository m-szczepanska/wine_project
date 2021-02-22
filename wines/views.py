from django.shortcuts import render

from wines.models import Wine


def wines_list(request):
    wines = Wine.objects.order_by('-created_at')
    context = {'wines': wines}

    return render(request, 'wines/list.html', context)


def wine_details(request, wine_id):
    wine = Wine.objects.get(id=wine_id)
    context = {'wine': wine}

    return render(request, 'wines/details.html', {'wine': wine})