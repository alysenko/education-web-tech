from django import forms
from models import Question, Answer

class AskForm(forms.ModelForm):
#	title = forms.CharField(max_length=255)
#	text = forms.CharField(widget=forms.TextArea)
	class Meta:
		model = Question
		fields = ['title', 'text']
	def clean_title(self):
		if self.cleaned_data['title'] == "":
			raise forms.ValidationError("Title is empty", code='empty')
		return self.cleaned_data['title']
	def clean_text(self):
		if self.cleaned_data['text'] == "":
			raise forms.ValidationError("Text is empty", code='empty')
		return self.cleaned_data['text']
		

class AnswerForm(forms.ModelForm):
#	text = forms.CharField(widget=forms.TextArea)
#	question = forms.IntegerField(widget=forms.HiddenInput)
	class Meta:
		model = Answer
		fields = ['text', 'question']
	def clean_text(self):
		if self.cleaned_data['text'] == "":
			raise forms.ValidationError("Text is empty", code='empty')
		return self.cleaned_data['text']
