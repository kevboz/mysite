from django import forms
from .models import Item

# Create your models here.
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__" #['item_name', 'item_desc', 'item_price', 'item_image']""

    
