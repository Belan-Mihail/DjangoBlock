from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
# Now that trailing comma is  important there in fields,  
# otherwise Python will read this as a string  instead of a tuple, and that will cause an error.