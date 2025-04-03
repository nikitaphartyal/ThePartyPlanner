from django import forms
from .models import Photo,Document
# from .models import Photo_venue
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file']