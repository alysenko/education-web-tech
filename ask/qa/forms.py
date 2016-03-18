from django import forms
from models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class AskForm(forms.ModelForm):
#	title = forms.CharField(max_length=255)
#	text = forms.CharField(widget=forms.TextArea)

	_user = User

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

	def save(self, commit=True):
#		question = super(AskForm, self).save(commit=False)
		question = Question(title=self.cleaned_data['title'],
				    text=self.cleaned_data['text'],
				    author=self._user)
		question.save()
		return question
		

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
#	question_id = forms.IntegerField(widget=forms.HiddenInput)
	question_id = forms.IntegerField()

	_user = User

	def clean_text(self):
		if self.cleaned_data['text'] == "":
			raise forms.ValidationError("Text is empty", code='empty')
		return self.cleaned_data['text']

	def save(self):
		# won't be there if no question, no check
		qst = Question.objects.get(pk=self.cleaned_data['question_id'])
		return Answer.objects.create(
					question=qst,
					text=self.cleaned_data['text'],
					author=self._user)

class SignupForm(forms.Form):
	username = forms.CharField(max_length=50)
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField()

	def clean_username(self):
		try:
			User.objects.get(username=self.cleaned_data['username'])
		except User.DoesNotExist:
			return self.cleaned_data['username']
		raise forms.ValidationError("User exists", code='exist')

	def save(self):
		user = User()
		user.username = self.cleaned_data['username']
		user.email = self.cleaned_data['email']

		pasw = self.cleaned_data['password']
		user.set_password(pasw)
		user.save()

		user = authenticate(username=user.username, password=pasw)
		return user

class LoginForm(forms.Form):
	username = forms.CharField(max_length=50)
	password = forms.CharField(widget=forms.PasswordInput)

	error_messages = {
		'invalid': "<username, password> pair is invalid",
	}

	def clean(self):
		try:
			user = User.objects.get(username=self.data.get('username'))
		except User.DoesNotExist:
			raise forms.ValidationError(self.error_messages['invalid'], code=1)

		if not user.check_password(self.data.get('password')):
			raise forms.ValidationError(self.error_messages['invalid'], code=1)

		return self.data
		
