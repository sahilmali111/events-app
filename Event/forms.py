from django.forms import ModelForm
from .models import *


class eventform(ModelForm):
    class Meta:
        model = addevent
        fields = ['eventname', 'description', 'time', 'location', 'image']
