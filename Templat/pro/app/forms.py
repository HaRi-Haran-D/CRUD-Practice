from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name','descri','price','image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full outline-none bg-transparent',
                'placeholder': 'Mutton Biriyani'
            }),
            'descri': forms.Textarea(attrs={
                'class': 'w-full outline-none bg-transparent',
                'placeholder': 'Tender and Marinated Mutton ...',
                'rows': '1'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full outline-none bg-transparent',
                'placeholder': '15'
            }),
            'image': forms.URLInput(attrs={
                'class': 'w-full outline-none bg-transparent'
            }),
        }

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError("Price Cannot be Negative")
        return price
    
    def clean(self):
        cleaned = super().clean()
        name = cleaned.get('name')
        descri = cleaned.get('descri')
        if name and descri and name.lower() in descri.lower():
            self.add_error("descri","Description should add new info beyond the name")
        return cleaned