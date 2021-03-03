from django.forms import ModelForm

from wines.models import Wine


class WineForm(ModelForm):
    class Meta:
        model = Wine
        fields = '__all__'