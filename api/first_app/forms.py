from django import forms
from django.forms import NumberInput
from first_app.models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["name", "videofile"]

class vpreview(forms.Form):
    name=forms.CharField()

class vgen(forms.Form):
    #name=forms.FilePathField( path='media/videos/',match='.*mp4$')
    fps=forms.IntegerField(widget=NumberInput(attrs={'type':'range', 'step': '1','min':'1', 'max': '10', 'value': '4'}))