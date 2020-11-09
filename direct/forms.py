from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
	body = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}), required=True)
	class Meta:
		model = Message
		fields = ('body',)