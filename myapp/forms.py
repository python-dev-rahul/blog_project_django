# forms.py
from django import forms
from .models import Post

class MyPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['pub_date']
        fields = ['image', 'background_color', 'heading', 'title', 'slug', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})  # Add Bootstrap class or any other styling class

    def error_messages(self):
        return {
            'required': 'This field is required.',
            'invalid': 'Enter a valid value.',
            'unique': 'This value must be unique.',
            # Add more custom error messages if needed
        }
