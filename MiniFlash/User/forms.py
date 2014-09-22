from allauth.account.forms import SignupForm
from django.forms import ModelForm
from models import CustomUser

class CustomSignupForm(SignupForm):
	def signup(self, request, user):
		pass

	def __init__(self, *args, **kwargs):
		self.fields.pop('password2')
		self.fields.pop('username')
		self.fields['email'].label = ''
		self.fields['email'].widget.attrs['placeholder'] = 'Email'
		self.fields['password1'].label = ''
		super(CustomSignupForm, self).__init__(*args, **kwargs)

class UserSettingsForm(ModelForm):
	class Meta:
		model = CustomUser
		fields = ['username', 'short_description', 'logo']

	def __init__(self, *args, **kwargs):
		self.fields['username'].help_text = ""
		super(UserSettingsForm, self).__init__(*args, **kwargs)