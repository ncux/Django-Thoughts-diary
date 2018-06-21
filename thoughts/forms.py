from django.forms import ModelForm

from .models import Thought

class ThoughtForm(ModelForm):

    class Meta:
        model = Thought
        fields = ('title', 'content',)