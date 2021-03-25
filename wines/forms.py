from django.forms import ModelForm

from wines.models import Wine, Grade, User


class WineForm(ModelForm):
    class Meta:
        model = Wine
        fields = '__all__'


class AddGradeForm(ModelForm):
    class Meta:
        model = Grade
        fields = ('grade',)