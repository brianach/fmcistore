from django import forms
from .widgets import CustomClearableFileInput
from .models import StoreItem, Category

class StoreItemForm(forms.ModelForm):

    class Meta:
        model = StoreItem
        fields = '__all__'

    #if StoreItem.category != 3:
    #    image_one = forms.ImageField(label='Image one', required=False, widget=CustomClearableFileInput)
    #    image_two = forms.ImageField(label='Image two', required=False, widget=CustomClearableFileInput)
    #else:
    #    image_one = forms.ImageField(label='Image one', required=False, widget=CustomClearableFileInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names

        if self.instance.image_one:
            self.fields['image_one'] = forms.ImageField(label='Image one', required=False, widget=CustomClearableFileInput)

        if self.instance.image_two:
            self.fields['image_two'] = forms.ImageField(label='Image two', required=False, widget=CustomClearableFileInput)

        # Access the current value of the category field
        category_value = self.instance.category if self.instance else None

        # Remove the unnecessary field based on the category
        #if category_value == 3:  # Change 3 to the actual ID for "accessories"
        #    del self.fields['image_two']

        # Set class for all fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
