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
		

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question_id = forms.IntegerField(widget=forms.HiddenInput)

	def clean_text(self):
		if self.cleaned_data['text'] == "":
			raise forms.ValidationError("Text is empty", code='empty')
		return self.cleaned_data['text']

	def save(self):
		# won't be there if no question, no check
		qst = Question.objects.get(pk=self.cleaned_data['question_id'])
		return Answer.objects.create(
					question=qst,
					text=self.cleaned_data['text'])
