from django import forms

from .models import MenuItem


class MenuItemForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('', 'Оберіть категорію'),
        ('Кухня', 'Кухня'),
        ('Бар', 'Бар'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}),
                                 label='Категорія')
    image = forms.ImageField(label='Зображення', required=False)

    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'category', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'price': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }

        labels = {
            'name': 'Назва',
            'description': 'Опис',
            'price': 'Ціна',
        }
