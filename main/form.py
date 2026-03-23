from .models import Note,Memory
from django import forms
class NoteForm(forms.ModelForm):
    """Form definition for Note."""

    class Meta:
        """Meta definition for Noteform."""

        model = Note
        fields = ['name','message']


class MemoryForm(forms.ModelForm):
    """Form definition for Note."""

    class Meta:
        """Meta definition for Noteform."""

        model = Memory
        fields = ['name','photo','caption']



