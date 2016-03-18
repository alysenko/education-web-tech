from django import forms
from models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

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
#	question_id = forms.IntegerField(widget=forms.HiddenInput)
	question_id = forms.IntegerField()

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

class SignupForm(forms.Form):
	username = forms.CharField(max_length=50)
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField()

	def save(self):
		name = self.cleaned_data['username']
		pasw = self.cleaned_data['password']
		mail = self.cleaned_data['email']
		user = User.objects.create_user(name, mail, pasw)
		user = authenticate(username=name, pasword=pasw)
		return user
