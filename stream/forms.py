from django import forms
from stream.models import anime, user
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm

class AnimeForm(forms.ModelForm):
    # name= forms.CharField(max_length=100, label=False, widget= forms.TextInput(attrs={'placeholder':'Movie Name','id':'txt'}))
    clue_id= forms.IntegerField(label=False, widget= forms.NumberInput(attrs={'placeholder':'bbb','id':'num'}))
    clue= forms.CharField(label=False, widget= forms.TextInput(attrs={'placeholder':'Answer','id':'pass'}))
    class Meta:
        model=anime
        fields='__all__'

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.pop("autofocus", None)
        self.fields['old_password'].widget.attrs.update({'placeholder':'Old Password','id':'pass'})
        self.fields['new_password1'].widget.attrs.update({'placeholder':'New Password','id':'pass'})
        self.fields['new_password2'].widget.attrs.update({'placeholder':'Confirm Password','id':'pass'})
        self.fields['old_password'].label=False
        self.fields['new_password1'].label=False
        self.fields['new_password2'].label=False

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)
        self.fields['username'].widget.attrs.update({'placeholder':'Contestent ID','id':'txt'})
        self.fields['password'].widget.attrs.update({'placeholder':'Password','id':'pass'})
        self.fields['username'].label=False
        self.fields['password'].label=False

class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder':'Email','id':'mail'})
        self.fields['email'].label=False

class CreateUser(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUser, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)
        #self.fields['dob'].widget.attrs.pop("autofocus", None)
        self.fields['username'].widget.attrs.update({'placeholder':'Contestent ID','id':'txt'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Password','id':'pass_s'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Confirm Password','id':'pass_s'})
        self.fields['password1'].label=False
        self.fields['password1'].help_text=None
        self.fields['password2'].label=False
        self.fields['password2'].help_text=False
    name= forms.CharField(max_length=100, label= False, widget= forms.TextInput(attrs={'placeholder':'First Name','id':'txt_s'}))
    #last_name= forms.CharField(max_length=100, label= False, widget= forms.TextInput(attrs={'placeholder':'Last Name','id':'txt_s'}))
    #dob= forms.DateField(label=False,required=False, widget= forms.DateInput(attrs={'placeholder':'Date of Birth','id':'num_s','onfocus':'(this.type="date")','onblur':'(this.type="text")',}))
    #email= forms.EmailField(max_length=100,label=False, widget= forms.EmailInput(attrs={'placeholder':'Email','id':'mail'}))
    #username= forms.CharField(min_length=5, max_length=100, label=False, widget= forms.TextInput(attrs={'placeholder':'Username'}))

    class Meta(UserCreationForm.Meta):
        model=user
        fields=UserCreationForm.Meta.fields + ('name',)

# Create a UserUpdateForm to update username and email
class UserUpdateForm(forms.ModelForm):
    email= forms.EmailField(max_length=100,label=False, widget= forms.EmailInput(attrs={'placeholder':'Email','id':'mail'}))
    username= forms.CharField(min_length=5, max_length=100, label=False, widget= forms.TextInput(attrs={'placeholder':'Username','id':'txt'}))

    class Meta:
        model = user
        fields = ['username', 'email']

# # Create a ProfileUpdateForm to update image
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']