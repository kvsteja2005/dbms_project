from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_description','host_details', 'event_time', 'event_location','event_fee', 'event_image']
