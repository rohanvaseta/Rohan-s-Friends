from django import forms 
from .models import Friends


class FriendsForm(forms.ModelForm):
    
    class Meta:
        model = Friends
        fields = "__all__"